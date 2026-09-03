<p align="center">
  <img
    src="https://atlasiko.com/assets/images/articles/gifs/stormtrooper-vacuuming-on-the-beach.gif"
    alt="AuraAI Job Hunt"
    width="300"
  >
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-4a4d6a5e9e4f.gif" width="100%">
</p>

<h1 align="center">🚀 AuraAI Job Hunt</h1>

<p align="center">
  <strong>AI-Powered Job Search → Filtering → Scoring → Resume Tailoring</strong>
</p>

<p align="center">
  Stop scrolling through hundreds of irrelevant jobs.
  <br>
  Let AI find, filter, rank, research, and prepare the best opportunities for you.
</p>

<p align="center">
  <a href="https://github.com/Atharva680/Aura-Ai-Job-Hunt">
    <img src="https://img.shields.io/github/stars/Atharva680/Aura-Ai-Job-Hunt?style=for-the-badge&logo=github" alt="GitHub Stars">
  </a>
  <a href="https://github.com/Atharva680/Aura-Ai-Job-Hunt/network/members">
    <img src="https://img.shields.io/github/forks/Atharva680/Aura-Ai-Job-Hunt?style=for-the-badge&logo=github" alt="GitHub Forks">
  </a>
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Bun-Runtime-black?style=for-the-badge&logo=bun" alt="Bun">
  <img src="https://img.shields.io/badge/LaTeX-Resume%20Engine-008080?style=for-the-badge&logo=latex" alt="LaTeX">
  <img src="https://img.shields.io/badge/Claude-AI%20Assisted-CC785C?style=for-the-badge" alt="Claude">
</p>

<p align="center">
  <a href="https://github.com/Atharva680/Aura-Ai-Job-Hunt">GitHub</a>
  •
  <a href="https://atharva-portfolio-beta-nine.vercel.app">Portfolio</a>
</p>

---

# 🎥 AuraAI in Action

<p align="center">
  <a href="./assets/demo/AuraAI_Job_Hunt_demo.mp4">
    <strong>▶️ WATCH THE AURA AI DEMO VIDEO</strong>
  </a>
</p>

> Click the button above to open the demo video stored directly inside the repository.

### ⚡ Core Workflow

```text
Job Sources
     ↓
Collect Listings
     ↓
Freshness Filter
     ↓
Seniority Filter
     ↓
Relevance Scoring
     ↓
Job Dashboard
     ↓
Top Job Selection
     ↓
Resume Tailoring
     ↓
Cover Letter
     ↓
Company Research
     ↓
Application Ready
````

---

# 🧠 What Is AuraAI?

**AuraAI Job Hunt** is an AI-assisted job discovery and application preparation framework designed to reduce the manual work involved in searching for relevant jobs.

Instead of simply scraping job boards, AuraAI creates a complete pipeline:

```text
Discover
   ↓
Collect
   ↓
Clean
   ↓
Filter
   ↓
Score
   ↓
Research
   ↓
Tailor
   ↓
Apply
```

The goal is simple:

> **Find fewer jobs — but make them much more relevant.**

---

# 🎯 The Problem

Traditional job searching creates several problems.

### ❌ Too Many Listings

A single search can return hundreds of jobs.

### ❌ Irrelevant Roles

Search engines frequently return:

* Senior roles
* Manager positions
* Unrelated engineering roles
* Different technology stacks
* Jobs requiring significantly more experience

### ❌ Manual Resume Editing

Every application may require:

* Keyword adjustments
* Skill prioritization
* Project selection
* Resume restructuring
* Cover-letter generation

### ❌ Company Research

Before applying, candidates often need to manually investigate:

* Company
* Technology
* Industry
* Role
* Salary
* Location
* Work model
* Hiring requirements

AuraAI attempts to bring these steps into one workflow.

---

# 💡 AuraAI Approach

AuraAI uses an **inverse funnel**.

Instead of:

```text
1000 Jobs
   ↓
500 Jobs
   ↓
200 Jobs
   ↓
50 Jobs
   ↓
Apply
```

AuraAI aims for:

```text
Many Job Listings
       ↓
