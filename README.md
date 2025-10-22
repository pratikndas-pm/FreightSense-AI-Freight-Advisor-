# FreightSense-AI-Freight-Advisor
# 🚢 FreightSense — AI Freight Advisor  
*Concept, Design, and Development by **Pratik Nirupam Das***  
> *Navigate Trade with Intelligence.*

---

## 🧭 Overview

**FreightSense** is an AI-powered Freight Advisor platform designed to help freight forwarders, shippers, and traders **quote faster, plan smarter, and deliver with confidence.**  

Conceptualized and developed by **Pratik Nirupam Das**, this product unifies predictive analytics, conversational AI, and freight domain intelligence into one decision engine — transforming how global logistics teams operate.

## 🚀 Live Demo  
🎯 **Try the App:** [FreightSense — AI Freight Advisor (Claude Demo)](https://claude.ai/public/artifacts/34608684-edd8-497d-bf8d-d6cc6b2db2fe)

---

## 💡 Vision

> To become the **operating brain for global freight**, where logistics professionals interact with a single AI layer that advises, predicts, and automates across quoting, routing, and customer engagement.

---

## ⚙️ Core Capabilities

| Module | Description | AI Power |
|--------|--------------|-----------|
| 💬 **AI Co-Pilot Interface** | Natural language workspace to query quotes, routes, leads, and shipments. | GPT-4o + Function Calling |
| 💸 **Quote Intelligence** | Predictive pricing, surcharges, and negotiation insights. | ML Rate Prediction + Margin Rules |
| 🗺️ **Route Optimization** | Multi-modal routing with cost-time-carbon trade-offs. | Pathfinding ML + CO₂ Calculator |
| ⚓ **Tracking & Predictive ETA** | Real-time vessel positions with delay forecasting. | ETA Prediction Model |
| 📈 **Lead Intelligence** | Scoring engine that ranks opportunities by conversion likelihood. | Logistic Regression / Gradient Boost |
| 📚 **Knowledge Hub (RAG)** | Retrieves tariffs, SOPs, and HS codes conversationally. | LangChain + Vector Search |
| 🤝 **CRM/TMS Integration** | Syncs quotes, leads, and bookings with business systems. | API Connectors |

# 🚢 FreightSense — AI Freight Advisor  
**Product Requirements Document (PRD)**  
*Concept, Design & Development by **Pratik Nirupam Das***  
> *Navigate Trade with Intelligence.*

🎯 **Try the App:** [FreightSense — AI Freight Advisor (Streamlit Demo)](https://5u3hm7wgdxx9lyjsvqqlxt.streamlit.app/)  

---

## 🧭 1. Product Overview

FreightSense is a **smart AI Freight Advisor** that helps freight forwarders, brokers, and shippers make faster, data-driven decisions — from quoting to tracking.

It combines **AI models**, **live logistics data**, and **conversational intelligence** to provide predictive insights on rates, ETAs, routes, and leads — all in one unified workspace.

---

## 💡 2. The Problem

Freight operations today are **slow, fragmented, and reactive**.  
Teams use multiple systems, emails, and spreadsheets to perform simple tasks like:
- Finding the best freight rate  
- Comparing transit times  
- Tracking delayed containers  
- Identifying promising leads  

This fragmentation leads to **delayed responses**, **inconsistent pricing**, and **poor customer experience**.

---

## 🚀 3. The Solution

FreightSense acts as a **digital co-pilot** for freight teams.  
It lets users ask questions in plain English and instantly get:
- Predictive rate recommendations  
- Optimized routes with CO₂ insights  
- Live shipment tracking with AI-based ETA  
- Ranked customer leads by win probability  

By connecting CRMs, TMSs, and APIs, FreightSense turns raw logistics data into actionable intelligence.

---

## 🎯 4. Vision & Objectives

> “To build the operating brain for global freight — where every logistics decision is assisted by AI.”

### Key Objectives
1. Reduce average quote time from hours → under 60 seconds.  
2. Improve rate accuracy and quote-to-win ratio.  
3. Predict ETAs within ±6 hours of actual arrival.  
4. Automate 30% of repetitive decision workflows.  
5. Achieve 80% user satisfaction (CSAT).

---

## 👥 5. User Personas

| User | Role | Goal | FreightSense Value |
|------|------|------|--------------------|
| **Freight Forwarder** | Pricing/Operations | Generate accurate quotes fast | AI-predicted rates, margin guardrails |
| **Sales Executive** | Sales / BD | Prioritize best leads | Lead scoring & CRM integration |
| **Shipment Coordinator** | Customer Ops | Track delays, predict ETAs | Predictive tracking alerts |
| **Logistics Manager** | Strategy / Decision maker | Improve efficiency & visibility | Unified analytics dashboard |

---

## ⚙️ 6. Product Scope

### In-Scope (MVP + V1)
- Chat-based AI interface  
- Predictive quoting, routing, ETA, and lead scoring  
- Knowledge hub with document search  
- CRM/TMS integration via API  
- Feedback & retraining loop  

### Out-of-Scope
- Payments or invoicing (future phase)  
- End-customer booking portal  

---

## 🧩 7. Detailed Feature Descriptions

Each feature defines:  
**User Input → Contextual Data → AI Output → Feedback Mechanism → Quality Evaluation**

---

### 💬 7.1 Conversational Assistant

**Goal:** Simplify interaction through natural language chat.

- **User Input:** “Compare rates for a 40FT from Dubai to Hamburg.”  
- **Contextual Data:** User profile, recent queries, lane info, preferred carriers.  
- **AI Output:**  
  *“Here are the top 3 carrier options. Maersk offers best cost-time balance (ETA 15 days, $2,430).”*  
- **Feedback:** 👍 / 👎 feedback stored; popular queries become quick actions.  
- **Quality Evaluation:** Intent accuracy ≥95%, response time <3 s.

---

### 💸 7.2 Smart Quote Engine

**Goal:** Automate freight pricing and ensure profitability.

- **User Input:** `/quote origin=Dubai dest=Hamburg equipment=40FT date=next week`  
- **Contextual Data:** Historical rates, carrier APIs, fuel index, congestion data, margin rules.  
- **AI Output:**  
  *“Predicted base rate: $2,430. Valid 7 days. Profit margin: 22%.”*  
- **Feedback:** User edits/accepts → system retrains model.  
- **Quality Evaluation:** ±5 % rate accuracy, quoting time <60 s.

---

### 🗺️ 7.3 Route Planner & Optimizer

**Goal:** Recommend fastest, cheapest, or greenest transport routes.

- **User Input:** “Find fastest route from Shanghai to Rotterdam.”  
- **Contextual Data:** Port distances, weather, congestion, carrier schedules.  
- **AI Output:**  
  *“Sea + rail saves 2 days and reduces CO₂ by 18%.”*  
- **Feedback:** Chosen route logged; system learns user preferences.  
- **Quality Evaluation:** Route accuracy ≥ 90%, CO₂ deviation ≤ 10 %.

---

### ⚓ 7.4 Predictive Tracking & ETA

**Goal:** Track shipments live and forecast delivery with AI.

- **User Input:** “Track container ABCD123456.”  
- **Contextual Data:** Vessel position, speed, port events, weather.  
- **AI Output:**  
  *“Container near Jeddah. ETA Hamburg Oct 31 16:00 ± 6 h.”*  
- **Feedback:** Actual arrival logged for retraining.  
- **Quality Evaluation:** ETA MAE ≤ 6 h, alert precision ≥ 90 %.

---

### 📈 7.5 Lead Scoring & Sales Advisor

**Goal:** Rank leads by conversion potential.

- **User Input:** “Show my top leads this week.”  
- **Contextual Data:** CRM activities, engagement, ticket size, region.  
- **AI Output:**  
  *“Top leads: Alpha (92/100), BlueLine (86), Nordic (79).”*  
- **Feedback:** Sales outcome logged for model update.  
- **Quality Evaluation:** Precision@k ≥ 0.75, uplift ≥ 20 %.

---

### 📚 7.6 Knowledge & Compliance Hub (RAG)

**Goal:** Retrieve freight SOPs, tariffs, and HS codes conversationally.

- **User Input:** “What is the BAF surcharge on Asia–EU trade?”  
- **Contextual Data:** Indexed PDFs, SOPs, tariff manuals.  
- **AI Output:**  
  *“BAF is 8.5 % for Asia–EU. Source: DP World Tariff 2024, Page 7.”*  
- **Feedback:** User marks helpful/unhelpful; verified weekly.  
- **Quality Evaluation:** Relevance ≥ 90 %, latency ≤ 2 s.

---

### 🔗 7.7 Integrations & APIs

**Goal:** Connect FreightSense to CRM, TMS, and partner systems.

- **User Input:** API requests (`/quote`, `/lead`, `/track`).  
- **Contextual Data:** Auth tokens, tenant settings.  
- **AI Output:** Structured JSON for embedding in external tools.  
- **Feedback:** Error logs analyzed for improvement.  
- **Quality Evaluation:** Uptime ≥ 99.9 %, error < 1 %.

---

### 📊 7.8 Analytics Dashboard

**Goal:** Provide managers a live view of performance.

- **User Input:** Filter by lane, mode, customer.  
- **Contextual Data:** Historical KPIs, user activity, model logs.  
- **AI Output:**  
  *“Quote-to-win ↑ 12 %, ETA accuracy 94 %, top lane DXB-HAM.”*  
- **Feedback:** Admins flag anomalies → triggers data audits.  
- **Quality Evaluation:** Data accuracy ≥ 95 %, report latency < 2 s.

---

### 🧠 7.9 AI Feedback & Learning Loop

**Goal:** Keep AI models accurate and explainable.

- **User Input:** Thumbs-up/down, corrections, real outcomes.  
- **Contextual Data:** Feedback logs, retraining samples.  
- **AI Output:** Adjusted weights and confidence scores.  
- **Feedback:** Monthly retraining pipeline.  
- **Quality Evaluation:** Drift < 5 %/month, 100 % traceable decisions.

---

## 🖥️ 8. Frontend Overview

- **Framework:** Next.js / React + TailwindCSS  
- **UI Elements:** Chat window, KPI cards, Live Map, Lead list  
- **Modes:** Light/Dark theme, responsive layout  
- **Behavior:** Real-time chat + shortcut chips + dashboard widgets  
- **Goal:** One-minute task completion with zero learning curve

---

## ⚙️ 9. Backend Overview

- **Framework:** FastAPI (Python) + Node.js for routing  
- **Databases:** PostgreSQL (structured), Pinecone (vectors)  
- **AI Models:** GPT-4o (LLM) | XGBoost/Scikit-Learn (ML)  
- **Integrations:** Freightos, MarineTraffic, HubSpot, DP World Flow  
- **Hosting:** Vercel (UI) + Render/Hugging Face Spaces (API)  
- **Security:** OAuth 2.0, PII masking, audit logs  

---

## 📈 10. Success Metrics

| Area | Metric | Target |
|------|---------|--------|
| **Quotes** | Time to quote | < 60 s |
| | Rate accuracy | ± 5 % |
| **Operations** | ETA MAE | ≤ 6 h |
| **Sales** | Lead conversion uplift | + 20 % |
| **User Experience** | CSAT | ≥ 80 % |
| **Adoption** | Weekly active users | ≥ 70 % |

---

## 🤖 11. AI Success Criteria

| Metric | Description | Target |
|---------|--------------|--------|
| **Precision@k** | Accuracy of top model predictions | ≥ 0.75 |
| **F1 Score** | Balance between precision & recall | ≥ 0.80 |
| **Latency** | Response speed | < 3 s |
| **Explainability** | Prediction with reason / source | 100 % |
| **Drift** | Accuracy change per month | < 5 % |

---

## 🔄 12. Typical Workflow

1. User asks: *“Quote 40FT Dubai → Hamburg.”*  
2. LLM detects intent and required data.  
3. APIs pull rates and schedule data.  
4. AI models predict price and ETA.  
5. LLM composes friendly summary.  
6. User acts (save, send, or edit).  
7. Feedback logged → improves models.

---

## 🧱 13. Product Roadmap

| Phase | Focus | Timeframe | Deliverable |
|--------|--------|------------|--------------|
| **MVP** | Chat + Quote + Route | 0–2 mo | Working prototype |
| **V1** | ETA + Lead Scoring + Docs | 3–4 mo | 100 users |
| **V2** | Booking Bot + Audit | 5–6 mo | Paid SaaS rollout |
| **Enterprise** | Multi-Agent + SLA | 7–9 mo | 3 enterprise clients |
| **Global Scale** | APIs + Localization | 10 mo + | Partner ecosystem |

---

## 🔗 14. Related Documents

| 👥 **User Stories** | User flows & acceptance criteria | [/docs/UserStories.md](../docs/UserStories.md) |

# 👥 FreightSense — AI Freight Advisor  
**User Stories, Detailed Acceptance Criteria & AI Testing Guidelines**  
*Concept, Design & Documentation by **Pratik Nirupam Das***  
> *Navigate Trade with Intelligence.*

---

## 💬 Epic 1 — Conversational Assistant  

### 🧩 Story 1.1 — Natural-Language Freight Advisor  

**As a** freight forwarder or sales executive  
**I want to** ask logistics-related questions like “Compare rates from Dubai to Hamburg” or “Track container ABCD123456”  
**So that** I receive accurate, context-aware answers instantly without manual search or spreadsheets.  

#### User Input  
Plain text or voice query about quoting, routing, tracking or leads.  

#### AI Logic  
1. Intent detection (quote / route / track / lead).  
2. Retrieves data from relevant APIs and internal knowledge graph.  
3. Synthesizes answer with LLM + context memory.  
4. Returns summary and interactive actions (“Draft Quote”, “View Map”).  

#### Acceptance Criteria (≥150 words, point wise)  
- System must correctly identify the intent behind at least 95 % of user queries without explicit keyword prompts.  
- Responses should appear within 3 seconds of input and contain factual data pulled from verifiable sources (e.g., rate API or vessel feed).  
- Each answer must include a short text summary, structured data table, and optional visual output (map or chart).  
- Conversation context should persist for minimum three turns allowing follow-up like “Show cheaper carriers” or “Add insurance cost”.  
- Users can react (👍/👎) and their feedback is stored for model improvement.  
- The system must log query metadata (intent, latency, feedback) for AI performance tracking.  
- UI updates (KPI cards, route tiles) should occur without page reload to maintain conversation flow.  
- The experience should reduce average decision time for users by > 40 % compared to manual lookup.  

#### AI Testing Criteria  

| Metric | Definition | Target |  
|--------|-------------|--------|  
| Intent Accuracy | Correct classification of user intent | ≥ 95 % |  
| Latency | Input to response time | ≤ 3 s |  
| Context Retention | Consistency across multi-turn dialogue | ≥ 90 % |  
| Hallucination Rate | Non-factual content | ≤ 2 % |  
| User Satisfaction | Avg. post-chat rating | ≥ 4.5 / 5 |  

---

## 💸 Epic 2 — Smart Quote Engine  

### 🧩 Story 2.1 — AI-Generated Freight Quote  

**As a** pricing analyst  
**I want to** receive an automatically calculated quote based on shipment inputs  
**So that** I can respond to clients faster and improve profit accuracy.  

#### User Input  
Origin, destination, container type, date.  

#### AI Logic  
1. Fetch live and historical rates from Freightos and DP World Flow.  
2. Predict market rate with regression + seasonality model.  
3. Add BAF/CAF/THC surcharges + currency conversion.  
4. Validate margin and profitability guardrails.  
5. Output structured quote summary (JSON + text view).  

#### Acceptance Criteria (≥150 words, point wise)  
- Quotes must be generated within 60 seconds end-to-end from input submission.  
- Each quote includes base rate, all surcharges, tax components, margin %, and total landed cost in both USD and local currency.  
- A confidence range (high, mid, low) is displayed based on data availability and model variance.  
- If the predicted margin drops below configured threshold (e.g., 10 %), system issues a red warning banner and suggests revised rate.  
- Users can export the quote (PDF/CSV) or push to CRM with a single click.  
- Every approved or edited quote is logged with timestamp, approver ID and final rate for auditing.  
- The system must reduce average manual quote time from 30 minutes to < 1 minute.  
- Accuracy between predicted and actual accepted rates should remain within ± 5 %.  
- Each quote record feeds back into training data to improve future predictions.  

#### AI Testing Criteria  

| Metric | Definition | Target |  
|--------|-------------|--------|  
| MAPE | Mean absolute percentage error vs actual rate | ≤ 5 % |  
| Quote Latency | End-to-end generation time | ≤ 60 s |  
| Margin Compliance | Quotes meeting profit guardrails | 100 % |  
| Quote-to-Win Lift | Improvement vs manual quotes | ≥ 20 % |  
| Data Drift | Monthly accuracy variance | ≤ 5 % |  

---

## 🗺️ Epic 3 — Route Optimization & Planner  

### 🧩 Story 3.1 — Multi-Mode Route Recommendation  

**As a** logistics planner  
**I want to** compare multiple routes (sea, air, rail, combined)  
**So that** I can choose the most efficient or eco-friendly option for each shipment.  

#### User Input  
Origin, destination, preferred mode, priority (cost/time/CO₂).  

#### AI Logic  
1. Collect schedule and congestion feeds.  
2. Compute ETA, cost and CO₂ for all routes.  
3. Rank options with multi-objective optimization.  
4. Return recommendations + map view.  

#### Acceptance Criteria (≥150 words, point wise)  
- At least three distinct route options should appear for every query unless data is missing.  
- Each option must display carrier name, transit days, total cost, and CO₂ impact in kg.  
- User can toggle between “Fastest”, “Cheapest”, and “Greenest” views with instant re-ranking.  
- A visual map should plot stops and transit path with color-coded ETA zones.  
- When users change parameters (e.g., delay by 2 days), system should recalculate in < 15 s.  
- Predicted ETAs must align within ± 6 hours of actual arrival for 80 % of tested routes.  
- The feature should enable users to simulate cost/CO₂ trade-offs and save scenarios to dashboard.  
- All data sources used for recommendations must be traceable for audit (transit schedule ID and timestamp).  
- Route planner should reduce average decision time by > 50 % compared to manual planning.  

#### AI Testing Criteria  

| Metric | Description | Target |  
|--------|--------------|--------|  
| Route Accuracy | Predicted optimal route matches actual best | ≥ 90 % |  
| ETA MAE | Mean absolute error in hours | ≤ 6 h |  
| CO₂ Deviation | Difference from verified emission data | ≤ 10 % |  
| Latency | Computation time | ≤ 30 s |  
| User Adoption | Active route planner usage | ≥ 70 % |  

---

## ⚓ Epic 4 — Predictive Tracking & ETA  

### 🧩 Story 4.1 — Real-Time Shipment Tracking  

**As a** shipment coordinator  
**I want to** track containers and get predicted ETAs  
**So that** I can inform customers of delays before they occur.  

#### Acceptance Criteria (≥150 words, point wise)  
- User can enter container ID or vessel name and view real-time location on map.  
- System must poll telemetry feeds every 15 minutes and update positions automatically.  
- Predicted ETA should include a confidence interval (± hours) and a color-coded risk indicator.  
- If delay > 3 hours is detected, AI sends an alert email and dashboard notification within 5 minutes.  
- The alert message must state reason (e.g., “Port congestion Jeddah”) and new ETA.  
- System stores actual arrival vs predicted ETA for model retraining.  
- Tracking page must load in < 2 s with no manual refresh needed.  
- Feature availability ≥ 99.5 % uptime.  
- Users should report ≥ 80 % trust score in ETA accuracy during pilot surveys.  

#### AI Testing Criteria  

| Metric | Definition | Target |  
|--------|-------------|--------|  
| ETA MAE | Average error vs actual arrival | ≤ 6 h |  
| Alert Precision | True delays correctly flagged | ≥ 90 % |  
| False Positives | Wrong delay alerts | ≤ 10 % |  
| Update Latency | Feed-to-dashboard delay | ≤ 5 min |  

---

## 📈 Epic 5 — Lead Intelligence & Scoring  

### 🧩 Story 5.1 — Sales Lead Prioritization  

**As a** sales executive  
**I want to** see which leads are most likely to convert  
**So that** I focus on high-value opportunities first.  

#### Acceptance Criteria (≥150 words, point wise)  
- System must analyze CRM data (engagement, quote history, region, value) and assign a lead score 0–100.  
- Top 10 % leads should be tagged as Hot (red), next 30 % as Warm, rest Cold.  
- Each lead card shows score, confidence %, and suggested action (call, email, remind).  
- Scoring must refresh nightly or on-demand trigger.  
- User can filter by region or lane and export ranked list to CRM.  
- All lead outcomes (Won/Lost) feed back to training dataset.  
- Lead scoring model must improve conversion rate ≥ 20 % over baseline in A/B test.  
- User interface should display trend of lead score changes over time.  
- Feature accuracy and drift monitored monthly with alert if precision@k drops below 0.7.  

#### AI Testing Criteria  

| Metric | Definition | Target |  
|--------|-------------|--------|  
| Precision@k | Accuracy of top k lead predictions | ≥ 0.75 |  
| F1 Score | Overall classification balance | ≥ 0.80 |  
| Conversion Uplift | Improvement vs control group | ≥ 20 % |  
| Model Drift | Performance change per month | ≤ 5 % |  

---

## 📚 Epic 6 — Knowledge & Compliance Hub (RAG)  

### 🧩 Story 6.1 — AI-Based Document Answering  

**As a** documentation officer  
**I want to** ask questions like “What’s the BAF surcharge for Asia-EU trade?”  
**So that** I can get accurate answers from company manuals instantly.  

#### Acceptance Criteria (≥150 words, point wise)  
- Users can upload PDF/DOC/TXT files for indexing; system confirms successful embedding.  
- When a question is asked, response must include quoted source document name and page number.  
- Response time ≤ 2 s for indexed docs < 50 MB.  
- Answer must contain less than 1 % hallucinated or unverifiable content verified via manual review.  
- Citation link click opens document at referenced section.  
- UI displays confidence score and rephrase option for clarity.  
- Users can mark answers as helpful/unhelpful; these labels feed retrieval fine-tuning.  
- The RAG system should handle > 1,000 documents and maintain query relevance ≥ 90 %.  
- Compliance queries must show 0 PII exposure or data leak.  

#### AI Testing Criteria  

| Metric | Description | Target |  
|--------|--------------|--------|  
| Relevance | Manual judgment score | ≥ 90 % |  
| Citation Accuracy | Correct source mapping | 100 % |  
| Latency | Average response time | ≤ 2 s |  
| Hallucination Rate | Non-factual output | ≤ 1 % |  

---

## 🔗 Epic 7 


---

### 🧑‍💼 Author
**Pratik Nirupam Das**  
Product Marketing & AI Product Manager — DP World / SeaRates  
[GitHub: pratikndas-pm](https://github.com/pratikndas-pm)  

**Tagline:** *Navigate Trade with Intelligence.*

---

### © 2025 FreightSense™  
An AI Freight Advisor simplifying global logistics through intelligence, automation & design.


---

## 🎯 Key KPIs

| Domain | Metrics | Target |
|---------|----------|--------|
| **Sales Efficiency** | Quote-to-Win %, Avg Margin, Time-to-Quote | +25% improvement |
| **Operational Performance** | ETA Mean Abs Error, On-Time %, Exception Resolution | <6h ETA MAE |
| **Adoption & Engagement** | DAU/WAU, Task Completion Rate, CSAT | 70% repeat usage |
| **Lead Conversion** | Precision@k, Conversion by Score Band, Outreach Uplift | +20% conversion |
| **Financial** | Revenue per user, Quote volume handled, AI usage ROI | Break-even <18 months |

---

## 🚀 Product Roadmap

| Phase | Timeframe | Focus | Key Outcomes |
|--------|------------|--------|---------------|
| **MVP** | Month 1–2 | Conversational UI · Quote & Route Advisor · Basic ETA Prediction · Lead Scoring v0 | Working demo + data foundation |
| **V1 Launch** | Month 3–4 | Negotiation Assistant · CRM Sync · Knowledge Hub (RAG) | Commercial pilot |
| **V2 Expansion** | Month 5–6 | Booking Bot · Contract Optimizer · Invoice Audit Engine | SaaS beta program |
| **Enterprise** | Month 7–9 | Multi-Agent Freight Workflow · SLA Watchdog · Predictive Re-bid | Enterprise clients onboard |
| **Global Scale** | Month 10+ | Localization · Self-serve API Platform · Marketplace ecosystem | Regional adoption & partnerships |

---

## 💰 Pricing Strategy

| Tier | Target Users | Offering | Pricing Model |
|------|---------------|-----------|----------------|
| **Free / Trial** | Individual freight agents, small forwarders | Limited quotes + 3 tracked shipments | Free (30 days) |
| **Pro** | Mid-size forwarders, digital brokers | Full AI advisory suite + CRM integration | **USD 99 / user / month** |
| **Enterprise** | Large 3PLs & carriers | Custom ML models, API access, private cloud | **Custom (Volume-based)** |
| **White-Label / OEM** | SaaS or Port operators | FreightSense embedded advisor module | License + revenue-share |

**Pricing logic:** Tiered SaaS + usage-based AI calls → predictable recurring revenue.

---

## 📈 Go-To-Market (GTM) Strategy

### 🎯 Target Segments
- Freight Forwarders (mid & enterprise)
- NVOCCs and Digital Brokers
- Port Communities & Terminal Operators
- 3PLs with legacy TMS/ERP stacks

### 🔑 Value Proposition
> *“Empower your sales, ops, and customer teams with predictive freight intelligence — without new systems.”*

### 🪜 GTM Phases
1. **Phase 1 – Pilot (0–3 months)**  
   - Target 5 forwarders (Middle East / Europe).  
   - Use DP World / SeaRates sandbox data for credibility.
2. **Phase 2 – Partnerships (3–6 months)**  
   - Integrate with Freightos, HubSpot, Salesforce.  
   - Co-market via logistics tech accelerators.
3. **Phase 3 – Growth (6–12 months)**  
   - Launch API plan for digital brokers.  
   - Focus on recurring SaaS and data-insights upsell.

### 📣 Marketing Channels
- LinkedIn thought leadership & demo videos  
- Webinars with freight & supply-chain associations  
- Integration showcases (DP World Flow, Freightos)  
- Product-led onboarding microsite (freightsense.ai/demo)

### 🧩 Sales Motion
Hybrid PLG (Product-Led Growth) + B2B Enterprise:  
- Free trial → convert to Pro users  
- API + data licensing for enterprise contracts  
- Partner onboarding via integrators

---

## 🏆 Competitor Landscape

| Competitor | Core Focus | Limitations | FreightSense Edge |
|-------------|-------------|--------------|--------------------|
| **Freightos** | Rate marketplace | Transactional, not predictive | Predictive quoting & AI advisory |
| **Project44** | Supply-chain visibility | Visibility only, no AI reasoning | Conversational intelligence + decision layer |
| **FourKites** | Real-time tracking | Strong ETA, limited pricing | Unified rate + ETA prediction |
| **CargoWise** | ERP/TMS backbone | Complex UX, legacy modules | Lightweight, AI-first SaaS overlay |
| **DP World Flow / Maersk Flow** | Platform-specific visibility | Closed ecosystem | Vendor-agnostic, API-centric advisor |

**FreightSense differentiator:**  
Combines **LLM intelligence**, **predictive models**, and **domain-specific automation** in a single user experience — turning fragmented logistics tools into one smart decision layer.

---

## 📊 Success Metrics (12-Month Targets)

- **100+ active forwarder accounts**
- **10K+ shipments tracked monthly**
- **20% improvement in quote-to-win ratio**
- **Under 6 hours ETA deviation**
- **> 75 % user satisfaction (CSAT)**

---

## 🧑‍💼 Author & Concept Owner

**Invented, Designed & Developed by:**  
**🧑‍💼 Pratik Nirupam Das**  
Product Marketing & AI Product Manager  

FreightSense represents my vision of an **AI-driven freight ecosystem** that merges predictive data, intelligent automation, and human-centered product design — creating a truly cognitive logistics platform.

---

## 📫 Contact & License

- 🌐 Portfolio: [github.com/pratikndas-pm](https://github.com/pratikndas-pm)  
- ✉️ Email: pratikndas.pm@gmail.com *(placeholder)*  
- 🔖 License: MIT  
- 🧭 Tagline: *Navigate Trade with Intelligence.*

---

### © 2025 Pratik Nirupam Das — FreightSense™  
*An AI Freight Advisor concept redefining digital logistics intelligence.*
