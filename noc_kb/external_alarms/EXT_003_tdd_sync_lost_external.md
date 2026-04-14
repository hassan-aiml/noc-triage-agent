---
alarm_id: EXT-003
category: external
subcategory: synchronization
severity: critical
alarm_name: TDD sync lost / GPS reference lost from BTS
tags: [TDD, sync, GPS, 1PPS, B41, n41, CBRS, external, notify_carrier, sector_impact]
---

# TDD sync lost / GPS reference lost from BTS (external source)

## What this means
The TDD frame sync reference coming from the carrier BTS has been lost. Affects TDD bands only: B41, n41, CBRS Band 48. FDD bands are not affected.

Misaligned TDD timing causes the DAS to inject UL noise into the BTS sector — this affects not just the DAS coverage, but the carrier's entire sector including users NOT on the DAS.

## Operational context (3PO)
If sync reference originates from the carrier BTS, this is external — notify carrier immediately.
Also check INT-010 — the fault may be in our own GPS path, not the carrier's.

## NOC triage checklist
- [ ] Is sync reference from carrier BTS or DAS's own GPS? Ask Operations if unsure — varies by site design.
- [ ] Is INT-010 (internal sync alarm) also active? If yes, fault may be in our GPS path.
- [ ] Has the carrier reported UL interference on this sector?
- [ ] Notify Operations — may need to disable TDD carriers until sync is restored.

## CRITICAL
Do not leave TDD carriers active with lost sync. UL noise impact is severe and the carrier will escalate.

## Actions
1. Notify carrier — provide site name, affected bands, alarm time
2. Notify Operations — assess whether TDD carriers should be disabled
3. If internal GPS is also suspect, treat INT-010 simultaneously
