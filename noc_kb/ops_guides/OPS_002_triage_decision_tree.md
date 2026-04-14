---
doc_id: OPS-002
category: ops_guide
title: NOC triage decision tree — first 5 minutes
tags: [triage, decision, internal, external, carrier, escalation, procedure, servicenow]
---

# NOC triage decision tree — first 5 minutes

## Step 1: Classify the alarm — internal or external?

### External alarms — notify carrier, do NOT open internal ops ticket
- No DL input or DL input low at POI → EXT-001 → notify carrier per OPS-001
- DL input overdrive at POI → EXT-002 → notify carrier AND Operations
- TDD sync lost and source is BTS → EXT-003 → notify carrier AND Operations
- Carrier frequency removed or changed → EXT-004 → contact carrier account team
- UL noise rise at POI → EXT-005 → notify Operations AND carrier

### Internal alarms — notify Operations, vendor dispatch requires Operations authorization
- Any remote unit, hub, fiber, PSU, thermal, RF, or management alarm → INT-001 through INT-012 → open ServiceNow internal ticket

---

## Step 2: Scope — how many elements are affected?

| Scope | Probable cause | Assign |
|---|---|---|
| Single remote offline | Local fiber, PoE, or hardware fault | P2 or P3 based on zone |
| Multiple remotes, same hub | Hub upstream, trunk fiber, or switch issue | P2 |
| All remotes on site | Hub down or full site power loss | P1 |
| Multiple sites simultaneously | Check NMS health first — may be NMS or management network issue, not field |

---

## Step 3: Zone criticality — assign severity adjustment

<!-- ============================================================
     DEMO DATA — Critical zones and site classifications below are
     fictitious examples for demo purposes. Replace with your
     actual site inventory and criticality designations.
     Note: No public safety coverage is included in this demo.
     ============================================================ -->

### Critical zones (upgrade severity by one level if affected)
These sites carry high traffic or contractual priority and warrant faster response:

| Site Name | Zone Type | Carriers | Notes |
|---|---|---|---|
| Grand Hyatt Dallas — Floors 1–3, Ballrooms | High-traffic hospitality | Vertex, PeakCell, Meridian | Events venue — frequent large gatherings |
| One Uptown Tower — Lobby, Floors 1–5 | Class A office, high density | Vertex, Meridian | Executive tenant SLA expectation |
| Northpark Center Mall — Food Court, Main Concourse | Retail, high footfall | All three carriers | Weekends especially high traffic |
| DFW Terminal B — Gates B1–B20 | Airport transit | Vertex, PeakCell | High visibility, traveler complaints escalate fast |
| Parkland Medical Center — Main Building | Healthcare facility | All three carriers | Patient and staff dependency — treat all alarms as P2 minimum |

### Standard zones (normal severity applies)
All other sites in portfolio follow the default severity matrix in META-001.

<!-- END DEMO DATA — Zone criticality -->

---

## Step 4: SLA response time targets by severity

<!-- ============================================================
     DEMO DATA — Response time targets below are reasonable
     industry estimates for a neutral host 3PO operator.
     No public safety SLA is included in this demo.
     Replace with your actual contractual SLA obligations.
     ============================================================ -->

| Severity | Condition | NOC Notify Operations | Operations Begin Review | Target Restore |
|---|---|---|---|---|
| P1 | Full site outage — all carriers, all bands | Immediately (≤5 min) | ≤15 minutes | 4 hours |
| P1 | Full site outage — single carrier, all bands | ≤10 minutes | ≤20 minutes | 4 hours |
| P1 | TDD sync lost with carriers active | Immediately (≤5 min) | ≤15 minutes | 2 hours (disable TDD first) |
| P2 | Partial outage — multiple remotes down | ≤20 minutes | ≤60 minutes | 8 hours |
| P2 | Single remote down — critical zone | ≤20 minutes | ≤60 minutes | 8 hours |
| P2 | Redundant path active, primary down | ≤30 minutes | ≤2 hours | Next business day |
| P3 | Single remote — non-critical zone | ≤60 minutes | Next business day | 3 business days |
| P3 | Fan fault, VSWR, management unreachable | Log ticket | Next business day | 5 business days |

