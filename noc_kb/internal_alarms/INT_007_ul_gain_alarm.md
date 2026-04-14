---
alarm_id: INT-007
category: internal
subcategory: rf_performance
severity: major
alarm_name: Uplink gain alarm / UL path fault
tags: [uplink, UL, gain, noise, PIM, oscillation, carrier_impact]
---

# Uplink gain alarm / UL path fault

## What this means
UL gain is out of spec — either too low (coverage hole, UE devices not heard by BTS) or too high (noise injection into the carrier BTS, oscillation risk).

## Operational context (3PO)
Internal alarm, but with direct external impact — high UL gain or noise pushes back into the carrier's BTS and can desensitize an entire sector. Carrier may contact us before we even alarm.

## Most likely causes
Too low: UL attenuator set incorrectly in NMS; UL path hardware fault.
Too high / noise: UL gain misconfigured; UL noise ingress from external sources near antennas (DECT phones, WiFi APs, other RF equipment); PIM from corroded or loose connectors; open/unterminated antenna port.

## NOC triage checklist
- [ ] Is the gain too low or too high? Determines root cause path.
- [ ] Recent configuration changes in NMS?
- [ ] Any unterminated antenna ports on this remote?
- [ ] Has the carrier reported UL interference on this sector?
- [ ] Single remote or multiple? Multiple = system-wide gain issue.

## Vendor first-trip materials
- 50-ohm terminator caps for unused antenna ports (carry 10+)
- Connector torque wrench
- PIM analyzer access if PIM is suspected
