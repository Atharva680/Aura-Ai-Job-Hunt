---
name: resume-tailor
description: >
  Transforms the candidate's base resume into a highly targeted, ATS-optimized version for a specific job.
  Follows a strict 13-step workflow: DIAGNOSE → RESEARCH → GAP ANALYSIS → REWRITE → OPTIMIZE → ASSEMBLE → VALIDATE.
  Triggers on: tailor resume, optimize resume, customize CV, /tailor
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, WebFetch, WebSearch, Agent, AskUserQuestion
---

# ATS-Optimized Resume Engine

This skill implements the Master Prompt for resume tailoring. It ensures that every resume produced is truthful, targeted, and technically specific.

## Workflow

### Step 0: Collect Inputs
1. Read `cv/main_example.tex` (Current Resume).
2. Get the Target Job Title and Job Description (from the job listing URL or provided text).
3. Verify if additional achievements or metrics are needed.

### Step 1: ATS Diagnostic
Analyze the base resume for:
- **Parsing Risks**: Tables, columns, graphics, unusual fonts, date formatting.
- **Section Audit**: Identify what works and what is weak.
- **Recruiter Scan**: 5-10 second value proposition check.
- **Top 10 Fixes**: Ranked priority list of changes.

### Step 2: Job Market & Keyword Research
- Analyze the job description.
- Use `WebSearch` to find current market requirements for the role.
- Create a ranked list of **Core Keywords** (Required/Preferred/Supporting).
- Perform **Buzzword Cleanup** (replace generic phrases with strong action verbs).

### Step 3: Resume Gap Analysis
- Build a gap matrix comparing requirements vs. evidence.
- Identify **Top Strengths**, **Top Gaps**, and **Hidden Strengths**.

### Step 4: Experience & Project Rewrite
Rewrite bullets using: **Accomplished X, measured by Y, by doing Z**.
- **Strict Rule**: NEVER FABRICATE. If a metric is missing, ask the user.
- **Technical Specificity**: Technology + Implementation + Purpose + Outcome.
- **Target Vocabulary**: Use terms from the job description naturally.

### Step 5: Professional Summary
Create two versions:
- **Version A**: ATS-optimized (keyword rich).
- **Version B**: Recruiter-focused (value proposition).

### Step 6: Skills Optimization
Reorganize skills based on priority: Job Requirements > Actual Experience > Technical Relevance.

### Step 7: Project Optimization
Rank projects by relevance to the target role. Rewrite bullets to emphasize: **Problem → Solution → Architecture → Implementation → Result**.

### Step 8: Section Order
Determine the optimal order (e.g., Experience before Projects for professionals, vice versa for students).

### Step 9: ATS-Safe Format
Ensure single-column, no tables/graphics, conventional headings.

### Step 10: One-Page Optimization
Prioritize high-impact evidence to fit the target length without sacrificing readability.

### Step 11: LaTeX Assembly & File Generation
- Use `cv/main_example.tex` as the base template unless a different one is provided.
- **DO NOT redesign the template.**
- Replace placeholder content with optimized content.
- Escape all LaTeX special characters (`%`, `&`, `$`, etc.).
- **Storage Rule:** Every tailored resume must be stored in `C:\Users\athar\Desktop\ai-job-search-master\tailored_resumes\`.
- **Naming Convention:** Use `resume_<company>_<role>.tex` and `resume_<company>_<role>.json`.
- **JSON Format:** Along with the LaTeX file, save a JSON file containing the tailored content, ATS score, and target keywords for future reference.
- **Write the final files** to the specified directory.

### Step 12: Final ATS Validation
Score the resume (0-100) across:
- ATS compatibility, Keyword alignment, Recruiter readability, Technical relevance, Achievement orientation, Quantification, Role alignment.
- Perform a final fabrication check.

### Step 13: Final Output
Provide the results in the following order:
1. Resume Diagnosis
2. Target Job Analysis
3. Gap Analysis
4. Rewritten Resume Content (Section by Section)
5. Final ATS Score Table
6. Final Resume File: Confirm the file has been written to `tailored_resumes/` and provide the absolute path, followed by the raw LaTeX code for the user's records.

## Absolute Rules
- **No fabrication of metrics or experience.**
- **No keyword stuffing.**
- **Preserve the LaTeX template exactly.**
- **Mark uncertain info as `[VERIFY]`.**
