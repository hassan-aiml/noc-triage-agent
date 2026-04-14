# Demo project — architecture and scope

## Overview
This is a demo project for a neutral host DAS NOC AI triage agent.
The architecture described below reflects standard neutral host DAS deployment
practices. Where simplifications were made for demo scope, they are noted in
the Demo scope section.

---

## Network architecture

### POI (Point of Interface)
- Each carrier has a dedicated POI per band — no band sharing between carriers
- There can be more than one POI for the same band, one per carrier
- When a POI alarm fires, both the carrier and the band are known precisely
- Total of 9 POIs in this demo, all feeding into the main hub

### POI assignments
| POI ID          | Carrier           | Band  |
|-----------------|-------------------|-------|
| POI-VTX-B2      | Vertex Wireless   | B2    |
| POI-VTX-B4      | Vertex Wireless   | B4    |
| POI-VTX-B13     | Vertex Wireless   | B13   |
| POI-PKC-B2      | PeakCell Networks | B2    |
| POI-PKC-B4      | PeakCell Networks | B4    |
| POI-PKC-B13     | PeakCell Networks | B13   |
| POI-MDN-B2      | Meridian Mobile   | B2    |
| POI-MDN-B4      | Meridian Mobile   | B4    |
| POI-MDN-N41     | Meridian Mobile   | n41   |

### Signal flow
```
Carrier BTS
    ↓
POI (carrier and band specific)
    ↓
Main Hub  ←── All POI signals mix here (all carriers, all bands)
    ↓ fiber
Expansion Hub(s)  ←── Receives the same signal mix as main hub
    ↓ fiber
Remote Units (RUs)  ←── Band separation happens here
    ↓
Band-specific amplifier modules on each RU
    ↓
Antennas → Coverage
```

### Hub architecture
- One main hub per sector
- Each sector can have 1–2 expansion hubs
- Main hub failure = full sector outage — all carriers, all bands, all expansion hubs
  and their remotes go down
- Expansion hub failure = partial outage — only the zones served by that expansion
  hub and remotes are affected. 
- If a hub fault is suspected, further investigation or testing is needed

### Remote units
- Each RU receives the full signal mix from the hub via fiber
- Band separation occurs at the RU level
- Each RU has band-specific amplifier modules
- Each amplifier module carries all participating carriers for that band

---

## Carrier band assignments

| Carrier           | Bands          | Technology        |
|-------------------|----------------|-------------------|
| Vertex Wireless   | B2, B4, B13    | LTE               |
| PeakCell Networks | B2, B4, B13    | LTE               |
| Meridian Mobile   | B2, B4, n41    | LTE + 5G NR (TDD) |

---

## Demo scope

- Single sector per site — real deployments typically have multiple independent
  sectors, each with their own hub chain and POI set
- 1–2 expansion hubs per sector — real deployments may have more depending on
  the OEM topology
- No public safety coverage — ERRCS/FirstNet coverage is not modeled
- Band-specific amplifier module alarms not modeled individually — RU alarms
  treat the remote as a single unit for simplicity

---

## Demo alarm scenarios

| Alarm ID     | Site                        | Scenario                                                          |
|--------------|-----------------------------|-------------------------------------------------------------------|
| INT-006      | Grand Hyatt Dallas F12      | Single RU DL output low — local hardware fault                    |
| INT-006-POI  | Northpark Center Mall       | All RUs low simultaneously — POI input loss suspected             |
| INT-010      | Union Station Dallas        | TDD sync lost — GPS antenna at main hub, Meridian n41 affected    |
| INT-002      | One Uptown Tower            | Main hub offline — full sector outage, all downstream unreachable |
| EXT-001      | Northpark Center Mall       | POI-MDN-N41 low input — Meridian n41 loss, entire sector affected |
| INT-005      | DFW Terminal B              | Overtemperature + fan fault on RU-11                              |

### Scenario notes

**INT-006-POI — All RUs low simultaneously:**
When all remotes under a hub show DL output low at the same time, the pattern
points to a POI input issue upstream rather than individual hardware faults.
The agent should check for EXT-001 before classifying as internal.

**EXT-001 — POI-MDN-N41 low input:**
When a POI goes down, the specific carrier and band served by that POI loses
service completely across the entire sector — main hub, all expansion hubs, and
all their remotes. Other carriers and other bands on different POIs continue
operating normally.

**INT-002 — Main hub offline:**
When the main hub goes offline, nothing downstream is reachable — no expansion
hubs, no remotes, no management connectivity. The outage affects all carriers
and all bands for the entire sector. POI input verification is not applicable
in this scenario since the hub itself is the point of failure.

---

## Fictitious data disclosure
- All carrier names, contact persons, phone numbers, and portal URLs are fictitious
- All site names are used for illustration only
- SLA timelines are representative industry estimates, not contractual obligations
- Operations staff names and vendor contacts are fictitious
- ServiceNow instance URL is fictitious
