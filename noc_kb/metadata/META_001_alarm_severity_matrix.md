---
doc_id: META-001
category: metadata
title: Master alarm reference — severity, escalation, and SLA
tags: [severity, P1, P2, P3, escalation, matrix, SLA, reference, servicenow]
---

# Master alarm reference

## Alarm severity matrix

| Alarm ID | Alarm Name | Default Severity | Escalate To | Notify Carrier? |
|---|---|---|---|---|
| INT-001 | Remote unit offline — single, non-critical zone | P3 | Operations next business day | No |
| INT-001 | Remote unit offline — critical zone or multiple remotes | P2 | Operations within 20 min | No |
| INT-002 | Hub / headend offline — full site down | P1 | Operations immediately | No |
| INT-003 | Fiber LOS — single remote | P2/P3 | Operations | No |
| INT-004 | PSU fault — redundant system, one PSU failed | P2 | Operations | No |
| INT-004 | PSU fault — single PSU, system down | P1 | Operations immediately | No |
| INT-005 | Overtemperature — below shutdown threshold | P3 | Operations + Facilities | No |
| INT-005 | Overtemperature — at or above shutdown threshold | P1 | Operations immediately + Facilities | No |
| INT-006 | DL output power low | Check EXT-001 first | Operations if internal confirmed | Only if EXT-001 active |
| INT-007 | UL gain alarm | P2 | Operations | If carrier reports interference |
| INT-008 | VSWR / antenna mismatch | P3 | Operations | No |
| INT-009 | Fan fault only, no overtemp | P3 | Operations | No |
| INT-009 | Fan fault + overtemp active | P1 | Operations immediately | No |
| INT-010 | TDD sync lost — carriers active | P1 | Operations immediately — disable TDD | Notify if UL noise confirmed |
| INT-010 | TDD sync lost — TDD carriers already disabled | P2 | Operations | No |
| INT-011 | Redundant path switchover — service maintained | P2 | Operations | No |
| INT-012 | Management unreachable — RF status unknown | P2 | IT / Network team | No |
| INT-012 | Management unreachable — RF confirmed active | P3 | IT / Network team | No |
| EXT-001 | DL input low at POI — one carrier, partial | P2 | Carrier NOC | YES — within 30 min |
| EXT-001 | DL input low at POI — one carrier, all bands | P1 | Carrier NOC | YES — within 15 min |
| EXT-001 | DL input low — all carriers simultaneously | P1 | Carrier NOC + Operations | YES — check INT-002 also |
| EXT-002 | DL input overdrive at POI | P1 | Carrier NOC + Operations | YES — within 15 min |
| EXT-003 | TDD sync lost — BTS source | P1 | Carrier NOC + Operations | YES — within 15 min |
| EXT-004 | Carrier frequency removed / changed | P2 | Carrier account team | YES |
| EXT-005 | UL noise rise at POI | P2 | Operations + Carrier | YES |

---

## Severity definitions

<!-- ============================================================
     DEMO DATA — Response times below are reasonable estimates
     for a neutral host 3PO DAS operator without public safety
     service obligations. Replace with your actual contracted
     SLA requirements before production use.
     ============================================================ -->

### P1 — Service affecting, immediate response
- Condition: Full site or full carrier outage, or any fault with imminent risk of outage or network harm (TDD sync, PSU failure, overtemp at threshold)
- NOC notification to Operations: Within 5 minutes of alarm confirmation
- Operations begin review: Within 15 minutes
- Target restore: 4 hours for full outage; 2 hours for TDD sync (disable first)
- ServiceNow: P1 incident auto-pages on-call Operations Engineer

### P2 — Service degraded, urgent response
- Condition: Partial outage, single carrier full loss, single remote down in critical zone, redundant path active
- NOC notification to Operations: Within 20 minutes of alarm confirmation
- Operations begin review: Within 60 minutes
- Target restore: 8 hours
- ServiceNow: P2 incident assigned to on-call Operations Engineer, no auto-page

### P3 — Minor or scheduled repair
- Condition: Single remote in non-critical zone, fan fault without overtemp, VSWR without power impact, management-only issues
- NOC notification to Operations: Within 60 minutes or at next business day
- Operations begin review: Next business day
- Target restore: 3–5 business days
- ServiceNow: P3 ticket queued to Operations backlog

<!-- END DEMO DATA — Severity definitions -->

---

## Critical zones — severity upgrade rule

<!-- ============================================================
     DEMO DATA — Site names, zone classifications, and carrier
     assignments below are fictitious examples for demo purposes.
     Replace with your actual site portfolio and criticality
     designations. Public safety coverage is NOT included in
     this demo — add those sites as P1 minimum if applicable.
     ============================================================ -->

Alarms at these sites are upgraded by one severity level (P3 → P2, P2 → P1):

| Site | Zone Type | Reason |
|---|---|---|
| Grand Hyatt Dallas — Lobby, Ballrooms | High-traffic hospitality | SLA with property; high guest complaint rate |
| One Uptown Tower — Lobby, Floors 1–5 | Class A office | Executive tenants; property SLA |
| Northpark Center — Food Court, Main Concourse | High-traffic retail | High footfall; carrier visibility |
| DFW Terminal B — Gates B1–B20 | Airport | High-visibility, fast-escalating traveler complaints |
| Parkland Medical Center — Main Building | Healthcare | Patient and staff dependency; treat all as P2 minimum |

<!-- END DEMO DATA — Critical zones -->

---

## Escalation contacts reference

<!-- ============================================================
     DEMO DATA — All names and contact information below are
     fictitious placeholders for demo purposes.
     Replace before production use.
     ============================================================ -->

| Role | Name | Phone | Available |
|---|---|---|---|
| On-Call Ops Engineer (primary) | Derek Sandoval | (214) 555-0461 | 24/7 rotation |
| On-Call Ops Engineer (backup) | Priya Nair | (214) 555-0478 | 24/7 rotation |
| Operations Manager | Tom Beckett | (214) 555-0490 | Business hours + P1 |
| VP of Operations | Angela Torres | (214) 555-0501 | P1 escalation only |
| Primary Vendor (Apex Field Services) | Kevin Marsh | (214) 555-0624 | 24/7 dispatch |
| Secondary Vendor (NovaTech) | Lisa Huang | (972) 555-0758 | Business hours + after-hours line |

<!-- END DEMO DATA — Escalation contacts -->

---

## ServiceNow quick reference

<!-- ============================================================
     DEMO DATA — ServiceNow instance and queue names below are
     fictitious. Replace with your actual configuration.
     ============================================================ -->

| Queue | Use for |
|---|---|
| NOC-Internal-DAS | All internal DAS alarms (INT-001 through INT-012) |
| NOC-External-Carrier | All external carrier alarms (EXT-001 through EXT-005) |
| OPS-VendorDispatch | Vendor work orders — created by Operations, not NOC |

ServiceNow instance: https://texnetdas-demo.service-now.com
P1 auto-page: Enabled — triggers on NOC-Internal-DAS severity = P1
Carrier ticket field: Required for all NOC-External-Carrier tickets

<!-- END DEMO DATA — ServiceNow -->
