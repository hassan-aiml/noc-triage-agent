---
alarm_id: INT-003
category: internal
subcategory: transport
severity: critical
alarm_name: Fiber link alarm / loss of signal on fiber
tags: [fiber, LOS, SFP, connector, OTDR, optical]
---

# Fiber link alarm / LOS on fiber

## What this means
Loss of optical signal on a fiber span between hub and remote. Affected remote(s) go offline.

## Most likely causes (ranked)
1. Dirty or contaminated fiber connector — most common, 50%+ of cases
2. Bent or kinked cable below minimum bend radius
3. Physical cut or crush damage to cable run
4. Failed SFP transceiver at hub or remote
5. Fiber splice failure (more common on longer runs)

## NOC triage checklist
- [ ] How many remotes affected? Single span vs. trunk/riser fiber.
- [ ] Did alarm appear suddenly or gradually? Sudden = physical event. Gradual = contamination or degrading SFP.
- [ ] Any recent construction, maintenance, or MAC activity in the building?
- [ ] Check NMS optical power levels — low Rx power confirms fiber path, not remote hardware.

## Severity
Same criteria as INT-001 — depends on zone criticality and remote count.

## Vendor first-trip materials
- Fiber inspection scope and one-click cleaner (fixes 50% of LOS faults on first visit)
- Spare jumpers: SC/APC and LC/UPC in 1m, 3m, 5m
- Spare SFP transceivers (single-mode 1310nm — match site spec)
- Optical power meter