<!-- END DEMO DATA — SLA targets -->

---

## Step 5: Operations escalation contacts

<!-- ============================================================
     DEMO DATA — All names, phone numbers, and email addresses
     below are fictitious placeholders for demo purposes.
     Replace with actual Operations on-call personnel and
     escalation paths before using in production.
     ============================================================ -->

### Operations on-call rotation

| Role | Name | Phone | Email | Hours |
|---|---|---|---|---|
| On-Call Operations Engineer (primary) | Derek Sandoval | (214) 555-0461 | d.sandoval@texnetdas-demo.com | 24/7 rotation |
| On-Call Operations Engineer (backup) | Priya Nair | (214) 555-0478 | p.nair@texnetdas-demo.com | 24/7 rotation |
| Operations Manager (P1 escalation) | Tom Beckett | (214) 555-0490 | t.beckett@texnetdas-demo.com | Business hours + P1 on-call |
| VP of Operations (major P1 / SLA breach risk) | Angela Torres | (214) 555-0501 | a.torres@texnetdas-demo.com | P1 escalation only |

### Escalation path for internal alarms

1. NOC opens ServiceNow ticket (queue: NOC-Internal-DAS)
2. NOC calls On-Call Operations Engineer — Derek Sandoval (primary) or Priya Nair (backup)
3. If no response in 20 minutes: call Operations Manager — Tom Beckett
4. If P1 with no Operations response in 30 minutes: call VP of Operations — Angela Torres
5. Operations Engineer reviews remotely, develops vendor scope of work, dispatches per OPS-003

### Escalation path for external alarms

1. NOC notifies carrier per OPS-001
2. NOC opens ServiceNow ticket (queue: NOC-External-Carrier) — log carrier ticket number
3. NOC notifies On-Call Operations Engineer as an FYI for P1 (no action required unless DAS is also at fault)
4. If carrier does not restore within SLA window — escalate to Operations Manager to engage carrier account team

<!-- END DEMO DATA — Operations contacts -->

---

## Step 6: Common misclassification traps — check these before escalating

| What NOC sees | Wrong action | Correct action |
|---|---|---|
| DL output power low on remotes | Dispatch DAS vendor | Check POI input (EXT-001) first — if external, notify carrier only |
| Management network unreachable | Declare P1 outage | Confirm RF is still active before escalating; may be IT/network issue |
| TDD sync lost | Treat as minor | Always P1/P2 — notify Operations immediately, consider disabling TDD carriers |
| All carriers down simultaneously | Notify all carriers individually | Check DAS headend (INT-002) first — single internal fault can look like all carriers |
| Fan fault, no other alarms | Ignore until overtemp appears | Log P3 ticket now — proactive repair prevents overtemp shutdown |

---

## Step 7: ServiceNow ticket minimum fields

Every alarm must have a ServiceNow ticket, internal or external. Minimum required fields:

- Site name and address
- Alarm ID and name from this KB
- Severity (P1 / P2 / P3)
- Category (internal / external)
- Time alarm first appeared
- NMS screenshot or alarm detail (attach)
- What NOC already checked (POI input level, ping test result, carrier contact, etc.)
- For external: carrier ticket number
- For internal: Operations engineer notified (name and time)

<!-- ============================================================
     DEMO DATA — ServiceNow instance below is fictitious.
     ============================================================ -->
ServiceNow: https://texnetdas-demo.service-now.com
Internal queue: NOC-Internal-DAS
External queue: NOC-External-Carrier
P1 auto-page: Enabled for NOC-Internal-DAS severity = P1
<!-- END DEMO DATA -->
