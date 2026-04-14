---
alarm_id: EXT-002
category: external
subcategory: poi_signal
severity: critical
alarm_name: DL input power high / POI overdrive
tags: [POI, overdrive, intermod, compression, attenuator, external, notify_carrier, hardware_risk]
---

# DL input power high / POI overdrive

## What this means
Signal arriving at the POI from the carrier BTS exceeds the DAS rated maximum input. Causes intermodulation distortion, signal compression, and can damage DAS hardware.

## Operational context (3PO)
External alarm — caused by the carrier's BTS output. Notify carrier AND notify Operations simultaneously. Operations may authorize adding a fixed attenuator at the POI as an immediate protective measure to prevent hardware damage.

## Most likely causes
1. Carrier increased BTS output power without coordinating with us
2. Carrier added a new frequency carrier to an already-loaded POI port
3. Carrier upgraded BTS hardware with higher rated output

## NOC triage checklist
- [ ] Current input power level vs. rated maximum? Get from NMS.
- [ ] One band or all bands affected?
- [ ] Has the carrier communicated any recent changes?
- [ ] Any DAS hardware damage indicators (intermod alarms, unexpected output behavior)?

## Actions
1. Notify carrier immediately — provide measured input power level
2. Notify Operations simultaneously — they may authorize attenuator install as bridge
3. Document all communications and timestamps

## Vendor first-trip materials (if Operations authorizes attenuator install)
- Fixed attenuators: 3 dB, 6 dB, 10 dB — N-type (inexpensive, always carry a set)
