# 🏃 Active Sprint Board

**Current Phase:** Sprint 1.0 (The Core Reporting Flow)

## ✅ Completed Sprints
- [x] **Sprint 0.1:** Core API connections established (Plays, Teams, Players, EDGE).
- [x] **Sprint 0.2:** Lambda Architecture deployed (DAX UNION).
- [x] **Sprint 0.3:** Schema hardening, PK uniqueness, and 2025-2026 season rollover.
- [x] **PROJ-01:** The Standings Matrix. (League Level)
- [x] **PROJ-01.5:** Traditional Stats Integration (G, A, P, GP extracted in DimPlayers).

## 🟡 Sprint 1.0: The Core Reporting Flow (Active)
- [ ] **PROJ-02: The League Dashboard.** Assemble the front page using the PROJ-01 Standings Matrix and a "League Leaders" Top 5 table.
- [ ] **PROJ-03: The Team Report.** Build the mid-level drill-through page. Requires mapping `CurrentTeamAbbrev` into `DimPlayers` to link the roster to the team entity.
- [ ] **PROJ-04: The Player Scorecard.** Finalize the drill-through destination page using the Identity Banner and Traditional Stats KPIs.

## 🧊 Product Backlog (Sprint 2.0 - Advanced Analytics)
- [ ] **PROJ-05:** The EDGE Radar Plot (Re-integrate burst telemetry).
- [ ] **PROJ-06:** Spatial Rink Mapping (Configure the custom SVG visual to plot `X_Coord` and `Y_Coord` from `FactPlayByPlay`).
- [ ] **PROJ-07:** Expected Goals (xG) Distance DAX Model.
- [ ] **PROJ-08:** Trade Target Scatter Plot (Speed vs. Volume).