---
alarm_id: INT-008
category: internal
subcategory: rf_performance
severity: minor
alarm_name: VSWR / antenna port mismatch
tags: [VSWR, antenna, connector, mismatch, N_connector, DIN]
---

# VSWR / antenna port mismatch

## What this means
High reflected power on an antenna port — antenna is loose, damaged, missing, or there is an impedance mismatch in the antenna path. Reflected power can damage amplifiers over time.

## Most likely causes (ranked)
1. Loose N-connector or DIN connector at the antenna port
2. Missing antenna — unterminated port needs a 50-ohm cap
3. Damaged antenna from physical impact, water ingress, or cut cable near antenna
4. Wrong cable or connector type used during maintenance
5. Excessive bend stress on cable near connector

## NOC triage checklist
- [ ] Any work done in the building recently? Maintenance crews commonly knock antennas.
- [ ] Is INT-006 (DL output power low) also active on the same remote? If yes, escalate to P2.
- [ ] How many antenna ports affected? Single = physical. All on same remote = remote hardware.

## Vendor first-trip materials
- 50-ohm terminator caps — N-type and DIN (carry 10+ of each, they cost almost nothing)
- Torque wrench for N-connectors (20–25 in-lbs)
- Spare N-type and DIN connectors and short jumpers
- Cable/antenna analyzer
