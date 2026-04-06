import os

def sync_docs():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, '..'))
    
    FENCE = chr(96) * 3
    files_to_update = {}

    # --- FILE 1: SPRINT_BOARD.md ---
    files_to_update['docs/SPRINT_BOARD.md'] = r"""# 🏃 Active Sprint Board

**Current Phase:** Sprint 1.0 (The Core Reporting Flow)

## ✅ Completed Sprints
- [x] **Sprint 0.1:** Core API connections established (Plays, Teams, Players, EDGE).
- [x] **Sprint 0.2:** Lambda Architecture deployed (DAX UNION).
- [x] **Sprint 0.3:** Schema hardening, PK uniqueness, and 2025-2026 season rollover.
- [x] **PROJ-01:** The Standings Matrix. (League Level)
- [x] **PROJ-01.5:** Traditional Stats Integration (G, A, P, GP extracted in DimPlayers).
- [x] **PROJ-02: The League Dashboard.** Assemble the front page using the PROJ-01 Standings Matrix and a "League Leaders" Top 5 table.
- [x] **PROJ-03: The Team Report.** Drill-through functionality and basic tables assembled. (UI/UX formatting parked for later).

## 🟡 Sprint 1.0: The Core Reporting Flow (Active)
- [ ] **PROJ-04: The Player Scorecard.** Finalize the drill-through destination page using the Identity Banner and Traditional Stats KPIs.

## 🧊 Product Backlog (Sprint 2.0 - Advanced Analytics)
- [ ] **PROJ-05:** The EDGE Radar Plot (Re-integrate burst telemetry).
- [ ] **PROJ-06:** Spatial Rink Mapping (Configure the custom SVG visual to plot `X_Coord` and `Y_Coord` from `FactPlayByPlay`).
- [ ] **PROJ-07:** Expected Goals (xG) Distance DAX Model.
- [ ] **PROJ-08:** Trade Target Scatter Plot (Speed vs. Volume).
"""

    # --- FILE 2: SCHEMA_ARCHITECTURE.md ---
    files_to_update['docs/SCHEMA_ARCHITECTURE.md'] = r"""# 🗄️ Schema Architecture & Data Graph

**Storage Engine:** Power BI VertiPaq (In-Memory Columnar Database)
**Format:** TMDL (Tabular Model Definition Language)

## 1. High-Level Topology
*(Updated to reflect strict cascading filters and removal of ambiguous paths)*

__FENCE__mermaid
graph TD
    DimGames --> FactPlayByPlay
    DimPlayers --> FactPlayByPlay
    
    DimTeams --> DimPlayers
    
    DimPlayers --> FactEdgeSkatingSpeeds
    DimPlayers --> FactEdgeBurstDetails
    DimGames --> FactEdgeSkatingSpeeds
__FENCE__

## 2. Dimension Tables (Lookups)

### `DimGames`
* **Purpose:** Unified tracking of all games (Live API + Historical Kaggle).
* **Fields:** `GameID` (PK), `Season`, `GameType`, `GameDate`, `HomeTeamID`, `AwayTeamID`.

### `DimTeams`
* **Purpose:** The Digital Rolodex for franchises. 
* **Fields:** `TeamID` (PK), `FranchiseID`, `TeamName`, `TeamAbbrev`, `TeamLogoURL`, `Conference`, `Division`, `LeagueRank`, `Points`, `GoalDifferential`, `StreakType`, `StreakCount`.

### `DimPlayers`
* **Purpose:** Active roster dictionary.
* **Fields:** `PlayerID` (PK), `PlayerName`, `Position`, `ShootsCatches`, `GamesPlayed`, `Goals`, `Assists`, `Points`, `CurrentTeamAbbrev` (FK to DimTeams), `HeadshotURL`.

## 3. Fact Tables (Events & Telemetry)

### `FactPlayByPlay` (DAX UNION Table)
* **Purpose:** The core event ledger. Unifies `FactLivePlays` and `FactHistoricalPlays`.
* **Fields:** `GameID` (FK), `EventID`, `PeriodNumber`, `TimeInPeriod_Seconds`, `EventType`, `EventTeamID`, `X_Coord`, `Y_Coord`, `ScoringPlayerID` (FK), `ShootingPlayerID` (FK), `HittingPlayerID` (FK), `HitteePlayerID` (FK).

### `FactEdgeSkatingSpeeds`
* **Purpose:** Player telemetry for top speeds.
* **Fields:** `PlayerID` (FK), `skatingSpeed.imperial`, `skatingSpeed.metric`, `periodDescriptor.number`, `homeTeam.abbrev`.

### `FactEdgeBurstDetails`
* **Purpose:** Player telemetry for acceleration and league comparisons.
* **Fields:** `PlayerID` (FK), `SkatingSpeedDetails.maxSkatingSpeed.imperial`, `SkatingSpeedDetails.maxSkatingSpeed.leagueAvg.imperial`, `burstsOver22`, `bursts20To22`, `bursts18To20`.

## 4. DAX Measures (`_Measures` Table)
* **Purpose:** Centralized repository for all explicit DAX calculations to prevent model scattering.
* **Metrics:** Covered in `MEASURE_DICTIONARY.md`
"""

    # --- FILE 3: MEASURE_DICTIONARY.md ---
    files_to_update['docs/MEASURE_DICTIONARY.md'] = r"""# 📏 DAX Measure Dictionary

| Measure Name | Table | Logic | Persona Focus |
| :--- | :--- | :--- | :--- |
| `Team Points` | `_Measures` | `SUM('DimTeams'[Points])` | Casual Fan |
| `Team Goal Diff` | `_Measures` | `SUM('DimTeams'[GoalDifferential])` | Casual Fan |
| `Current Streak` | `_Measures` | Extracts streak contextually at Team hierarchy | Casual Fan |
| `Player Goals` | `_Measures` | `SUM('DimPlayers'[Goals])` | Casual Fan / Manager |
| `Player Assists` | `_Measures` | `SUM('DimPlayers'[Assists])` | Casual Fan / Manager |
| `Player Points` | `_Measures` | `SUM('DimPlayers'[Points])` | Casual Fan / Manager |
| `Games Played` | `_Measures` | `SUM('DimPlayers'[GamesPlayed])` | Casual Fan / Manager |
| `Player Max Speed (mph)` | `_Measures` | `AVERAGE` of EDGE max speed | Fantasy Manager |
| `League Avg Max Speed` | `_Measures` | `AVERAGE` of EDGE league avg speed | Fantasy Manager |
| `Player Bursts > 22mph` | `_Measures` | `SUM` of bursts over 22mph | Fantasy Manager |
| `Player Bursts 20-22mph` | `_Measures` | `SUM` of bursts 20-22mph | Fantasy Manager |
"""

    for relative_path, content in files_to_update.items():
        full_path = os.path.join(project_root, relative_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        safe_content = content.replace('__FENCE__', FENCE)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(safe_content)
        print(f"✅ Synced: {relative_path}")

    print("\n🚀 Post-Sprint Audit complete. Documentation is perfectly synced with the codebase!")

if __name__ == "__main__":
    sync_docs()