import json
import re
import os
from datetime import datetime
from tools.job_pipeline import scrape_all_jobs, bucket_jobs

# ============================================================
# CONFIGURATION & RULES
# ============================================================

TARGET_ROLES = ["AI Engineer", "ML Engineer", "Data Engineer", "Python Developer", "GenAI", "LLM"]
CORE_SKILLS = ["rag", "langchain", "databricks", "spark", "fastapi", "azure", "openai", "vector search", "pgvector"]
PREFERRED_CITIES = ["bangalore", "hyderabad", "pune", "mumbai", "nagpur", "remote"]

NEGATIVE_SENIORITY = ["senior", "lead", "staff", "architect", "manager", "mid-senior", "principal"]
POSITIVE_SENIORITY = ["fresher", "graduate", "junior", "associate", "trainee", "entry level", "early career"]

# ============================================================
# UTILITIES
# ============================================================

def parse_posted_date(date_str):
    """Robust date parsing based on filter_fresh_postings.py logic."""
    if not date_str:
        return None

    date_str = date_str.lower().strip()
    now = datetime.now()

    # Handle relative dates
    if "hour" in date_str:
        match = re.search(r"(\d+)", date_str)
        if match: return now # Approx current day
    if "day" in date_str:
        match = re.search(r"(\d+)", date_str)
        if match: return now # Approx current week
    if "week" in date_str:
        return now # Approx current month

    # Handle ISO and common formats
    formats = ["%Y-%m-%d", "%B %d, %Y", "%d %B %Y", "%Y-%m-%dT%H:%M:%SZ"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None

def extract_experience(text):
    """Extracts years of experience from text using regex."""
    if not text: return None
    text = text.lower()
    # Patterns: "2-4 years", "5+ years", "min 3 years", "0-1 year"
    pattern = r"(\d+)\s*(?:-|to)?\s*(\d+)?\s*years?"
    match = re.search(pattern, text)
    if match:
        min_exp = int(match.group(1))
        max_exp = int(match.group(2)) if match.group(2) else min_exp
        return (min_exp, max_exp)
    return None

# ============================================================
# FILTERING & SCORING
# ============================================================

def apply_seniority_filter(job):
    """
    Implements the MANDATORY SENIORITY FILTER.
    Returns: (is_passed, classification, reason)
    """
    desc = (job.get("description", "") or "").lower()
    title = (job.get("title", "") or "").lower()

    # 1. Check Negative Keywords (Hard Reject)
    for word in NEGATIVE_SENIORITY:
        if word in title or word in desc:
            # For safety, if "Senior" is in title, it's a reject.
            if word in title:
                return False, "❌ REJECT", f"Seniority mismatch: {word} in title"

    # 2. Experience Range Check
    exp = extract_experience(desc)
    if exp:
        min_exp, max_exp = exp
        if min_exp >= 4:
            return False, "❌ REJECT", f"Experience required: {min_exp}+ years"
        if min_exp >= 2:
            return True, "🟡 STRETCH", f"Experience gap: {min_exp}-{max_exp} years"
        if min_exp <= 1:
            return True, "🔥 HIGH PRIORITY", "Perfect entry-level match"

    # 3. Positive Indicators
    for word in POSITIVE_SENIORITY:
        if word in title or word in desc:
            return True, "🔥 HIGH PRIORITY", "Explicitly entry-level"

    return True, "✅ GOOD FIT", "Compatible seniority"

def calculate_relevance_score(job):
    """Calculates a weighted relevance score 0-100."""
    score = 0
    title = (job.get("title", "") or "").lower()
    desc = (job.get("description", "") or "").lower()
    loc = (job.get("location", "") or "").lower()

    # Seniority Fit (30%) - Already passed filter, so give baseline
    score += 20

    # Role Fit (25%)
    for role in TARGET_ROLES:
        if role.lower() in title:
            score += 25
            break

    # Technical Skill Fit (20%)
    skill_matches = 0
    for skill in CORE_SKILLS:
        if skill in desc or skill in title:
            skill_matches += 1
    score += min(20, skill_matches * 4)

    # Location Fit (10%)
    for city in PREFERRED_CITIES:
        if city in loc:
            score += 10
            break

    # Evidence Baseline (15%) - Assuming candidate has the internship
    score += 15

    return min(100, score)

# ============================================================
# MAIN PIPELINE
# ============================================================

def run_master_pipeline():
    print("🚀 Starting Master AI Job Pipeline...")

    # Phase 1: Scraping
    raw_jobs = scrape_all_jobs()
    total_scraped = len(raw_jobs)
    print(f"📦 Scraped {total_scraped} unique jobs.")

    # Phase 2: Filtering
    filtered_jobs = []
    rejected_count = 0

    for job in raw_jobs:
        # Freshness Check
        posted_date = parse_posted_date(job.get("date") or job.get("posted_at"))
        if not posted_date or (datetime.now() - posted_date).days > 7:
            continue

        # Seniority Filter
        passed, classification, reason = apply_seniority_filter(job)
        if not passed:
            rejected_count += 1
            continue

        # Scoring
        score = calculate_relevance_score(job)

        job["seniority_classification"] = classification
        job["relevance_score"] = score
        job["filter_reason"] = reason
        filtered_jobs.append(job)

    print(f"🛡️  Seniority Filter: Rejected {rejected_count} unsuitable roles.")
    print(f"🎯 Found {len(filtered_jobs)} relevant jobs.")

    # Phase 3: Dashboard Update
    dashboard_data = bucket_jobs(filtered_jobs)

    # Save JSON for backup/API
    with open("jobs_dashboard_data.json", "w") as f:
        json.dump(dashboard_data, f, indent=2)

    # BAKE data into HTML to avoid CORS issues when opening locally
    try:
        with open("job_dashboard.html", "r", encoding="utf-8") as f:
            html_content = f.read()

        # Replace placeholder with JSON string
        updated_html = html_content.replace("{{JOB_DATA}}", json.dumps(dashboard_data))

        with open("job_dashboard.html", "w", encoding="utf-8") as f:
            f.write(updated_html)
        print("📊 Dashboard HTML baked and updated successfully.")
    except Exception as e:
        print(f"⚠️  Warning: Could not update HTML dashboard directly: {e}")

    # Phase 4: Tailor Queue
    # Sort by score descending
    sorted_jobs = sorted(filtered_jobs, key=lambda x: x["relevance_score"], reverse=True)
    top_jobs = sorted_jobs[:5]

    queue = []
    for j in top_jobs:
        queue.append({
            "id": j.get("id"),
            "title": j.get("title"),
            "company": j.get("company"),
            "url": j.get("url"),
            "score": j.get("relevance_score"),
            "classification": j.get("seniority_classification")
        })

    with open("tailor_queue.json", "w") as f:
        json.dump(queue, f, indent=2)
    print("📝 Tailor queue updated with top 5 matches.")

    # Final Report
    print("\n" + "="*60)
    print(f"{'Job Title':<30} | {'Company':<20} | {'Score':<5}")
    print("-" * 60)
    for j in top_jobs:
        print(f"{j.get('title', 'N/A')[:30]:<30} | {j.get('company', 'N/A')[:20]:<20} | {j.get('relevance_score'):<5}")
    print("="*60)
    print("\nRun /resume-tailor for the jobs in tailor_queue.json")

if __name__ == "__main__":
    run_master_pipeline()
