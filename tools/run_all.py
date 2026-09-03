#!/usr/bin/env python3
"""Run the fresh-job discovery, triage, staging, and dashboard workflow.

This entrypoint is intentionally *not* an unattended application submitter.
It produces an approval queue; each selected posting must continue through the
interactive /apply workflow, which verifies the posting and creates tailored
documents before the candidate decides whether to submit.
"""

from __future__ import annotations

import argparse
import csv
import json
import shutil
import subprocess
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "jobs_data"
FILTER_SCRIPT = ROOT / "tools" / "filter_fresh_postings.py"
LINKEDIN = ROOT / ".agents" / "skills" / "linkedin-search" / "cli" / "src" / "cli.ts"
FREEHIRE = ROOT / ".agents" / "skills" / "freehire-search" / "cli" / "src" / "cli.ts"

# Keep the live run focused and respectful of public job-board rate limits.
LINKEDIN_SEARCHES = (
    ("junior data engineer", "India", None),
    ("junior python developer", "India", None),
    ("fresher AI ML engineer", "India", None),
    ("junior AI engineer", "Remote", "remote"),
    ("associate AI engineer", "India", None),
    ("graduate ML engineer", "India", None),
    ("entry level data engineer", "India", None),
    ("GenAI engineer", "India", None),
    ("LLM engineer", "India", None),
)
FREEHIRE_SEARCHES = (
    ("junior data engineer", ("--country", "IN")),
    ("junior python developer", ("--country", "IN")),
    ("fresher machine learning engineer", ("--country", "IN")),
    ("junior AI engineer", ("--remote", "remote")),
    ("associate AI engineer", ("--country", "IN")),
    ("graduate ML engineer", ("--country", "IN")),
    ("GenAI engineer", ("--country", "IN")),
)
ENTRY_MARKERS = ("junior", "associate", "graduate", "fresher", "entry level", "engineer i", "engineer 1")
PROFILE_MARKERS = (
    "ai", "machine learning", "ml", "data engineer", "python", "generative", "llm", "rag", "databricks",
)


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=ROOT, encoding="utf-8", capture_output=True, check=False)


def read_envelope(text: str | None, source: str) -> dict[str, Any] | None:
    if text is None:
        print(f"warning: {source} returned no output; skipped", file=sys.stderr)
        return None
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        print(f"warning: {source} returned non-JSON output; skipped", file=sys.stderr)
        return None
    return payload if isinstance(payload, dict) and isinstance(payload.get("results"), list) else None


def fresh_envelope(payload: dict[str, Any], max_days: int) -> dict[str, Any] | None:
    filtered = subprocess.run(
        [sys.executable, str(FILTER_SCRIPT), "--max-days", str(max_days)],
        cwd=ROOT,
        input=json.dumps(payload),
        text=True,
        capture_output=True,
        check=False,
    )
    if filtered.returncode:
        print(f"warning: freshness filter failed: {filtered.stderr.strip()}", file=sys.stderr)
        return None
    return read_envelope(filtered.stdout, "freshness filter")


def search_live(max_days: int) -> list[dict[str, Any]]:
    if shutil.which("bun") is None:
        print("warning: Bun is unavailable; using existing cached files only", file=sys.stderr)
        return []
    results: list[dict[str, Any]] = []
    for query, location, remote in LINKEDIN_SEARCHES:
        command = ["bun", "run", str(LINKEDIN), "search", "--query", query, "--location", location,
                   "--jobage", str(max_days), "--limit", "50", "--format", "json"]
        if remote:
            command.extend(("--remote", remote))
        completed = run(command)
        payload = read_envelope(completed.stdout, f"LinkedIn {query}") if not completed.returncode else None
        if payload:
            payload = fresh_envelope(payload, max_days)
            if payload:
                results.extend({**job, "portal": "linkedin-search", "source": "cli"} for job in payload["results"])
    for query, extra in FREEHIRE_SEARCHES:
        command = ["bun", "run", str(FREEHIRE), "search", "--query", query, "--jobage", str(max_days),
                   "--limit", "50", "--no-description", "--format", "json", *extra]
        completed = run(command)
        payload = read_envelope(completed.stdout, f"Freehire {query}") if not completed.returncode else None
        if payload:
            payload = fresh_envelope(payload, max_days)
            if payload:
                results.extend({**job, "portal": "freehire-search", "source": "cli"} for job in payload["results"])
    return results


