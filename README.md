<p align="center">
  <img src="assets/mascot/pip_flight_loop.gif" alt="AuraAI Mascot" width="200">
</p>

# AuraAI Job Hunt

*The intelligent job search framework powered by AI.*

An AI-powered job application framework built on [Claude Code](https://claude.com/claude-code). This framework transforms the job search process by using a structured agentic workflow to evaluate job postings, tailor CVs, write cover letters, and prepare for interviews.

> Note: This is an independent project and is not affiliated with, endorsed by, sponsored by, or maintained by Anthropic. Anthropic and Claude Code are referenced only to describe the toolchain this workflow uses.

## Overview

AuraAI Job Hunt turns Claude Code into a full-stack job application assistant. The core workflow (self-profiling, fit evaluation, and the drafter-reviewer application pipeline) is **language- and country-agnostic**. While it includes sample search skills for various portals, the pattern is designed to be adapted for any local job board.

```
/setup          /scrape              /apply <url>
  |                |                     |
  v                v                     v
Fill in        Search job           Evaluate fit
your profile   portals              Score & recommend
  |                |                     |
  v                v                     v
Profile        Present matches      Draft CV + Cover Letter
files ready    with fit ratings     (LaTeX, tailored)
                   |                     |
                   v                     v
               Pick a match         Reviewer agent critiques
               -> /apply            -> Revise -> Final output
```

The framework encodes career guidance best practices, including structured evaluation criteria, forward-looking cover letter framing, and optional salary benchmarking.

## Prerequisites

- [Claude Code](https://claude.com/claude-code) (CLI).
- Python 3.10+
- [Bun](https://bun.sh) (for job search CLI tools)
- LaTeX distribution with `lualatex` and `xelatex` (e.g., TeX Live, MacTeX, TinyTeX, or MiKTeX).
- Optional: `pip install pypdf` for ATS parseability checks.

## Quick start

### 1. Clone the repository

```bash
git clone https://github.com/Atharva680/auraaijobhunt.git
cd auraaijobhunt
```

### 2. Install job search tools

PowerShell:

```powershell
$tools = @("jobbank-search", "jobdanmark-search", "jobindex-search", "jobnet-search", "linkedin-search", "freehire-search")
foreach ($tool in $tools) {
  Push-Location ".agents/skills/$tool/cli"
  bun install
  Pop-Location
}
```

Bash / zsh / Git Bash:

```bash
for tool in jobbank-search jobdanmark-search jobindex-search jobnet-search linkedin-search freehire-search; do
  (cd .agents/skills/$tool/cli && bun install)
done
```

### 3. Set up your profile

```bash
claude
# Then inside Claude Code:
/setup
```

### 4. Search for jobs

```bash
/scrape
```

### 5. Apply to a job

```bash
/apply https://example.com/job/123
```

## Other commands

- **`/interview`**: Preps you for a scheduled interview with a stage-specific prep pack and mock interviews.
- **`/outcome`**: Records application results and archives submitted materials.
- **`/notion-sync`**: Syncs the pipeline into a Notion database.
- **`/gmail-sync`**: Auto-detects application status from Gmail.
- **`/rank`**: Batch-scores scraped postings against the fit framework.
- **`/expand`**: Enriches your profile from public sources (GitHub, portfolio, etc.).
- **`/upskill`**: Analyzes skill gaps and produces a prioritized learning plan.
- **`/html-report`**: Generates a self-contained HTML dashboard.
- **`/add-template`**: Registers custom CV or cover letter templates.
- **`/add-portal`**: Generates a job-portal search skill for your market.
- **`/reset`**: Wipes profile data or documents to start fresh.

## File structure

```
auraaijobhunt/
├── CLAUDE.md                          # Main candidate profile + workflow rules
├── .claude/
│   ├── commands/                      # Workflow definitions (/apply, /setup, etc.)
│   ├── skills/                        # Core application skills
│   └── settings.json                  # Claude Code permissions
├── .agents/skills/                    # Job portal CLI tools
├── cv/                                # CV templates and sources
├── cover_letters/                    # Cover letter templates and fonts
├── templates/                         # Custom registered templates
├── documents/                         # Career source materials
├── tools/                             # Utility scripts (salary, linting, etc.)
├── job_scraper/                       # Scraper state
└── job_search_tracker.csv             # Application tracking spreadsheet
```

## How `/apply` works

The `/apply` command runs a **drafter-reviewer workflow**:

1. **Parse** the job posting.
2. **Evaluate fit** against your profile.
3. **Draft** tailored CV and cover letter in LaTeX.
4. **Review**: A second agent researches the company and critiques the drafts.
5. **Revise**: Drafter updates materials based on feedback.
6. **Compile & Inspect**: PDFs are rendered and visually inspected for layout perfection.
7. **ATS-check**: Verifies the PDF text layer for parser compatibility.
8. **Present**: Final output with a verification checklist.

## Customization

You can manually edit `CLAUDE.md`, `01-candidate-profile.md`, `02-behavioral-profile.md`, and `04-job-evaluation.md` to refine your profile and fit criteria.

## License

MIT
