import subprocess
import json
import os
from datetime import datetime, timedelta

# Configuration
PORTALS = {
    "linkedin-search": {
        "cmd": "bun run .agents/skills/linkedin-search/cli/src/cli.ts search",
        "args": lambda q, l: ["-q", q, "-l", l, "--format", "json", "--limit", "20"]
    },
    "freehire-search": {
        "cmd": "bun run .agents/skills/freehire-search/cli/src/cli.ts search",
        "args": lambda q, l: ["-q", f"{q} {l}", "--format", "json", "--limit", "20"]
    }
}

QUERIES = ["AI Engineer", "ML Engineer", "Data Engineer", "Python Developer"]
LOCATIONS = ["Bangalore, Karnataka, India", "Hyderabad, Telangana, India", "Pune, Maharashtra, India", "Mumbai, Maharashtra, India", "Nagpur, Maharashtra, India", "Remote"]

def run_command(cmd, args):
    full_cmd = f"{cmd} {' '.join(args)}"
    try:
        result = subprocess.run(full_cmd, shell=True, capture_output=True, text=True, timeout=60, encoding="utf-8")
        if result.returncode == 0:
            return json.loads(result.stdout)
        return None
    except Exception as e:
        print(f"Error running {full_cmd}: {e}")
        return None

def parse_date(date_str):
    if not date_str:
        return None
    formats = [
        "%Y-%m-%d",
        "%B %d, %Y",
        "%d %B %Y",
        "%Y-%m-%dT%H:%M:%SZ"
    ]
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None

def scrape_all_jobs():
    all_jobs = []
    for portal_name, config in PORTALS.items():
        print(f"Scraping {portal_name}...")
        for q in QUERIES:
            for l in LOCATIONS:
                args = config["args"](q, l)
                data = run_command(config["cmd"], args)
                if data:
                    jobs = []
                    if isinstance(data, list):
                        jobs = data
                    elif isinstance(data, dict):
                        jobs = data.get("results", data.get("jobs", []))
                    for job in jobs:
                        job["portal"] = portal_name
                        all_jobs.append(job)

    seen_urls = set()
    unique_jobs = []
    for job in all_jobs:
        url = job.get("url")
        if url and url not in seen_urls:
            seen_urls.add(url)
            unique_jobs.append(job)
    return unique_jobs

def bucket_jobs(jobs):
    now = datetime.now()
    buckets = {
        "3h": [], "5h": [], "8h": [], "12h": [], "24h": [], "1d": [], "7d": []
    }
    processed_jobs = []
    for job in jobs:
        date_str = job.get("date") or job.get("posted_at")
        posted_date = parse_date(date_str)
        if posted_date:
            diff = now - posted_date
            hours = diff.total_seconds() / 3600
            if hours <= 3: buckets["3h"].append(job)
            if hours <= 5: buckets["5h"].append(job)
            if hours <= 8: buckets["8h"].append(job)
            if hours <= 12: buckets["12h"].append(job)
            if hours <= 24: buckets["24h"].append(job)
            if hours <= 24: buckets["1d"].append(job)
            if hours <= 168: buckets["7d"].append(job)
            processed_jobs.append({**job, "hours_ago": round(hours, 1), "posted_at": date_str})

    return {
        "last_updated": now.isoformat(),
        "counts": {k: len(v) for k, v in buckets.items()},
        "jobs": processed_jobs[:100]
    }

def main():
    jobs = scrape_all_jobs()
    dashboard_data = bucket_jobs(jobs)
    with open("jobs_dashboard_data.json", "w") as f:
        json.dump(dashboard_data, f, indent=2)
    print("Pipeline complete. Data saved to jobs_dashboard_data.json")

if __name__ == "__main__":
    main()
