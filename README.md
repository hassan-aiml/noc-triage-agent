(venv) hassanhai@Mac noc-agent % python noc_agent_v1.py --all

─────────────────────────────────────────────────────────────────
Processing alarm: INT-006 — Grand Hyatt Dallas — Floor 12
─────────────────────────────────────────────────────────────────

[1/4] Embedding alarm...
  Embedding: 'Alarm INT-006: Downlink output power low on single remote RU-04. Measured -18 dB...'

[2/4] Retrieving runbook context...
  Retrieved 1 chunks (3 exact + semantic)

[3/4] Running triage agent...

[4/4] Triage complete.

=================================================================
  NOC TRIAGE BRIEF
=================================================================
  Site:       Grand Hyatt Dallas — Floor 12
  Alarm:      INT-006 — Downlink Output Power Low - Single Remote Unit
  Time:       2025-01-15 02:47:33
  Severity:   P2
  Type:       INTERNAL
  SN Queue:   NOC-Internal-DAS
─────────────────────────────────────────────────────────────────

  IMMEDIATE ACTION
  Isolate RU-04 from service and verify power levels at adjacent test points to confirm amplifier failure versus cabling issue

  PROBABLE CAUSES
  1. Faulty or degraded amplifier in RU-04 remote unit
  2. Loose or damaged RF connector at RU-04 input/output
  3. Failed power supply or power distribution issue to RU-04 amplifier stage

  DIAGNOSTIC CHECKLIST
  1. Verify no EXT-001 alarm at POI feeding this hub (CONFIRMED: none active)
  2. Check power levels at RU-04 input - should match other remotes under same hub
  3. Measure DC voltage at RU-04 amplifier power input
  4. Inspect all RF connectors at RU-04 for physical damage or corrosion
  5. Compare RU-04 configuration against working remotes to rule out mis-provisioning

  VENDOR FIRST-TRIP KIT
  · Replacement remote amplifier module compatible with RU-04
  · RF test set or spectrum analyzer
  · Replacement RF jumpers/connectors
  · Multimeter for DC power verification

  DISPATCH RECOMMENDATION
  OPERATIONS REVIEW REQUIRED

  AGENT REASONING
  This is INTERNAL because EXT-001 is NOT active at the POI, confirming the carrier signal is arriving normally. All other remotes under the same hub show normal DL output, which isolates the fault to RU-04 hardware specifically. The -18 dBm reading (6 dB below threshold) on a single remote while others are normal is classic amplifier degradation or local component failure.

=================================================================

  Saved: triage_INT-006_2025-01-15_02-47-33.json

  [Press Enter to run next alarm, or Ctrl+C to stop]


─────────────────────────────────────────────────────────────────
Processing alarm: INT-006 — Northpark Center Mall — Food Court
─────────────────────────────────────────────────────────────────

[1/4] Embedding alarm...
  Embedding: 'Alarm INT-006: Downlink output power low on ALL 5 remotes under HUB-01 simultane...'

[2/4] Retrieving runbook context...
  Retrieved 2 chunks (3 exact + semantic)

[3/4] Running triage agent...

[4/4] Triage complete.

=================================================================
  NOC TRIAGE BRIEF
=================================================================
  Site:       Northpark Center Mall — Food Court
  Alarm:      INT-006 — Downlink Input Power Loss at POI (Upstream Carrier Failure)
  Time:       2025-01-15 03:55:12
  Severity:   P1
  Type:       EXTERNAL
  SN Queue:   NOC-External-Carrier
