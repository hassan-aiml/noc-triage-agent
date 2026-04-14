---
alarm_id: INT-001
category: internal
subcategory: remote_unit
severity: critical
alarm_name: Remote unit offline / no comms
tags: [remote_unit, fiber, power, PoE, management_network]
---

# Remote unit offline / no comms

## What this means
The remote unit (RU/RAU) is not responding on the management network. Coverage in the zone served by this unit is lost or degraded.

## Operational context (3PO)
This is an internal DAS alarm — owned and resolved by Operations/vendor. No carrier notification required unless it also triggers EXT-001 (DL input lost) on a carrier.

## Most likely causes (ranked)
1. Loss of fiber or Cat6 connectivity to the remote
2. Loss of PoE or DC power to the remote
3. Upstream switch or PoE injector failure
4. Remote unit hardware failure
5. Management VLAN misconfiguration (unit may still be passing RF)

## NOC triage checklist
- [ ] How many remotes are offline? Single = likely local fault. Multiple on same hub = upstream issue.
- [ ] Is the hub/headend itself reachable? If not, escalate to INT-002 first.
- [ ] Is NMS showing "no comms" or "power fault"? Different root causes.
- [ ] Check if other remotes on the same hub port or switch are affected.
- [ ] Note exact alarm time — correlate with maintenance activity or power events.

## Severity assignment
| Condition | Severity |
|---|---|
| Single remote, non-critical zone | P3 |
| Single remote, high-traffic area | P2 |
| Multiple remotes, same hub | P2 |
| All remotes offline (hub down) | P1 — escalate immediately |

## Escalation
Notify Operations with: site name, remote ID, zone served, alarm time, NMS screenshot.

## Vendor first-trip materials (low cost, always carry)
- Spare fiber jumpers (SC/APC and LC/UPC — 1m, 3m, 5m)
- PoE tester cable
- Spare SFP transceiver (match site wavelength)
- Fiber inspection scope and one-click cleaner
- Laptop with NMS access
