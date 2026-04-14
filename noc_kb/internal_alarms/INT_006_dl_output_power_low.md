---
alarm_id: INT-006
category: internal
subcategory: rf_performance
severity: major
alarm_name: Downlink output power low / DL gain alarm
tags: [downlink, RF, gain, POI, coverage, misdiagnosis_risk]
---

# Downlink output power low / DL gain alarm

## What this means
DL RF output at the remote antenna port is below threshold. Coverage is degraded — users see reduced signal, dropped calls, slow data.

## CRITICAL — Most common misdiagnosis in DAS NOC operations
This alarm is frequently caused by an external issue (no or low DL input at the POI from the carrier BTS), NOT a DAS hardware fault.

Always check EXT-001 (DL input low at POI) before assuming the DAS is at fault.

If EXT-001 is also active: notify the carrier. Do NOT dispatch a DAS vendor. This is the single biggest source of unnecessary truck rolls.

## Most likely causes (ranked)
1. Low or no DL input at POI — external, carrier issue (check EXT-001 first)
2. Recent gain configuration change in NMS — operator error
3. Attenuator incorrectly added to RF path during maintenance
4. Gain module or amplifier card hardware fault
5. Partial fiber degradation affecting signal level without triggering full LOS

## NOC triage checklist
- [ ] Is EXT-001 also active? If yes — notify carrier, do NOT dispatch vendor.
- [ ] Any maintenance on this site in the last 48–72 hours?
- [ ] Any NMS configuration changes recently? Check the change log.
- [ ] One remote or multiple? Multiple = upstream issue or POI.
- [ ] What is the actual DL output power reading vs. threshold in NMS?

## Severity
| Condition | Severity |
|---|---|
| Single remote, minor degradation, non-critical zone | P3 |
| Single remote, critical zone | P2 |
| Multiple remotes, building-wide degradation | P2 |
| No DL output at all | P1 |

## Escalation path
External cause confirmed → notify carrier per OPS-001. Do not open internal Operations ticket.
Internal cause confirmed → notify Operations with remote ID, DL power reading, POI input level, recent maintenance log.
