---
alarm_id: EXT-001
category: external
subcategory: poi_signal
severity: critical
alarm_name: No DL input / DL input power low at POI
tags: [POI, downlink, BTS, carrier, no_signal, external, notify_carrier]
---

# No DL input / DL input power low at POI

## What this means
The DAS headend sees no or very low downlink signal from the carrier BTS at the Point of Interface (POI). No coverage is being distributed in the building.

## Operational context (3PO) — CRITICAL
This is an EXTERNAL alarm. We do not own the BTS or RAN.
Action: Notify the affected carrier immediately per OPS-001 carrier notification procedure.
Do NOT dispatch a DAS vendor for this alarm.

Our responsibility: confirm signal is absent at the POI, notify the carrier, monitor for restoration, document the carrier ticket number.

## NOC triage checklist
- [ ] Which carrier(s) affected? One carrier = carrier-specific. All carriers simultaneously = check internal (possible DAS headend fault — see INT-002).
- [ ] Is INT-006 (DL output low on remotes) also active? Expected — downstream effect of this alarm.
- [ ] Get DL input power reading at POI from NMS if available.
- [ ] One band or all bands for the carrier? One band = possible carrier refarming. All bands = BTS likely down.

## Severity
| Condition | Severity |
|---|---|
| One carrier, one band, partial loss | P2 — notify carrier |
| One carrier, all bands, full outage | P1 — notify carrier immediately |
| All carriers affected simultaneously | P1 — also check INT-002 (DAS headend) |

## Carrier notification
Notify carrier per OPS-001. Document: alarm time, carrier notified, time of notification, carrier ticket number, restoration time.

## Carrier contacts
See OPS-001 for carrier contact information and notification procedures.
- Carrier A: NOC ___  Account team ___
- Carrier B: NOC ___  Account team ___
- Carrier C: NOC ___  Account team ___
