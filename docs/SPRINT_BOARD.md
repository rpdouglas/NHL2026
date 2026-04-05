# 🏃 Active Sprint Board

**Current Phase:** Sprint 1.0 (The Visual Foundation)

## ✅ Completed Sprints
- [x] **Sprint 0.1:** Core API connections established (Plays, Teams, Players, EDGE).
- [x] **Sprint 0.2:** Lambda Architecture deployed. Historical Kaggle CSV successfully appended via DAX UNION to bypass Mashup Engine memory limits.
- [x] **Sprint 0.3:** Schema hardening. `DimTeams` enriched with live standings. All fact tables strictly typed (Int64, Decimal).

## 🟡 Sprint 1.0: The Visual Foundation (Active)
- [ ] **PROJ-01:** The Radar Plot. Build DAX measures to calculate Player EDGE metrics vs. League Averages for Fantasy Manager comparisons.
- [ ] **PROJ-02:** Spatial Mapping. Translate `X_Coord` and `Y_Coord` onto a custom SVG hockey rink background.
- [ ] **PROJ-03:** The Standings Matrix. Build a hierarchical matrix visual (Conference -> Division -> Team) using the unified `DimTeams` table.

## 🧊 Product Backlog (Future Epics)
- [ ] **PROJ-04:** Expected Goals (xG) Model. Implement a DAX algorithm calculating shot danger based on distance and angle from the net.
- [ ] **PROJ-05:** Automated Daily Refresh. Migrate the Power BI Desktop file to the Power BI Service and configure scheduled refreshes via a personal gateway.