─────────────────────────────────────────────────────────────────

  IMMEDIATE ACTION
  Check POI monitoring for EXT-001 alarm status and verify DL input signal presence at demarcation point before any other action

  CARRIER NOTIFICATION REQUIRED
  Notify: All carriers feeding HUB-01
  Ref: OPS-001 carrier notification procedure

  PROBABLE CAUSES
  1. Complete DL input signal loss at POI from carrier BTS/RAN equipment
  2. Carrier fiber cut or transport failure upstream of POI
  3. Carrier BTS power outage or equipment failure affecting all bands/carriers

  DIAGNOSTIC CHECKLIST
  1. Verify EXT-001 (DL input low at POI) alarm is active for HUB-01
  2. Check POI demarcation point signal levels for all carriers feeding this hub
  3. Confirm alarm pattern: simultaneous loss across ALL remotes, ALL carriers, ALL bands under single hub
  4. Rule out INT-002 (hub offline) by verifying hub management is responsive and no hub fault alarms present
  5. Document measured input power at POI and compare to carrier SLA baseline

  DISPATCH RECOMMENDATION
  DO NOT DISPATCH

  AGENT REASONING
  Pattern is definitive for upstream POI input loss (EXT-001), not internal DAS hardware fault. When ALL remotes under a single hub show identical simultaneous DL power loss across ALL carriers and ALL bands, this indicates loss of source signal at the POI feeding that hub. Per META-001 runbook: INT-006 requires checking EXT-001 first. This is external carrier infrastructure, not DAS equipment failure. No vendor dispatch needed.

=================================================================

  Saved: triage_INT-006_2025-01-15_03-55-12.json

  [Press Enter to run next alarm, or Ctrl+C to stop]


─────────────────────────────────────────────────────────────────
Processing alarm: INT-010 — Union Station Dallas — Main Concourse
─────────────────────────────────────────────────────────────────

[1/4] Embedding alarm...
  Embedding: 'Alarm INT-010: TDD clock sync lost at main hub. GPS reference no longer locked. ...'

[2/4] Retrieving runbook context...
  Retrieved 2 chunks (3 exact + semantic)

[3/4] Running triage agent...

[4/4] Triage complete.

=================================================================
  NOC TRIAGE BRIEF
=================================================================
  Site:       Union Station Dallas — Main Concourse
  Alarm:      INT-010 — TDD Clock Sync Lost - GPS Reference Unlocked
  Time:       2025-01-15 03:12:05
  Severity:   P1
  Type:       INTERNAL
  SN Queue:   NOC-Internal-DAS
─────────────────────────────────────────────────────────────────

  IMMEDIATE ACTION
  Disable Meridian Mobile n41 TDD carrier immediately to prevent UL interference and notify Operations for emergency GPS system diagnostics

  CARRIER NOTIFICATION REQUIRED
  Notify: Meridian Mobile
  Ref: OPS-001 carrier notification procedure

  PROBABLE CAUSES
  1. GPS antenna cable damage or disconnection on rooftop
  2. GPS antenna failure or obstruction blocking satellite signal
  3. GPS distribution amplifier failure in equipment room

  DIAGNOSTIC CHECKLIST
  1. Verify GPS antenna cable continuity from rooftop to HUB-01-MAIN equipment room
  2. Check GPS distribution amplifier status and LED indicators in equipment room
  3. Test GPS antenna with known-good receiver to isolate antenna vs distribution fault
  4. Review recent weather events or rooftop maintenance that could have damaged GPS infrastructure

  VENDOR FIRST-TRIP KIT
  · GPS antenna (replacement)
  · GPS distribution amplifier (backup unit)
  · RF cable tester
  · Replacement GPS coaxial cables and connectors

  DISPATCH RECOMMENDATION
  OPERATIONS REVIEW REQUIRED

  AGENT REASONING
  This is an INTERNAL fault because the alarm explicitly states 'GPS reference no longer locked' at our DAS hub equipment. The GPS antenna and distribution system are DAS infrastructure we own and maintain. TDD sync loss is always P1/P2 per critical rules - classified as P1 because loss of sync on TDD bands creates immediate risk of uplink interference to the carrier's network. Meridian must be notified that their n41 TDD service is compromised and should be taken offline until our GPS sync is restored.

=================================================================

  Saved: triage_INT-010_2025-01-15_03-12-05.json

  [Press Enter to run next alarm, or Ctrl+C to stop]


