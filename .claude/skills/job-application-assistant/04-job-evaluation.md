# Job Evaluation Framework: Atharva Vijay Shinde

This framework implements the **MANDATORY SENIORITY FILTER**. Every job must be evaluated against the criteria in `.claude/skills/job-application-assistant/seniority-filtering.md` BEFORE any other scoring.

## 1. The Seniority Hard-Gate (Pre-Score)
Before calculating a score, determine the Seniority Classification. If the result is **❌ REJECT**, stop immediately.

| Category | Criteria | Result |
| :--- | :--- | :--- |
| **🔥 HIGH PRIORITY** | 0-2 yrs, Fresher, Graduate, Junior, Associate, Trainee | PROCEED |
| **✅ GOOD FIT** | 1-3 yrs (if flexible or accepts grads) | PROCEED |
| **🟡 STRETCH** | 2-4 yrs (low priority unless flexible) | PROCEED (Note as Stretch) |
| **❌ REJECT** | 4+ yrs, Senior, Lead, Principal, Staff, Architect, Manager, Mid-Senior level | **HARD STOP** |

## 2. Weighted Relevance Score
If the job passes the Seniority Hard-Gate, calculate the final score (0-100):

| Dimension | Weight | Evaluation Criteria |
| :--- | :--- | :--- |
| **Seniority Fit** | 30% | Compatibility with entry-level/early-career (~11 months exp). |
| **Role/Responsibility Fit** | 25% | Alignment with target roles (AI/ML/Data/Python Engineer). |
| **Technical Skill Fit** | 20% | Match with Core/Preferred/Supporting skills. |
| **Experience/Evidence Fit** | 15% | Ability to prove skills via InfoCepts internship and projects. |
| **Education/Eligibility Fit** | 5% | B.E. CS status, graduation date, and degree requirements. |
| **Location/Work Mode Fit** | 5% | Bangalore, Hyderabad, Pune, Mumbai, Nagpur, or Remote. |

## 3. Skill Match Tiers
- **Strong match:** RAG Pipelines, LangChain, OpenAI API, Prompt Engineering, AI Agents, Vector DBs, Databricks, Apache Spark, Delta Lake, ETL/ELT, Python, FastAPI, MLOps, Docker, Azure, MLflow, PostgreSQL.
- **Moderate match:** TensorFlow, PyTorch, OpenCV, NLP, Reinforcement Learning, Node.js, React.
- **Weak/gap:** Kubernetes at scale, non-Azure clouds (AWS/GCP).

## 4. Location & Language Gates
- **Location:** PASS: Bangalore, Hyderabad, Pune, Mumbai, Nagpur, remote. FLAG: other Indian metros. FAIL: others.
- **Language:** Compare against `01-candidate-profile.md`. Hard FAIL if a required language is missing.

## 5. Final Classification & Action
| Score | Classification | Action |
| :--- | :--- | :--- |
| 75+ | 🔥 HIGH PRIORITY | Apply immediately, full tailor. |
| 60–74 | ✅ GOOD FIT | Apply, address minor gaps. |
| 45–59 | 🟡 STRETCH | Optional application, high-effort tailor. |
| <45 | ⚪ LOW PRIORITY / REJECT | Skip. |

## 6. Mandatory Output Format
Every evaluation must conclude with the **Seniority Summary Table**:

| Job Title | Company | Experience Required | Candidate Experience | Seniority | Skill Match | Classification | Reason |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

## 7. Role-Specific Evidence
- **AI/GenAI/Data:** Lead with InfoCepts RAG delivery (100K+ docs, 95% accuracy), agent automation (260+ hrs/year), and Databricks Associate certifications.
- **Junior Python/Software:** Lead with Python, FastAPI, Docker, Azure microservices, and AI-agent automation.
- **Computer Vision:** Use OpenCV, YuNet, TensorFlow attendance system (98% accuracy).
- **ML/RL:** Use LSTM + Deep Q-Learning energy optimizer.
