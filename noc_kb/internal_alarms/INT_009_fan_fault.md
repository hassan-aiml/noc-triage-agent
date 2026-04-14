---
alarm_id: INT-009
category: internal
subcategory: environmental
severity: minor
alarm_name: Fan fault
tags: [fan, cooling, overtemp, fan_module]
---

# Fan fault

## What this means
One or more internal cooling fans have failed or are running below spec. No immediate service impact, but overtemperature will follow — treat urgently in warm environments.

## NOC triage checklist
- [ ] Is INT-005 (overtemperature) also active? If yes, elevate to P1/P2.
- [ ] What is the ambient temperature at the site?
- [ ] Climate-controlled room or unconditioned space?
- [ ] How many fans faulted? Some units tolerate one failed fan with reduced cooling margin.

## Severity
| Condition | Severity |
|---|---|
| Fan fault, climate-controlled room, no overtemp | P3 — schedule repair |
| Fan fault, warm/unconditioned space, summer | P2 — expedite |
| Fan fault + overtemp active | P1 |

## Vendor first-trip materials
- Replacement fan module (confirm part number before dispatch — inexpensive, always carry)