─────────────────────────────────────────────────────────────────
Processing alarm: INT-002 — One Uptown Tower — All Floors
─────────────────────────────────────────────────────────────────

[1/4] Embedding alarm...
  Embedding: 'Alarm INT-002: Main hub HUB-01-MAIN unreachable on management network. All 14 re...'

[2/4] Retrieving runbook context...
  Retrieved 3 chunks (3 exact + semantic)

[3/4] Running triage agent...

[4/4] Triage complete.

=================================================================
  NOC TRIAGE BRIEF
=================================================================
  Site:       One Uptown Tower — All Floors
  Alarm:      INT-002 — Master Hub Complete Outage - Site-Wide DAS Failure
  Time:       2025-01-15 04:05:18
  Severity:   P1
  Type:       INTERNAL
  SN Queue:   NOC-Internal-DAS
─────────────────────────────────────────────────────────────────

  IMMEDIATE ACTION
  Confirm main hub HUB-01-MAIN physical status immediately via on-site security or building management - verify if unit has power lights and attempt local console access if accessible.

  PROBABLE CAUSES
  1. Main hub HUB-01-MAIN power failure (AC power loss or rectifier failure)
  2. Main hub catastrophic hardware failure (controller board, backplane, or power supply)
  3. Upstream network switch failure or fiber cut isolating main hub from management and data networks

  DIAGNOSTIC CHECKLIST
  1. Verify main hub HUB-01-MAIN power status - check breaker panel and UPS/rectifier alarms
  2. Confirm upstream network connectivity - test switch port and fiber to main hub
  3. Check NMS logs for any pre-failure alarms from HUB-01-MAIN (temperature, fan, PSU warnings)
  4. Verify if expansion hub HUB-02-EXP can be reached via alternate path or if truly downstream-only
  5. Correlate alarm timestamp with any scheduled maintenance, power events, or building work

  VENDOR FIRST-TRIP KIT
  · Replacement main hub unit (compatible with HUB-01-MAIN model)
  · Fiber optic test equipment and patch cables
  · Laptop with management console cable and DAS configuration backup

  DISPATCH RECOMMENDATION
  OPERATIONS REVIEW REQUIRED

  AGENT REASONING
  This is INT-002 (master hub offline) - a critical internal DAS failure affecting the entire building across all carriers and bands. With 14 remotes and an expansion hub all unreachable downstream of HUB-01-MAIN, this is the single point of failure. No RF service is possible until main hub is restored. This requires immediate P1 escalation and likely vendor dispatch after Operations confirms the failure mode.

=================================================================

  Saved: triage_INT-002_2025-01-15_04-05-18.json

  [Press Enter to run next alarm, or Ctrl+C to stop]


─────────────────────────────────────────────────────────────────
Processing alarm: EXT-001 — Northpark Center Mall — Food Court
─────────────────────────────────────────────────────────────────

[1/4] Embedding alarm...
  Embedding: 'Alarm EXT-001: DL input power low at POI-MDN-N41. Meridian Mobile n41 (5G TDD) s...'

[2/4] Retrieving runbook context...
  Retrieved 1 chunks (3 exact + semantic)

[3/4] Running triage agent...

[4/4] Triage complete.

=================================================================
  NOC TRIAGE BRIEF
=================================================================
  Site:       Northpark Center Mall — Food Court
  Alarm:      EXT-001 — DL Input Power Loss at POI (Carrier BTS/RAN Issue)
  Time:       2025-01-15 05:33:41
  Severity:   P1
  Type:       EXTERNAL
  SN Queue:   NOC-External-Carrier