Freshness Filter
       ↓
Seniority Filter
       ↓
Role Relevance
       ↓
Skill Match
       ↓
Location / Work Model
       ↓
Quality Score
       ↓
Top Opportunities
       ↓
Tailored Application
```

The result is a smaller, higher-quality job pool.

---

# ✨ Features

| Feature                | Description                                           |
| ---------------------- | ----------------------------------------------------- |
| 🔎 Job Discovery       | Collect job opportunities from configured sources     |
| 🧹 Data Cleaning       | Normalize and clean scraped listings                  |
| ⏱️ Freshness Filtering | Prioritize recently posted opportunities              |
| 🎓 Seniority Filtering | Remove roles outside the candidate's experience level |
| 🎯 Relevance Scoring   | Score jobs based on role and skill alignment          |
| 📊 Job Dashboard       | Organize and review shortlisted opportunities         |
| 🤖 AI Resume Tailoring | Adapt resume content to a target role                 |
| ✍️ Cover Letters       | Generate role-specific cover letters                  |
| 🏢 Company Research    | Research companies before applying                    |
| 💰 Salary Intelligence | Compare salary and market information                 |
| 🧪 QA                  | Validate generated resumes and outputs                |
| 📄 LaTeX Resume        | Maintain ATS-friendly resume source                   |
| 🔐 Privacy             | Keep personal configuration local                     |
| 🛠️ Developer Workflow | Structured repository for continuous improvement      |

---

# 🔎 Job Collection

AuraAI can collect job listings and normalize them into a consistent structure.

A typical listing can contain:

```text
Job Title
Company
Location
Work Model
Experience
Skills
Description
Posted Date
Salary
Source
Job URL
```

This allows downstream components to work with a predictable dataset.

---

# ⏱️ Freshness Filter

Job freshness matters.

AuraAI can prioritize listings according to their posting age.

Example:

```text
Posted Today       → High Priority
Posted 1–3 Days    → High Priority
Posted 4–7 Days    → Medium Priority
Posted 8–14 Days   → Lower Priority
Older Listings     → Review / Exclude
```

This prevents the application pipeline from spending most of its effort on stale opportunities.

---

# 🎓 Seniority Wall

One of the most important components is **experience-level filtering**.

A search for:

```text
AI Engineer
```

may return:

```text
AI Engineer — Fresher
AI Engineer — 1–2 Years
AI Engineer — 3–5 Years
Senior AI Engineer — 5–8 Years
Lead AI Engineer — 8+ Years
Principal AI Engineer — 10+ Years
```

AuraAI attempts to distinguish between these levels.

### Target

```text
Junior
Entry Level
Fresher
Associate
Early Career
```

### Potentially Excluded

```text
Senior
Lead
Staff
Principal
Manager
Director
Architect
```

The objective is not to reject jobs blindly, but to prevent obviously mismatched opportunities from dominating the results.

---

# 🎯 Relevance Scoring

AuraAI evaluates jobs using multiple signals.

Conceptually:

```text
Relevance Score =
    Role Match
  + Skill Match
  + Experience Match
  + Location Match
  + Freshness
  + Work Model
  + Technology Match
```

Example:

```text
Job: AI Engineer

Role Match           ██████████  100%
Skills Match         █████████   90%
Experience Match     ██████████  100%
Location Match       ████████    80%
Freshness             █████████   90%

Overall Score: 92%
```

The exact scoring logic can be configured according to the candidate profile.

---

# 📊 Job Dashboard

The dashboard is designed to answer one question:

> **Which jobs should I apply to first?**

Example:

| Score | Role               | Experience | Location  | Status    |
| ----: | ------------------ | ---------- | --------- | --------- |
|    94 | AI Engineer        | 0–2 yrs    | Hybrid    | 🔥 Apply  |
|    91 | ML Engineer        | 0–2 yrs    | Remote    | 🔥 Apply  |
|    87 | Python AI Engineer | 1–2 yrs    | Pune      | ✅ Review  |
|    72 | Data Engineer      | 2–4 yrs    | Bengaluru | ⚠️ Review |
|    42 | Senior AI Engineer | 5+ yrs     | Mumbai    | ❌ Skip    |

---

# 🧠 AI Intelligence Layer

AuraAI can use AI-assisted workflows for:

```text
Job Understanding
       ↓
