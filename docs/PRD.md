# 🚢 FreightSense — AI Freight Advisor  
**Product Requirements Document (PRD)**  
*Concept, Design & Development by **Pratik Nirupam Das***  
> *Navigate Trade with Intelligence.*

---

## 🧭 1. Product Overview

FreightSense is a **digital freight advisor powered by AI** that helps freight forwarders, brokers, and shippers make smarter decisions — faster.  
It understands natural language, predicts freight rates and delivery times, recommends routes, and ranks sales leads — all through a simple conversational interface.

---

## 💡 2. The Problem

Freight professionals spend hours quoting, comparing carriers, tracking shipments, and following up on leads using scattered spreadsheets and emails.  
Data is siloed, decisions are slow, and teams react to problems instead of predicting them.

---

## 🚀 3. The Solution

FreightSense uses **AI + analytics + integrations** to create one unified workspace that:
- Answers freight questions instantly (like ChatGPT for logistics).  
- Predicts rates, ETAs, and lead conversion chances.  
- Automates quoting and document lookup.  
- Connects with CRMs, visibility systems, and rate databases.  

---

## 🎯 4. Vision & Goals

> “To become the operating brain for global freight — where every decision is assisted by intelligence.”

**Core Goals**
- Reduce quote turnaround from hours → under 1 minute.  
- Improve ETA accuracy and win ratio.  
- Automate repetitive logistics workflows.  
- Offer full transparency into every AI decision.

---

## 👥 5. User Personas

| User | Role | Main Needs | FreightSense Value |
|------|------|-------------|---------------------|
| **Freight Forwarder** | Pricing & operations | Quick, error-free quotes | Predictive rates + margin guardrails |
| **Sales Executive** | Client management | Which leads to pursue first | Lead scoring & smart follow-ups |
| **Shipment Coordinator** | Tracking & updates | Reliable ETAs, proactive alerts | Predictive ETA & risk alerts |
| **Logistics Manager** | Strategy & reporting | Visibility & efficiency | Analytics & automation dashboard |

---

## ⚙️ 6. Product Scope

### In-Scope (MVP + V1)
- Chat-based AI assistant  
- Quote prediction, route optimization, ETA forecasting  
- Lead scoring + CRM integration  
- RAG-based knowledge retrieval  
- Feedback + retraining pipeline  

### Out-of-Scope
- Payments, invoicing, or customs filings (future phase)  
- End-customer booking portal  

---

## 🧩 7. Detailed Feature Descriptions

Each feature below explains the **user input**, **context data**, **AI behavior**, **feedback loop**, and **evaluation methods**.

---

### 💬 7.1 Conversational Assistant

**Goal:** Let users interact naturally and perform logistics tasks without menus or training.

- **User Input:**  
  “Compare rates for a 40FT from Dubai to Hamburg next week.”  
  or “Track container ABCD123456.”

- **Contextual Data:**  
  - User profile (role, permissions)  
  - Recent chats (context memory)  
  - Lane data (origin, destination, date)  
  - Company policies (margin limits, preferred carriers)

- **LLM Output:**  
  Responds with an actionable summary:  
  *“Top 3 carriers with rates, ETAs, and CO₂ impact. Maersk is optimal for cost-time balance.”*

- **Feedback Mechanism:**  
  👍 / 👎 on responses; selections logged for learning.  
  Frequent queries → auto-shortcuts (chips).

- **Quality Evaluation:**  
  - Intent detection accuracy ≥ 95%  
  - Avg. response latency < 3 s  
  - ≥ 80% tasks resolved in one message  

---

### 💸 7.2 Smart Quote Engine

**Goal:** Automatically calculate and recommend optimal freight rates.

- **User Input:**  
  `/quote origin=Dubai dest=Hamburg equipment=40FT date=next week`

- **Contextual Data:**  
  - Historical rates  
  - Carrier rate APIs (Freightos, DP World Flow)  
  - Fuel index, seasonality, congestion data  
  - Company margin rules & currency

- **LLM Output:**  
  *“Predicted base rate: $2,430. Recommended Maersk route (ETA 15 days). Profit margin: 22%. Draft quote ready?”*

- **Feedback Mechanism:**  
  User accepts/edit rate → system logs adjustments for retraining rate model.  
  Sales team approval adds labeled “accepted quote” data.

- **Quality Evaluation:**  
  - Quote accuracy within ±5%  
  - Quoting time < 60 sec  
  - Quote-to-Win ratio +25%

---

### 🗺️ 7.3 Route Planner & Optimizer

**Goal:** Suggest the fastest, cheapest, or greenest shipping route.

