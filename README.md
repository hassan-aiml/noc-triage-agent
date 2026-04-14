# NOC Triage Agent
**AI-powered alarm triage for neutral host DAS operations — built with Python, LangChain, Claude, Supabase pgvector, and Voyage AI**

---

## What it does

NOC engineers at neutral host DAS companies receive dozens of alarms per shift. The critical decision — is this an internal DAS hardware fault or an external carrier issue? — determines whether you dispatch a field tech, notify a carrier, or do nothing. Getting it wrong wastes hours and violates SLAs.

This agent automates that decision.

Given a raw alarm, it:
1. Embeds the alarm using Voyage AI and retrieves relevant runbook context via semantic search (Supabase pgvector)
2. Runs a reasoning chain (LangChain + Claude) that applies runbook logic to classify the alarm
3. Outputs a structured triage brief: severity, type, dispatch recommendation, probable causes, and step-by-step diagnostics

**It doesn't just classify — it explains its reasoning.** Every brief includes an AGENT REASONING block showing exactly why the agent made its decision.

---

## Demo: 6 alarm scenarios

| Alarm | Site | Classification | Dispatch |
|-------|------|---------------|----------|
| INT-006 (single RU) | Grand Hyatt Dallas | INTERNAL — amplifier failure | Ops review |
| INT-006 (all remotes) | Northpark Center Mall | EXTERNAL — carrier signal loss at POI | Do not dispatch |
| INT-010 (GPS sync loss) | Union Station Dallas | INTERNAL — GPS antenna/distribution | Ops review |
| INT-002 (hub offline) | One Uptown Tower | INTERNAL — master hub failure | Ops review |
| EXT-001 (carrier input low) | Northpark Center Mall | EXTERNAL — Meridian n41 BTS failure | Do not dispatch |
| INT-005 (overtemp + fan fault) | DFW Terminal B | INTERNAL — co-alarming fan module | Ops review |

The most interesting case: **two INT-006 alarms at the same site** get classified differently — one as internal (single RU fault), one as external (all remotes down simultaneously = upstream POI loss). The agent correctly reads the pattern.

---

## Architecture

```
Alarm input (JSON)
      │
      ▼
Voyage AI embeddings
      │
      ▼
Supabase pgvector (RAG retrieval)
   ← runbook chunks →
      │
      ▼
LangChain + Claude (Anthropic)
   ← triage reasoning →
      │
      ▼
Structured triage brief (JSON + CLI output)
```

**Stack:**
- **Claude (Anthropic)** — reasoning engine, classification logic, structured output generation
- **LangChain** — orchestration, chain management
- **Voyage AI** — domain-optimized embeddings for telecom/RF content
- **Supabase + pgvector** — runbook storage and semantic retrieval
- **Python** — CLI runner, JSON output, batch processing

---

## Key design decisions

**Why Voyage AI instead of OpenAI embeddings?**
Telecom runbooks have dense technical vocabulary (DL/UL power levels, TDD sync, POI demarcation, hub topology). Voyage AI's domain-tuned models retrieve more relevant chunks than general-purpose embeddings on this content.

**Why RAG instead of stuffing all runbooks in context?**
Runbooks grow. Retrieval keeps the context window clean and forces the agent to work with the most relevant procedure — same way a trained NOC tech would consult the right section, not read the whole manual.

**Why structured JSON output?**
Every brief saves to JSON. This makes it trivial to connect downstream: ticketing systems (ServiceNow, Jira), carrier notification workflows, NMS dashboards.

---

## Running the demo

```bash
git clone https://github.com/hassan-aiml/noc-triage-agent
cd noc-triage-agent
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
```

Set environment variables:
```bash
ANTHROPIC_API_KEY=your_key
VOYAGE_API_KEY=your_key
SUPABASE_URL=your_url
SUPABASE_KEY=your_key
```

Run all demo scenarios:
```bash
python noc_agent_v1.py --all
```

Run a single alarm:
```bash
python noc_agent_v1.py --alarm INT-006
```

---

## Output format

Each triage brief includes:
- **Site / Alarm / Time / Severity / Type** — structured metadata
- **Immediate action** — first thing the NOC engineer should do
- **Carrier notification** — if external, which carrier and which procedure
- **Probable causes** — ranked list
- **Diagnostic checklist** — step-by-step verification
- **Vendor first-trip kit** — what to send with the tech (internal only)
- **Dispatch recommendation** — OPERATIONS REVIEW REQUIRED or DO NOT DISPATCH
- **Agent reasoning** — plain-English explanation of the classification decision

Saved as: `triage_{ALARM_ID}_{TIMESTAMP}.json`

---

## What's next

- [ ] Webhook intake for live NMS alarm feeds
- [ ] Auto-carrier notification via email/SMS trigger on EXT-001 classification
- [ ] ServiceNow ticket creation on OPERATIONS REVIEW REQUIRED
- [ ] Multi-tenant runbook support (per-site, per-carrier configs)

---

## About

Built by Hassan Hai — exploring applied AI for telecom operations. Background in neutral host DAS, currently completing a postgraduate program in AI/ML.

[LinkedIn](https://www.linkedin.com/in/hassan73/) · [Portfolio](hassan-aiml)