Requirement Extraction
       ↓
Candidate Matching
       ↓
Skill Gap Identification
       ↓
Resume Tailoring
       ↓
Cover Letter Generation
       ↓
Company Research
```

AI is used as an assistance layer rather than blindly generating everything.

---

# 📄 AI Resume Tailoring

A major feature of AuraAI is role-specific resume preparation.

Instead of using one generic resume:

```text
MASTER RESUME
      ↓
Target Job
      ↓
Analyze Job Description
      ↓
Extract Important Skills
      ↓
Identify Relevant Experience
      ↓
Prioritize Matching Projects
      ↓
Generate Tailored Resume
```

The goal is to maintain the candidate's actual experience while emphasizing the most relevant information.

---

# 🎯 Resume Tailoring Philosophy

AuraAI follows an important principle:

> **Tailor the presentation — never fabricate the experience.**

The system should not invent:

* Employment
* Projects
* Certifications
* Technologies
* Achievements
* Job responsibilities

Instead, it should prioritize existing evidence that is relevant to the target position.

---

# ✍️ Cover Letters

AuraAI can generate role-specific cover letters using information from:

```text
Candidate Profile
       +
Job Description
       +
Company Information
       +
Relevant Projects
       ↓
Personalized Cover Letter
```

The objective is to avoid generic:

> "I am writing to express my interest..."

style applications.

---

# 🏢 Company Research

Before applying, AuraAI can organize company intelligence.

Example:

```text
Company
├── Industry
├── Products
├── Technology
├── Location
├── Company Size
├── Role
├── Hiring Information
├── Salary Information
└── Application URL
```

This helps candidates understand the opportunity before submitting an application.

---

# 💰 Salary & Market Intelligence

The repository also contains salary-related tooling.

Example workflow:

```text
Job Title
    ↓
Experience Level
    ↓
Location
    ↓
Market Data
    ↓
Salary Range
```

This can help candidates understand whether a role is aligned with their expectations and market conditions.

---

# 🧪 Quality Assurance

Generated outputs should not automatically be considered final.

AuraAI includes quality checks around:

* Resume formatting
* Required sections
* LaTeX compilation
* Job relevance
* Experience alignment
* Generated content
* File structure
* Output consistency

Example:

```text
Generate Resume
      ↓
Compile
      ↓
Validate
      ↓
Review
      ↓
Application Ready
```

---

# 🏗️ Architecture

```text
                   ┌───────────────────┐
                   │    Job Sources    │
                   └─────────┬─────────┘
                             │
                             ▼
                   ┌───────────────────┐
                   │  Job Scraper /    │
                   │    Collector      │
                   └─────────┬─────────┘
                             │
                             ▼
                   ┌───────────────────┐
                   │ Data Cleaning &   │
                   │  Normalization    │
                   └─────────┬─────────┘
                             │
                             ▼
              ┌────────────────────────────┐
              │     Relevance Pipeline     │
              ├────────────────────────────┤
              │ Freshness                  │
              │ Seniority                  │
              │ Role Match                 │
              │ Skill Match                │
              │ Location                   │
              │ Experience                 │
              └──────────────┬─────────────┘
                             │
                             ▼
                   ┌───────────────────┐
                   │   Job Dashboard   │
                   └─────────┬─────────┘
                             │
                 ┌───────────┼───────────┐
                 ▼           ▼           ▼
             Resume      Cover Letter   Research
             Tailoring                   │
                 │           │           │
                 └───────────┼───────────┘
                             ▼
                   ┌───────────────────┐
                   │ Application Ready │
                   └───────────────────┘
