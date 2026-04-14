---
alarm_id: INT-005
category: internal
subcategory: environmental
severity: major
alarm_name: Overtemperature alarm
tags: [temperature, HVAC, fan, overtemp, shutdown, facilities]
---

# Overtemperature alarm

## What this means
Hub or remote has exceeded its operational temperature threshold. Equipment may auto-shutdown, causing a coverage outage.

## Operational context (3PO)
Internal alarm — but often requires building facilities coordination for HVAC. Operations handles DAS side; facilities handles room cooling.

## Most likely causes (ranked)
1. HVAC failure in equipment room
2. Vents or airflow obstructed
3. Fan module failed (check INT-009)
4. High ambient temperature — seasonal or building issue
5. DAS overdrive — excessive input power generating excess heat

## NOC triage checklist
- [ ] Is the hub approaching or past shutdown threshold? Get temperature value from NMS.
- [ ] Is INT-009 (fan fault) also active?
- [ ] Ambient temperature at site? Ask facilities or check building BMS.
- [ ] How long has the alarm been active? Trending upward = active problem.
- [ ] Multiple sites affected? May be a seasonal/weather event.

## Severity
| Condition | Severity |
|---|---|
| Elevated, below shutdown, trending stable | P3 |
| Elevated, trending upward, no cooling action | P2 |
| At or above shutdown threshold | P1 |
| Equipment already shutdown | P1 — treat as outage |

## Escalation
Notify Operations AND building facilities. Include: site name, current temp reading, duration, whether fan fault is co-alarming.

## Vendor first-trip materials
- Replacement fan module (confirm part number before dispatch — cheap part)
- IR thermometer
- Temporary portable fan if facilities repair is pending
