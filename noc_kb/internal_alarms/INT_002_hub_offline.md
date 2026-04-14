---
alarm_id: INT-002
category: internal
subcategory: headend
severity: critical
alarm_name: Master hub / headend offline
tags: [hub, headend, controller, NMS, power, overtemp]
---

# Master hub / headend offline

## What this means
The main DAS controller/headend is unreachable by NMS. All remotes served by this hub are likely down — full site outage.

## Operational context (3PO)
P1 by default. Entire building or zone has no DAS coverage. Notify Operations immediately. If the site has a carrier SLA, the clock is running.

## Most likely causes (ranked)
1. AC or DC power loss at the equipment room
2. Blown fuse or tripped breaker at IDF/BDF
3. Overtemperature shutdown
4. Management port or network issue (hub may still be passing RF — verify before declaring outage)
5. Hub hardware failure

## NOC triage checklist
- [ ] Is this just this hub or is NMS itself down? Check other sites.
- [ ] Are all remotes under this hub also showing offline? Confirms hub is truly down.
- [ ] Did a building power event occur? Check other equipment in same room.
- [ ] Is INT-005 (overtemperature) also active? Overtemp shutdown is common.
- [ ] Does the site have a redundant controller? Confirm whether failover occurred.

## Severity assignment
| Condition | Severity |
|---|---|
| Hub unreachable, remotes still passing RF (management-only) | P3 |
| Hub down, partial remote loss | P2 |
| Hub down, full site outage | P1 |
| Hub down, public safety coverage affected | P1 — notify immediately |

## Escalation
P1: Notify Operations AND site facilities simultaneously. Include: site name, hub ID, all affected remotes, alarm time, whether power/HVAC event is suspected.

## Vendor first-trip materials
- Spare fuses (assorted — match hub spec)
- Spare PSU module (if hot-swap supported)
- Multimeter for input voltage check
- Laptop with NMS and remote access