- **User Input:**  
  “Find cheapest way from Shanghai to Rotterdam.”  
  “Show air vs sea+rail cost difference.”

- **Contextual Data:**  
  - Port distance matrix  
  - Schedule feeds  
  - Weather & congestion data  
  - CO₂ factors by mode  

- **LLM Output:**  
  *“Sea+rail is $300 cheaper, arrives 4 days later, emits 22% less CO₂. DHL optimal for sustainability.”*

- **Feedback Mechanism:**  
  User selects or bookmarks route; system logs preference and updates “recommendation success” stats.

- **Quality Evaluation:**  
  - Route accuracy ≥ 90%  
  - User-chosen recommendation alignment ≥ 80%  
  - CO₂ estimate deviation ≤ 10%

---

### ⚓ 7.4 Predictive Tracking & ETA

**Goal:** Predict accurate delivery times and alert users about delays.

- **User Input:**  
  “Track container ABCD123456.”  
  or “ETA for vessel MSC Vienna.”

- **Contextual Data:**  
  - Vessel ID, location, speed, and port call data  
  - Historical delay patterns  
  - Weather and congestion feeds  

- **LLM Output:**  
  *“Container ABCD123456 currently near Jeddah, moving at 14.2 kn. ETA Hamburg: Oct 31 16:00 ± 6 h.”*

- **Feedback Mechanism:**  
  Actual arrival time logged automatically. Model retrains monthly to reduce deviation.

- **Quality Evaluation:**  
  - ETA Mean Absolute Error ≤ 6 h  
  - Delay alert precision ≥ 90%  
  - User confirmation rate ≥ 85%

---

### 📈 7.5 Lead Scoring & Sales Advisor

**Goal:** Help sales teams focus on the most promising leads.

- **User Input:**  
  “Show today’s top leads.” or “Which customer has highest chance to book?”

- **Contextual Data:**  
  - CRM data: past quotes, follow-ups, conversions  
  - Email open rates, website interactions  
  - Lane & trade type  

- **LLM Output:**  
  *“Top 3 leads: Alpha Logistics (92/100), BlueLine Freight (86), Nordic Trade (79). Suggest calling Alpha Logistics today.”*

- **Feedback Mechanism:**  
  Sales rep logs whether contact converted → system uses to fine-tune scoring model.

- **Quality Evaluation:**  
  - Precision@k ≥ 0.75  
  - Conversion uplift ≥ 20%  
  - Drift < 5% monthly  

---

### 📚 7.6 Knowledge & Compliance Hub (RAG)

**Goal:** Answer operational or compliance questions instantly.

- **User Input:**  
  “What is BAF surcharge for Asia-Europe trade?”  
  “HS code for automotive parts?”

- **Contextual Data:**  
  - Indexed company documents (tariffs, SOPs, HS manuals)  
  - Metadata (date, source, lane)

- **LLM Output:**  
  *“BAF (Bunker Adjustment Factor) is 8.5% for Asia–EU routes. Source: DP World Tariff 2024, Page 7.”*

- **Feedback Mechanism:**  
  User marks helpful/unhelpful; curator verifies accuracy weekly.

- **Quality Evaluation:**  
  - Relevance ≥ 90% (manual review)  
  - Response latency ≤ 2 s  
  - 100% citation traceability  

---

### 🔗 7.7 Integrations & APIs

**Goal:** Seamlessly connect FreightSense with other systems.

- **User Input:**  
  System-level API calls (`/quote`, `/lead`, `/track`).

- **Contextual Data:**  
  API keys, user tokens, tenant configuration.

- **LLM Output:**  
  Structured JSON with AI result for embedding into external CRM/TMS.

- **Feedback Mechanism:**  
  Partner integration usage monitored; success/failure logged for stability.

- **Quality Evaluation:**  
  - API uptime > 99.9%  
  - Data sync error < 1%  
  - Avg. response time < 1 s  

---

### 📊 7.8 Analytics Dashboard

**Goal:** Give decision-makers a real-time snapshot of business and AI performance.

- **User Input:**  
  Select filters (lane, mode, carrier, customer segment).

- **Contextual Data:**  
  Aggregated system logs and AI outputs.

- **LLM Output:**  
  Auto-generated summaries:  
  *“Quote-to-Win ratio up 12% this week; ETA accuracy 94%; top lane DXB-HAM.”*

- **Feedback Mechanism:**  
  Managers can comment or flag anomalies; prompts future data audits.

- **Quality Evaluation:**  
  - Data accuracy ≥ 95%  
  - Report latency < 2 s  
  - Adoption ≥ 70% weekly active users  

