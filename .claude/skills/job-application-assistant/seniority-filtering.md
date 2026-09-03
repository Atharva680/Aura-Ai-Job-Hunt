# Job Relevance & Seniority Filter — MANDATORY RULES

This document defines the absolute criteria for filtering jobs for Atharva Vijay Shinde. These rules OVERRIDE any default AI behavior and must be applied before any job is ranked or recommended.

## 1. Candidate Seniority Baseline
**Classification: ENTRY-LEVEL / JUNIOR / EARLY-CAREER**
- **Total Practical Experience:** Approximately 11 months (including internships).
- **Rule:** Advanced technical skills (GenAI, RAG, PySpark, etc.) do NOT imply seniority.

## 2. The Seniority Hard-Filter
**Sequence:** SENIORITY ELIGIBILITY $\rightarrow$ ROLE RELEVANCE $\rightarrow$ EXPERIENCE FIT $\rightarrow$ SKILL FIT $\rightarrow$ KEYWORD FIT.
**Hard-Fail:** If a job is fundamentally a seniority mismatch, it is REJECTED regardless of technical keyword match.

## 3. Experience Range Hierarchy
| Tier | Range / Keywords | Classification | Action |
| :--- | :--- | :--- | :--- |
| **Tier A** | 0-2 yrs, Fresher, Graduate, Junior, Associate, Trainee, SE I | 🔥 HIGH PRIORITY | Highest relevance |
| **Tier B** | 1-3 yrs | ✅ GOOD FIT | Consider if flexible/accepts grads |
| **Tier C** | 2-4 yrs | 🟡 STRETCH | Low priority / Only if flexible |
| **Tier D** | 4+ yrs, Senior, Lead, Principal, Staff, Architect, Manager | ❌ REJECT | Do not recommend |

## 4. Detection Indicators
- **Positive:** Fresher, Entry Level, Graduate Program, Apprenticeship, 0-1 years.
- **Negative:** Mid-Senior, Senior, Lead, 5+ years, 10+ years.
- **LinkedIn Label:** "Mid-Senior level" + high experience = REJECT.

## 5. Relevance Scoring (Weighted)
1. **Seniority Fit (30%)** - MUST be compatible.
2. **Role/Responsibility Fit (25%)**
3. **Technical Skill Fit (20%)**
4. **Experience/Evidence Fit (15%)**
5. **Education/Eligibility Fit (5%)**
6. **Location/Work Mode Fit (5%)**

## 6. Classification Categories
- **🔥 HIGH PRIORITY:** Strong role + seniority + skill alignment.
- **✅ GOOD FIT:** Relevant role with minor gaps.
- **🟡 STRETCH:** Relevant role but meaningful experience gap.
- **⚪ LOW PRIORITY:** Some relevance but weak overall fit.
- **❌ REJECT:** Fundamental mismatch (Seniority, Experience, Education).

## 7. Mandatory Evaluation Table
Every shortlisted job must be presented in this format:

| Job Title | Company | Experience Required | Candidate Experience | Seniority | Skill Match | Classification | Reason |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

## 8. Application Threshold
- **HIGH PRIORITY / GOOD FIT** $\rightarrow$ Apply.
- **STRETCH** $\rightarrow$ Optional application.
- **LOW PRIORITY / REJECT** $\rightarrow$ Skip.

## 9. Final Fail-Safe Questions
1. Is this actually an entry-level/early-career opportunity?
2. Does the required experience match ~11 months?
3. Does the job contain "Mid-Senior/Senior/Lead" language?
4. Is there a hard eligibility mismatch? $\rightarrow$ If YES, **REJECT**.
