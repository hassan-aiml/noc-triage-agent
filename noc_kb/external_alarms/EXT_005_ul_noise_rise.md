---
alarm_id: EXT-005
category: external
subcategory: poi_signal
severity: major
alarm_name: UL noise rise / high UL input at POI
tags: [uplink, noise, POI, BTS, desensitization, PIM, carrier_impact]
---

# UL noise rise / high UL input at POI

## What this means
Excessive uplink noise is being pushed from the DAS back into the BTS at the POI. Desensitizes the BTS and degrades UL performance for all users on that sector.

## Operational context (3PO)
The noise is coming out of our DAS, so we own resolution — but the root cause is usually an internal DAS issue (see INT-007 UL gain alarm). Notify Operations. Carrier may contact us before we alarm.

## NOC triage checklist
- [ ] Is INT-007 (UL gain alarm) also active? Likely yes — work that runbook.
- [ ] Has the carrier already reported UL interference?
- [ ] Single remote or multiple? Determines whether it is localized or system-wide.

## Actions
1. Notify Operations
2. Treat as INT-007 — Operations will isolate remotes in NMS to find the source
3. Notify carrier if they have not already raised an alarm
