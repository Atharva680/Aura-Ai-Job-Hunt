import json
import os
import glob
from datetime import datetime, timedelta

# Constants
SEEN_JOBS_FILE = '.claude/skills/job-scraper/seen_jobs.json'
TRACKER_FILE = 'job_search_tracker.csv'

# Profile signals for quick fit
STRONG_SKILLS = {'rag', 'langchain', 'openai', 'vector', 'pgvector', 'pinecone', 'databricks', 'spark', 'delta lake', 'fastapi', 'azure', 'mlops'}
MODERATE_SKILLS = {'tensorflow', 'pytorch', 'opencv', 'nlp', 'reinforcement learning', 'node.js', 'react', 'postgresql'}

def quick_fit(title, company, description=''):
    text = (title + ' ' + company + ' ' + description).lower()
    if any(skill in text for skill in STRONG_SKILLS):
        return 'High'
    if any(skill in text for skill in MODERATE_SKILLS):
        return 'Medium'
    return 'Low'

def load_json(path):
    if not os.path.exists(path):
        return {}
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return {}

def main():
    # 1. Load State
    seen_data = load_json(SEEN_JOBS_FILE).get('seen', {})

    # Load tracker (simple check)
    applied_keys = set()
    if os.path.exists(TRACKER_FILE):
        with open(TRACKER_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                applied_keys.add(line.strip())

    # 2. Aggregate Search Results
    all_results = []
    files = glob.glob('search_*.json')

    for file in files:
        portal = 'linkedin-search' if 'linkedin' in file else 'freehire-search'
        source = 'cli'

        try:
            with open(file, 'r', encoding='utf-8-sig') as f:
                data = json.load(f)
                # Support both formats: {results: [...]} and [...]
                results = data.get('results', data) if isinstance(data, dict) else data

                for res in results:
                    # Standardize fields
                    title = res.get('title', 'Unknown')
                    company = res.get('company', 'Unknown')
                    location = res.get('location', 'Unknown')
                    url = res.get('url', '')
                    date_str = res.get('date') or res.get('posted_at')

                    if not url: continue

                    key = f"{company}_{title}_{url}"
                    if key in seen_data or key in applied_keys:
                        continue

                    # Date filter (14 days)
                    if date_str:
                        try:
                            # Try common formats
                            for fmt in ('%Y-%m-%d', '%Y-%m-%dT%H:%M:%SZ', '%b %d, %Y'):
                                try:
                                    posted_date = datetime.strptime(date_str, fmt)
                                    break
                                except: continue
                        except:
                            posted_date = None
                    else:
                        posted_date = None

                    if posted_date and (datetime.now() - posted_date).days > 14:
                        continue

                    all_results.append({
                        'title': title,
                        'company': company,
                        'location': location,
                        'url': url,
                        'date': date_str,
                        'portal': portal,
                        'source': source,
                        'fit': quick_fit(title, company)
                    })
        except Exception as e:
            print(f"Error reading {file}: {e}")

    # 3. Deduplicate within run (mass-posting)
    final_jobs = []
    seen_in_run = {}
    for job in all_results:
        # Group by company + title (normalized)
        group_key = f"{job['company'].lower()}_{job['title'].lower()}"
        if group_key in seen_in_run:
            existing = seen_in_run[group_key]
            if existing['location'] != job['location']:
                existing['location'] += f", {job['location']}"
                existing['mass_posted'] = True
            continue

        job['mass_posted'] = False
        seen_in_run[group_key] = job
        final_jobs.append(job)

    # 4. Store and Present
    new_seen = {}
    for job in final_jobs:
        key = f"{job['company']}_{job['title']}_{job['url']}"
        new_seen[key] = {
            'title': job['title'],
            'company': job['company'],
            'url': job['url'],
            'first_seen': datetime.now().strftime('%Y-%m-%d'),
            'posted_date': job['date'],
            'fit': job['fit'],
            'status': 'new',
            'portal': job['portal'],
            'source': job['source']
        }

    # Save to seen_jobs.json
    os.makedirs(os.path.dirname(SEEN_JOBS_FILE), exist_ok=True)
    with open(SEEN_JOBS_FILE, 'w', encoding='utf-8') as f:
        json.dump({'seen': {**seen_data, **new_seen}}, f, indent=2)

    # Output for Claude
    print("## New Job Matches - 2026-09-01\n")

    high_matches = [j for j in final_jobs if j['fit'] == 'High']
    med_matches = [j for j in final_jobs if j['fit'] == 'Medium']
    low_matches = [j for j in final_jobs if j['fit'] == 'Low']

    print(f"Found {len(final_jobs)} new positions ({len(high_matches)} high, {len(med_matches)} medium, {len(low_matches)} low match).\n")

    print("| # | Fit | Title | Company | Location | URL |")
    print("|---|-----|-------|---------|----------|-----|")

    sorted_jobs = high_matches + med_matches + low_matches
    for i, job in enumerate(sorted_jobs, 1):
        title = job['title']
        if job['mass_posted']:
            title += " (posted in multiple cities)"

        print(f"| {i} | {job['fit']} | {title} | {job['company']} | {job['location']} | [Link]({job['url']}) |")

if __name__ == '__main__':
    main()
