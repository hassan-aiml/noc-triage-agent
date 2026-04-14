---
alarm_id: INT-010
category: internal
subcategory: synchronization
severity: major
alarm_name: Clock / sync source lost (internal DAS)
tags: [TDD, sync, GPS, 1PPS, CBRS, B41, n41, timing]
---

# Clock / sync source lost — internal DAS

## What this means
TDD synchronization reference has been lost within the DAS. The hub cannot synchronize its remotes. Affects TDD bands only: B41, n41, CBRS Band 48. FDD bands (B4, B13, AWS) are NOT affected.

## Operational context (3PO)
Internal alarm but with major external impact — a lost TDD sync causes the DAS to inject uplink noise into the carrier BTS sector, desensitizing the entire sector. Do not leave TDD carriers active with lost sync. Notify Operations immediately.

## Most likely causes (ranked)
1. GPS antenna cable disconnected or damaged at the hub
2. GPS receiver lost sky view — obstruction, antenna moved
3. 1PPS cable from BTS or BBU to DAS headend disconnected or damaged
4. GPS receiver hardware failure
5. Hub firmware issue with sync source selection

## NOC triage checklist
- [ ] Which bands are affected? Confirm TDD bands only.
- [ ] GPS status in NMS — "no lock" or "signal lost"?
- [ ] Any maintenance at the hub location or rooftop (GPS antenna)?
- [ ] Is sync coming from BTS or from a dedicated GPS at the DAS hub? (Varies by site — ask Operations if unsure)
- [ ] Has the carrier reported UL interference on this sector?

## Severity — always P1 or P2, never lower
| Condition | Severity |
|---|---|
| TDD sync lost, TDD carriers still active | P1 — notify Operations to disable TDD carriers immediately |
| TDD sync lost, TDD carriers already disabled | P2 — resolve before re-enabling |

## Vendor first-trip materials
- Spare GPS antenna (low cost, always carry)
- Spare GPS antenna coax cable and connectors
- Phone GPS app to verify sky view at antenna location
