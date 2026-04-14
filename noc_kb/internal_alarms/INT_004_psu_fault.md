---
alarm_id: INT-004
category: internal
subcategory: power
severity: critical
alarm_name: Power module fault / PSU alarm
tags: [PSU, power, fuse, breaker, input_voltage]
---

# Power module fault / PSU alarm

## What this means
Internal PSU has failed or input power is out of spec. Without redundant PSU, the hub or remote may lose power entirely.

## Most likely causes (ranked)
1. Input voltage out of spec from building electrical
2. Blown fuse or tripped breaker at IDF/BDF panel
3. PSU hardware failure (heat damage, end of life)
4. Cooling blockage causing PSU thermal shutdown
5. Power surge or transient event

## NOC triage checklist
- [ ] Single PSU alarm (redundant system) or full power loss?
- [ ] Are other IDF/BDF equipment items also affected? Could be shared circuit.
- [ ] Check building power or UPS alarms — possible site-wide event.
- [ ] Is INT-005 (overtemperature) also active? PSU + overtemp = cooling failure.

## Severity
| Condition | Severity |
|---|---|
| Redundant PSU, one failed, system running | P2 — schedule repair |
| Single PSU failed, system down | P1 |
| PSU fault + overtemp co-alarm | P1 — imminent shutdown |

## Vendor first-trip materials
- Spare fuses (assorted, match hub model spec)
- Multimeter to verify input voltage
- Spare PSU module if hot-swap capable and site is high-priority
