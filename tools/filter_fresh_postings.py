#!/usr/bin/env python3
"""Keep only verifiably fresh job records from a portal JSON response.

The input and output use the portal CLI envelope: {"results": [...]}.  Records
whose `date` / `posted_date` is absent, malformed, older than the requested
window, or expressed as a known stale relative label are rejected.  This is
deliberately fail-closed: a deadline and `first_seen` are not posting dates.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime, timedelta, timezone
from typing import Any

STALE_LABEL = re.compile(r"\b(last\s+month|30\+?\s*days?\s+ago|\d+\+\s*days?\s+ago)\b", re.I)
RELATIVE_DAYS = re.compile(r"^(?:posted\s+)?(\d+)\s+days?\s+ago$", re.I)
RELATIVE_HOURS = re.compile(r"^(?:posted\s+)?(\d+)\s+hours?\s+ago$", re.I)
RELATIVE_MINUTES = re.compile(r"^(?:posted\s+)?(\d+)\s+minutes?\s+ago$", re.I)


def parse_posted(value: Any, today: date) -> date | None:
    if not isinstance(value, str) or not value.strip():
        return None
    raw = value.strip()
    if STALE_LABEL.search(raw):
        return None
    for pattern, unit in ((RELATIVE_DAYS, "days"), (RELATIVE_HOURS, "hours"), (RELATIVE_MINUTES, "minutes")):
        match = pattern.match(raw)
        if match:
            amount = int(match.group(1))
            return today - timedelta(days=amount if unit == "days" else 0)
    normalized = raw.replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(normalized).date()
    except ValueError:
        try:
            return date.fromisoformat(raw)
        except ValueError:
            return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Filter portal results to verifiable recent postings.")
    parser.add_argument("--max-days", type=int, default=7, choices=range(1, 8), metavar="1..7")
    args = parser.parse_args()
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError as error:
        print(f"Invalid JSON input: {error}", file=sys.stderr)
        return 2
    if not isinstance(payload, dict) or not isinstance(payload.get("results"), list):
        print('Expected a JSON object containing a "results" array.', file=sys.stderr)
        return 2

    today = datetime.now(timezone.utc).date()
    cutoff = today - timedelta(days=args.max_days)
    kept, rejected = [], []
    for record in payload["results"]:
        if not isinstance(record, dict):
            rejected.append({"reason": "record is not an object"})
            continue
        posted = parse_posted(record.get("posted_date", record.get("date")), today)
        if posted is None or posted < cutoff or posted > today:
            rejected.append({"title": record.get("title"), "reason": "missing, malformed, future, or stale posting date"})
            continue
        normalized = dict(record)
        normalized["posted_date"] = posted.isoformat()
        kept.append(normalized)
    payload["results"] = kept
    payload["meta"] = {**(payload.get("meta") or {}), "count": len(kept), "freshness_max_days": args.max_days, "rejected_count": len(rejected)}
    print(json.dumps(payload, indent=2))
    if rejected:
        print(json.dumps({"freshness_rejections": rejected}, indent=2), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
