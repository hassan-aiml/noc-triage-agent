---
alarm_id: INT-012
category: internal
subcategory: management
severity: minor
alarm_name: Management network unreachable / SNMP loss
tags: [NMS, SNMP, management_VLAN, polling, network, misdiagnosis_risk]
---

# Management network unreachable / SNMP loss

## What this means
NMS can no longer poll this element. This may be a network infrastructure issue, NOT a DAS hardware problem. The DAS may be fully operational and passing RF while showing this alarm.

## Common misclassification risk
This alarm is frequently treated as a P1 outage when the DAS is actually fine. Verify whether RF service is affected before escalating.

## Most likely causes (ranked)
1. Management VLAN or routing change on building network
2. SNMP community string changed without updating NMS
3. Firewall rule change blocking SNMP
4. Switch port or management interface down
5. DAS management port hardware failure

## NOC triage checklist
- [ ] Can you ping the management IP from the NMS server?
- [ ] Are other elements on the same switch or VLAN also unreachable?
- [ ] Recent building network maintenance window?
- [ ] Does the carrier report any coverage issue? If not, DAS is likely still passing RF.
- [ ] Check SNMP community strings.

## Severity
| Condition | Severity |
|---|---|
| Management unreachable, RF confirmed active | P3 — IT/network issue |
| Management unreachable, RF status unknown | P2 — treat as potential outage until confirmed |