```

---

# 🧩 Engineering Components

The repository is organized into separate areas for different parts of the workflow.

```text
AuraAI Job Hunt
│
├── job_scraper/
│   └── Job collection & processing
│
├── cv/
│   └── Resume / CV source files
│
├── cover_letters/
│   └── Cover letter outputs
│
├── company_research/
│   └── Company intelligence
│
├── documents/
│   └── Supporting documents
│
├── templates/
│   └── Reusable templates
│
├── tools/
│   └── Utility scripts
│
├── upskill/
│   └── Skill development resources
│
├── tests/
│   └── Automated tests
│
├── assets/
│   └── Images & demo assets
│
├── aggregate_jobs.py
├── salary_lookup.py
├── salary_config.json
├── profile_config.json
├── README.md
├── SETUP.md
├── CONTRIBUTING.md
└── SECURITY.md
```

---

# 📁 Project Structure

```text
ai-job-search-master/
│
├── .agents/
├── .claude/
├── .github/
│
├── assets/
│   ├── mascot/
│   └── demo/
│       └── AuraAI_Job_Hunt_demo.mp4
│
├── company_research/
├── cover_letters/
├── cv/
├── documents/
├── job_scraper/
├── templates/
├── tests/
├── tools/
├── upskill/
│
├── aggregate_jobs.py
├── salary_lookup.py
├── salary_config.json
├── profile_config.json
│
├── AGENTS.md
├── CLAUDE.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── SECURITY.md
└── SETUP.md
```

---

# ⚙️ Quick Start

## 1. Clone the Repository

```bash
git clone https://github.com/Atharva680/Aura-Ai-Job-Hunt.git
```

```bash
cd Aura-Ai-Job-Hunt
```

---

## 2. Create a Virtual Environment

### Windows

```powershell
python -m venv .venv
```

```powershell
.\.venv\Scripts\Activate.ps1
```

### macOS / Linux

```bash
python3 -m venv .venv
```

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

If a requirements file is present:

```bash
pip install -r requirements.txt
```

Otherwise, install the dependencies required by the specific module you want to run.

---

# 🔐 Configuration

AuraAI keeps candidate-specific configuration separate from the core pipeline.

Typical configuration can include:

```text
Target Roles
Experience
Preferred Locations
Skills
Technologies
Salary Expectations
Work Model
Education
Projects
```

Example conceptual configuration:

```json
{
  "target_roles": [
    "AI Engineer",
    "Machine Learning Engineer",
    "Python Developer"
  ],
  "experience_level": "entry-level",
  "work_models": [
    "Remote",
    "Hybrid",
    "On-site"
  ]
}
```

> Keep personal information and API keys out of Git.

---

# 🎯 Relevance Rules

A job should ideally satisfy several conditions before reaching the final application queue.

```text
                    JOB
                     │
                     ▼
              Is it fresh?
                     │
              ┌──────┴──────┐
             NO             YES
             │               │
            SKIP             ▼
                    Experience Match?
                           │
                    ┌──────┴──────┐
                   NO             YES
                   │               │
                  SKIP             ▼
                          Role Relevant?
                               │
                        ┌──────┴──────┐
                       NO             YES
                       │               │
                      SKIP             ▼
                             Skill Match
                                  │
                                  ▼
                            Score & Rank
```

---

# 🎓 Seniority Filtering Philosophy

Job titles alone are not always enough.

For example:

```text
AI Engineer
```

could represent:

```text
Entry Level
Mid Level
Senior
```

Therefore, AuraAI should consider:

* Job title
* Required years of experience
* Seniority language
* Responsibilities
* Required technical depth
* Leadership requirements
* Management responsibilities

Examples of seniority signals:

```text
Senior
Lead
Staff
Principal
Architect
Manager
Director
Head
```

These signals can be used to reduce false-positive job matches.

---

# 🧮 Example Scoring Model

An illustrative scoring model could look like:

```text
Role Relevance       30%
Skill Match          25%
Experience Match     20%
Freshness            10%
Location             10%
Work Model            5%
--------------------------------
Total                100%
```

Example:

```text
Role Match       = 28 / 30
Skill Match      = 22 / 25
Experience       = 20 / 20
Freshness        =  9 / 10
Location         =  8 / 10
Work Model       =  5 /  5