def read_cached(max_days: int) -> list[dict[str, Any]]:
    jobs: list[dict[str, Any]] = []
    for path in DATA.glob("search_*.json"):
        try:
            payload = json.loads(path.read_text(encoding="utf-8-sig"))
        except (OSError, json.JSONDecodeError):
            continue
        envelope = payload if isinstance(payload, dict) else {"results": payload}
        filtered = fresh_envelope(envelope, max_days)
        if filtered:
            portal = "freehire-search" if "freehire" in path.name else "linkedin-search"
            jobs.extend({**job, "portal": portal, "source": "cache"} for job in filtered["results"])
    return jobs


def normalize_jobs(jobs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    unique: dict[str, dict[str, Any]] = {}
    for job in jobs:
        title = str(job.get("title") or "").strip()
        company = str(job.get("company") or "").strip()
        url = str(job.get("url") or "").strip()
        if not (title and company and url):
            continue
        title_lower = title.lower()
        if not any(marker in title_lower for marker in ENTRY_MARKERS):
            continue
        corpus = f"{title} {job.get('description') or ''}".lower()
        if not any(marker in corpus for marker in PROFILE_MARKERS):
            continue
        key = url.split("?")[0].lower()
        posted = str(job.get("posted_date") or job.get("date") or "")[:10]
        unique.setdefault(key, {
            "title": title, "company": company, "location": job.get("location"), "url": url,
            "posted_date": posted, "portal": job.get("portal"), "source": job.get("source"),
            "work_mode": job.get("work_mode"), "skills": job.get("skills") or [],
            "fit_signal": "high" if any(marker in corpus for marker in ("databricks", "langchain", "fastapi", "spark", "python")) else "medium",
            "status": "needs_review",
        })
    return sorted(unique.values(), key=lambda job: job["posted_date"], reverse=True)


def write_outputs(jobs: list[dict[str, Any]], max_days: int) -> None:
    DATA.mkdir(exist_ok=True)
    metadata = {"generated_at": datetime.now(timezone.utc).isoformat(), "max_posting_age_days": max_days, "jobs": jobs}

    # JSON outputs
    (DATA / "all_jobs.json").write_text(json.dumps(jobs, indent=2), encoding="utf-8")
    (DATA / "auto_apply_queue.json").write_text(json.dumps({
        "generated_at": metadata["generated_at"],
        "action_required": "Review each posting, then run /apply <url> for jobs you approve.",
        "jobs": jobs,
    }, indent=2), encoding="utf-8")

    # CSV output
    csv_path = DATA / "all_jobs.csv"
    if jobs:
        keys = jobs[0].keys()
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(jobs)

def print_terminal_dashboard(jobs: list[dict[str, Any]]) -> None:
    if not jobs:
        print("\nNo jobs found to display.")
        return

    print("\n" + "="*110)
    print(f"{'JOB HUNT DASHBOARD':^110}")
    print("="*110)
    print(f"{'Date':<12} | {'Company':<25} | {'Role':<35} | {'Location':<15} | {'Fit':<8}")
    print("-" * 110)

    for job in jobs:
        date_str = job.get("posted_date", "N/A")
        company = (job.get("company") or "N/A")[:23]
        role = (job.get("title") or "N/A")[:33]
        loc = (job.get("location") or "N/A")[:13]
        fit = job.get("fit_signal", "N/A")
        print(f"{date_str:<12} | {company:<25} | {role:<35} | {loc:<15} | {fit:<8}")

    print("="*110)
    print(f"Total Jobs Staged: {len(jobs)}")
    print("Review the list above, then run: /apply <url>")
    print("="*110 + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the safe end-to-end fresh-job workflow.")
    parser.add_argument("--max-days", type=int, choices=range(1, 8), default=7, metavar="1..7")
    parser.add_argument("--no-search", action="store_true", help="Use only existing jobs_data/search_*.json files.")
    args = parser.parse_args()
    live = [] if args.no_search else search_live(args.max_days)
    jobs = normalize_jobs(live or read_cached(args.max_days))
    write_outputs(jobs, args.max_days)
    print_terminal_dashboard(jobs)
    print(f"Staged {len(jobs)} fresh entry-level jobs in jobs_data/auto_apply_queue.json.")
    print("No applications were submitted. Review the queue, then run /apply <url> for each approved job.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
