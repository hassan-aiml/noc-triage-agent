---
alarm_id: EXT-004
category: external
subcategory: poi_signal
severity: major
alarm_name: Carrier removed or frequency change at BTS
tags: [carrier, frequency, refarming, RAN_optimization, external, coordination]
---

# Carrier removed or frequency change at BTS

## What this means
A carrier frequency previously active at the POI has disappeared or shifted. Usually means the carrier has refarmed spectrum, shut down a carrier, or remapped a sector.

## Operational context (3PO)
External — carrier action. Do not dispatch DAS vendor. Coordinate with carrier RAN/RF team to understand the change and determine if our DAS gain plan needs updating.

## NOC triage checklist
- [ ] Which carrier and which band/frequency disappeared?
- [ ] Did the carrier notify us in advance? Check email and ticket queue.
- [ ] Is the new frequency (if refarmed) within the DAS passband? Operations must confirm.
- [ ] Is DAS now out of compliance with the agreed frequency plan?

## Actions
1. Contact carrier account team or RAN team to confirm the change
2. Open a coordination ticket with Operations — gain plan update may be required
3. Do not log this as an outage if the carrier intentionally removed the carrier