Total            = 92 / 100
```

The weights can be adjusted according to the candidate's priorities.

---

# 🧑‍💻 Example Application Flow

Imagine AuraAI discovers:

```text
500 job listings
```

After filtering:

```text
500
 ↓
350 Fresh
 ↓
180 Experience Compatible
 ↓
95 Role Relevant
 ↓
45 Strong Skill Match
 ↓
20 High-Quality Opportunities
 ↓
10 Priority Applications
```

Instead of manually processing 500 jobs, the candidate can focus on the strongest opportunities.

> Numbers above are illustrative and represent the intended workflow rather than guaranteed output.

---

# 🤖 AI-Assisted Development

This repository is also designed around AI-assisted engineering workflows.

AI can assist with:

```text
Code Generation
Documentation
Resume Tailoring
Job Analysis
Company Research
Cover Letters
Testing
Debugging
Workflow Automation
```

However, human review remains important.

---

# 🔒 Privacy & Security

Personal job-search information can be sensitive.

Recommended practices:

### Never commit:

```text
API Keys
Passwords
Access Tokens
Private Credentials
Personal Documents
Private Resume Versions
Sensitive Personal Data
```

Use environment variables where applicable.

Example:

```powershell
$env:API_KEY="your-key"
```

And ensure secrets are excluded through `.gitignore`.

---

# ⚠️ Responsible Use

AuraAI is designed as an **application assistance system**, not an automatic mass-application bot.

Users should:

* Review job descriptions
* Verify requirements
* Review AI-generated resumes
* Check generated cover letters
* Confirm salary information
* Verify company information
* Submit applications themselves where appropriate

AI-generated content should be treated as a draft that requires human verification.

---

# 🧪 Testing

Run the available tests using the project's configured test tooling.

For example:

```bash
pytest
```

Specific tests can also be executed:

```bash
pytest tests/
```

---

# 🛠️ Development Workflow

A typical development cycle:

```text
Create Feature
     ↓
Implement
     ↓
Run Tests
     ↓
Review Output
     ↓
Update Documentation
     ↓
Commit
     ↓
Push
```

Recommended Git workflow:

```bash
git status
```

```bash
git add .
```

```bash
git commit -m "feat: describe change"
```

```bash
git push origin main
```

---

# 📈 Roadmap

Potential future improvements include:

* [ ] More job-source integrations
* [ ] Improved duplicate detection
* [ ] Better seniority classification
* [ ] Advanced semantic job matching
* [ ] Resume-to-JD similarity analysis
* [ ] Skill-gap analysis
* [ ] Application tracking
* [ ] Job-status tracking
* [ ] Automated company research
* [ ] Salary trend analysis
* [ ] Browser dashboard
* [ ] Notifications
* [ ] Better ranking algorithms
* [ ] Application analytics
* [ ] Personalized learning recommendations

---

# 🌟 Why AuraAI?

Most job-search tools focus on **finding jobs**.

AuraAI focuses on the complete journey:

```text
Find
 ↓
Filter
 ↓
Understand
 ↓
Rank
 ↓
Research
 ↓
Tailor
 ↓
Prepare
 ↓
Apply
```

The objective is to transform job hunting from a repetitive search task into an intelligent workflow.

---

# 🚀 What Makes AuraAI Different?

### Traditional Job Search

```text
Search
 ↓
Scroll
 ↓
Open
 ↓
Read
 ↓
Reject
 ↓
Repeat
```

### AuraAI

```text
Search
 ↓
Collect
 ↓
Filter
 ↓
Score
 ↓
Rank
 ↓
Research
 ↓
Tailor
 ↓
Apply
```

The difference is **decision support**.

---

# 🧠 Core Idea

> **Don't apply to more jobs. Apply to better jobs.**

AuraAI is built around this principle.

A smaller list of highly relevant opportunities can be more useful than a massive list of loosely related jobs.

---

# 🎥 Demo Workflow

The included demo demonstrates the overall concept:

```text
1. Job discovery
       ↓
2. Job collection
       ↓
3. Filtering
       ↓
4. Relevance scoring
       ↓
5. Job selection
       ↓
6. Resume preparation
       ↓