─────────────────────────────────────────────────────────────────

  IMMEDIATE ACTION
  Immediately notify Meridian Mobile NOC that n41 (5G TDD) DL signal is absent at POI-MDN-N41, impacting entire Northpark Food Court DAS sector.

  CARRIER NOTIFICATION REQUIRED
  Notify: Meridian Mobile
  Ref: OPS-001 carrier notification procedure

  PROBABLE CAUSES
  1. Meridian Mobile BTS outage or transmitter failure for n41 band
  2. Fiber cut or POI interface failure between Meridian BTS and DAS entry point
  3. Meridian RAN maintenance or configuration change affecting n41 sector

  DIAGNOSTIC CHECKLIST
  1. Verify all other carrier POIs (other than Meridian n41) show normal input levels — CONFIRMED normal per alarm
  2. Check if Meridian has reported any planned maintenance or BTS work on n41 sector
  3. Confirm measured power at POI is -41 dBm (30+ dB below expected -10 to -15 dBm threshold)
  4. Document that impact is sector-wide: main hub, expansion hub, and all remotes affected
  5. Monitor for EXT-001 alarm clearance after Meridian restores signal

  DISPATCH RECOMMENDATION
  DO NOT DISPATCH

  AGENT REASONING
  This is definitively EXTERNAL per runbook EXT-001. The alarm is isolated to a single carrier (Meridian) and single band (n41), with all other POIs showing normal levels. A 30+ dB power loss at the POI entry point indicates the problem is upstream of the DAS — either at the BTS, fiber transport, or POI interface on the carrier side. No DAS vendor dispatch is warranted; Meridian Mobile must restore their transmitter or fiber path.

=================================================================

  Saved: triage_EXT-001_2025-01-15_05-33-41.json

  [Press Enter to run next alarm, or Ctrl+C to stop]


─────────────────────────────────────────────────────────────────
Processing alarm: INT-005 — DFW Terminal B — Gates B1-B20
─────────────────────────────────────────────────────────────────

[1/4] Embedding alarm...
  Embedding: 'Alarm INT-005: Overtemperature alarm on remote unit RU-11. Current temp 68C, ope...'

[2/4] Retrieving runbook context...
  Retrieved 7 chunks (3 exact + semantic)

[3/4] Running triage agent...

[4/4] Triage complete.

=================================================================
  NOC TRIAGE BRIEF
=================================================================
  Site:       DFW Terminal B — Gates B1-B20
  Alarm:      INT-005 — Overtemperature Alarm with Fan Fault
  Time:       2025-01-15 06:18:22
  Severity:   P2
  Type:       INTERNAL
  SN Queue:   NOC-Internal-DAS
─────────────────────────────────────────────────────────────────

  IMMEDIATE ACTION
  Notify Operations and building facilities immediately with current temp (68C), fan fault status, and 7C margin to auto-shutdown threshold.

  PROBABLE CAUSES
  1. Fan module failure (INT-009 co-alarming) causing inadequate cooling
  2. HVAC failure in equipment room (not yet detected by facilities)
  3. Vents or airflow obstructed around RU-11

  DIAGNOSTIC CHECKLIST
  1. Confirm current temperature reading from NMS and verify if trending upward or stable
  2. Verify INT-009 (fan fault) is active on RU-11 and obtain fan status details
  3. Contact building facilities to physically verify HVAC operation in equipment room despite 'normal' report
  4. Check for physical obstructions around RU-11 vents or airflow paths
  5. Review temperature trend over last 2-4 hours to determine rate of increase

  VENDOR FIRST-TRIP KIT
  · Replacement fan module for remote unit
  · Thermal monitoring equipment
  · Portable cooling unit (if HVAC repair delayed)

  DISPATCH RECOMMENDATION
  OPERATIONS REVIEW REQUIRED

  AGENT REASONING
  This is an INTERNAL alarm (DAS hardware issue) classified as P2 because temperature is elevated and trending toward the 75C auto-shutdown threshold with only 7C margin remaining. The co-alarming fan fault (INT-009) is the most likely root cause, making this a DAS equipment issue rather than purely environmental. Despite facilities reporting normal HVAC, the fan failure combined with rising temperature requires urgent coordination between Operations and facilities to prevent imminent auto-shutdown and coverage outage.