---

### 🧠 7.9 AI Feedback & Learning Loop

**Goal:** Ensure AI gets smarter, safer, and more accurate over time.

- **User Input:**  
  Thumbs-up/down, corrections, or verified outcomes.

- **Contextual Data:**  
  Feedback logs, retraining datasets, anomaly detection reports.

- **LLM Output:**  
  Adjusts recommendations and confidence levels automatically.

- **Feedback Mechanism:**  
  Monthly model evaluation; poor predictions flagged for retraining.

- **Quality Evaluation:**  
  - Model drift < 5% monthly  
  - Human validation coverage 100% (sample basis)  
  - Audit trace for every prediction  

---

## 🧩 8. Frontend & Backend Overview

### 🖥️ Frontend
- Built with **Next.js / React** and **TailwindCSS**  
- Main UI components: Chat window, KPI cards, Live Map, Lead list  
- Features dark/light mode  
- Real-time response updates using WebSockets

### ⚙️ Backend
- **APIs:** FastAPI (Python) for AI microservices  
- **Databases:** PostgreSQL for transactions, Pinecone for vector search  
- **AI Layer:** GPT-4o (LLM), Scikit-Learn/XGBoost (predictive models)  
- **Integrations:** Freightos, MarineTraffic, HubSpot, DP World Flow  
- **Hosting:** Vercel (UI) + Render/Hugging Face Spaces (API)

---

## 📈 9. Success Metrics

| Area | Metric | Target |
|------|---------|--------|
| **User Experience** | Avg. task completion time | < 60 s |
| **Pricing Accuracy** | Deviation from actual | ≤ 5% |
| **ETA Precision** | Mean Absolute Error | ≤ 6 h |
| **Lead Conversion** | Improvement vs baseline | + 20% |
| **Customer Satisfaction** | CSAT | ≥ 80% |
| **Adoption** | Weekly active users | ≥ 70% |

---

## 🤖 10. AI Success Criteria

| Metric | Description | Target |
|---------|--------------|--------|
| **Precision@k** | Correctness of top predictions | ≥ 0.75 |
| **F1 Score** | Precision/recall balance | ≥ 0.80 |
| **Latency** | LLM response speed | < 3 s |
| **Explainability** | Prediction with reason | 100% |
| **Model Drift** | Accuracy change / month | < 5% |

---

## 🔄 11. Typical Workflow

1. User asks a question (e.g., *“Quote 40FT Dubai → Hamburg”*).  
2. FreightSense recognizes intent using the LLM.  
3. It fetches contextual data (rates, schedules, user prefs).  
4. AI model predicts the rate + ETA.  
5. LLM formats the answer into plain English.  
6. User acts on it (save, send, or edit).  
7. Feedback recorded → improves next prediction.

---

## 🧱 12. Product Roadmap

| Phase | Focus | Timeframe | Key Output |
|--------|--------|------------|-------------|
| **MVP** | Chat + Quote + Route | 0–2 mo | Pilot prototype |
| **V1** | ETA + Lead Scoring + Docs | 3–4 mo | 100 users |
| **V2** | Booking Bot + Audit | 5–6 mo | Paid SaaS rollout |
| **Enterprise** | Multi-Agent + SLA | 7–9 mo | Large 3PL adoption |
| **Global Scale** | Localization + APIs | 10 mo+ | Developer ecosystem |

---

## 🔗 13. Linked Documents

| Document | Description | Link |
|-----------|--------------|------|
| 👥 **User Stories** | Detailed flows & acceptance criteria | [/docs/UserStories.md](../docs/UserStories.md) |
| 🚀 **GTM Canvas** | Marketing, pricing, channels | [/docs/FreightSense-GTM-Canvas.md](../docs/FreightSense-GTM-Canvas.md) |
| 🧪 **Testing Criteria** | QA & model validation | [/docs/TestingCriteria.md](../docs/TestingCriteria.md) |
| 🎨 **Frontend Guide** | UI standards & components | [/docs/FrontendGuide.md](../docs/FrontendGuide.md) |
| 📊 **README** | Brand, KPIs, competitors | [/README.md](../README.md) |

---

### 🧑‍💼 Author
**Pratik Nirupam Das**  
Product Marketing & AI Product Manager — DP World / SeaRates  
[GitHub: pratikndas-pm](https://github.com/pratikndas-pm)  

**Tagline:** *Navigate Trade with Intelligence.*

---

### © 2025 FreightSense™  
An AI Freight Advisor simplifying global logistics through intelligence, automation & design.