7. Application preparation
```

Demo file:

```text
assets/demo/AuraAI_Job_Hunt_demo.mp4
```

---

# 📊 Example Candidate Workflow

```text
                    ┌───────────────┐
                    │ Candidate     │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ Master Resume │
                    └───────┬───────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ AuraAI Engine │
                    └───────┬───────┘
                            │
            ┌───────────────┼────────────────┐
            │               │                │
            ▼               ▼                ▼
       Job Search      Company Research   Salary
            │
            ▼
       Job Filtering
            │
            ▼
       Relevance Score
            │
            ▼
       Best Opportunities
            │
            ▼
       Resume Tailoring
            │
            ▼
       Cover Letter
            │
            ▼
       Application
```

---

# 🏆 Built For

AuraAI is especially useful for candidates who want to:

* Reduce repetitive job searching
* Find entry-level opportunities
* Focus on relevant roles
* Improve application quality
* Maintain multiple resume variants
* Research companies faster
* Organize job opportunities
* Understand skill requirements
* Build a systematic job-search process

---

# 🔗 Project Links

### GitHub Repository

[https://github.com/Atharva680/Aura-Ai-Job-Hunt](https://github.com/Atharva680/Aura-Ai-Job-Hunt)

### Portfolio

[https://atharva-portfolio-beta-nine.vercel.app](https://atharva-portfolio-beta-nine.vercel.app)

---

# 🤝 Contributing

Contributions are welcome.

A typical contribution workflow:

```bash
git clone https://github.com/Atharva680/Aura-Ai-Job-Hunt.git
```

Create a branch:

```bash
git checkout -b feature/your-feature
```

Make your changes and test them:

```bash
pytest
```

Commit:

```bash
git add .
git commit -m "feat: add your feature"
```

Push:

```bash
git push origin feature/your-feature
```

Then open a Pull Request.

---

# 🐛 Issues & Suggestions

If you discover a bug or have an idea for improving AuraAI:

1. Check existing issues.
2. Create a new issue if necessary.
3. Explain the problem clearly.
4. Include reproduction steps where possible.
5. Include relevant logs or screenshots.
6. Suggest a potential solution if you have one.

---

# 📜 License

See the repository's `LICENSE` file for the applicable license.

---

# ⭐ Support the Project

If you find AuraAI useful:

⭐ Star the repository

🍴 Fork the project

🐛 Report issues

💡 Suggest improvements

🤝 Contribute

Every contribution helps improve the project.

---

# 👨‍💻 Author

## Atharva Vijay Shinde

AI / ML • Python • Automation • Data Engineering • Generative AI

<p align="center">
  <a href="https://github.com/Atharva680">
    GitHub
  </a>
  •
  <a href="https://atharva-portfolio-beta-nine.vercel.app">
    Portfolio
  </a>
</p>

---

# 📊 Project Philosophy

```text
                 ┌─────────────────────┐
                 │   Too Many Jobs     │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │    AuraAI Engine    │
                 └──────────┬──────────┘
                            │
           ┌────────────────┼────────────────┐
           │                │                │
           ▼                ▼                ▼
       FILTER             SCORE           RESEARCH
           │                │                │
           └────────────────┼────────────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Best Opportunities  │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Tailored Resume     │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Application Ready   │
                 └─────────────────────┘
```

---

<p align="center">

### 🚀 Search Less. Filter Smarter. Apply Better.

<strong>AuraAI Job Hunt</strong>

</p>

<p align="center">
  Built with ❤️, Python, AI, automation, and a lot of iteration.
</p>

---

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=Atharva680&label=Repository%20Views&color=blue&style=flat-square" alt="Repository Views">
</p>
```

### Important

Keep the demo video exactly here in your repository:

```text
assets/
└── demo/
    └── AuraAI_Job_Hunt_demo.mp4
```

And the README reference should remain:

```markdown
<a href="./assets/demo/AuraAI_Job_Hunt_demo.mp4">
  <strong>▶️ WATCH THE AURA AI DEMO VIDEO</strong>
</a>
```

That way, the README works correctly on GitHub without exposing your local Windows path.
