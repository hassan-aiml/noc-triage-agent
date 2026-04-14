---
alarm_id: INT-011
category: internal
subcategory: transport
severity: major
alarm_name: Redundant path switchover
tags: [redundancy, fiber, backup_path, failover, resilience]
---

# Redundant path switchover

## What this means
The DAS has switched from primary to backup fiber path. Coverage is maintained but the primary path is down. This is a warning, not an outage — but must be treated urgently. If the backup path also fails, service is lost with no further failover.

## NOC triage checklist
- [ ] Confirm in NMS that the remote is truly on backup path, not an alarm artifact.
- [ ] Treat the primary path fault as a Fiber LOS alarm (INT-003) and begin that triage immediately.
- [ ] How long has the switchover been active? If long-standing, it may have been previously missed.

## Severity
| Condition | Severity |
|---|---|
| Backup active, service maintained, primary cause unknown | P2 |
| Backup active, primary cause confirmed and repair scheduled | P3 |
