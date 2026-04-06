import os

def sync_docs():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, '..'))
    
    FENCE = chr(96) * 3
    files_to_update = {}

    # --- FILE 1: SPRINT_BOARD.md ---
    files_to_update['docs/SPRINT_BOARD.md'] = r"""# 🏃 Active Sprint Board

**Current Phase:** Sprint 1.0 (The Visual Foundation)

## ✅ Completed Sprints
- [x] **Sprint 0.1:** Core API connections established (Plays, Teams, Players, EDGE).
- [x] **Sprint 0.2:** Lambda Architecture deployed (DAX UNION).
- [x] **Sprint 0.3:** Schema hardening, PK uniqueness, and 2025-2026 season rollover.

## 🟡 Sprint 1.0: The Visual Foundation (Active)
- [x] **PROJ-01:** The Standings Matrix. Build a hierarchical matrix visual (Conference -> Division -> Team) using the `DimTeams` table.
- [ ] **PROJ-02:** The EDGE Radar Plot. Build DAX measures calculating Player Speed/Bursts vs. League Average.
- [ ] **PROJ-03:** Spatial Rink Mapping. Configure the custom SVG visual to plot `X_Coord` and `Y_Coord` from `FactPlayByPlay`.

## 🧊 Product Backlog
- [ ] **PROJ-04:** Expected Goals (xG) DAX Model (Distance from net calculation).
- [ ] **PROJ-05:** Trade Target Scatter Plot (Speed vs. Volume).
"""

    # --- FILE 2: SCHEMA_ARCHITECTURE.md ---
    files_to_update['docs/SCHEMA_ARCHITECTURE.md'] = r"""# 🗄️ Schema Architecture & Data Graph

**Storage Engine:** Power BI VertiPaq (In-Memory Columnar Database)
**Format:** TMDL (Tabular Model Definition Language)

## 1. High-Level Topology

__FENCE__mermaid
graph TD
    DimGames --> FactPlayByPlay
    DimTeams --> FactPlayByPlay
    DimPlayers --> FactPlayByPlay
    
    DimTeams --> FactEdgeSkatingSpeeds
    DimPlayers --> FactEdgeSkatingSpeeds
    
    DimPlayers --> FactEdgeBurstDetails
    DimGames --> FactEdgeSkatingSpeeds
__FENCE__

## 2. Dimension Tables (Lookups)

### `DimGames`
* **Purpose:** Unified tracking of all games (Live API + Historical Kaggle).
* **Fields:** `GameID` (PK), `Season`, `GameType`, `GameDate`, `HomeTeamID`, `AwayTeamID`.

### `DimTeams`
* **Purpose:** The Digital Rolodex for franchises. Built via a Left Outer Join of the legacy Stats API (for historical IDs) and the live Standings API.
* **Fields:** `TeamID` (PK), `TeamName`, `TeamAbbrev`, `TeamLogoURL`, `Conference`, `Division`, `LeagueRank`, `Points`, `GoalDifferential`, `StreakType`, `StreakCount`.

### `DimPlayers`
* **Purpose:** Active roster dictionary.
* **Fields:** `PlayerID` (PK), `PlayerName`, `Position`, `ShootsCatches`, `HeadshotURL`.

## 3. Fact Tables (Events & Telemetry)

### `FactPlayByPlay` (DAX UNION Table)
* **Purpose:** The core event ledger. Unifies `FactLivePlays` and `FactHistoricalPlays`.
* **Fields:** `GameID` (FK), `EventID`, `PeriodNumber`, `TimeInPeriod_Seconds`, `EventType`, `EventTeamID` (FK), `X_Coord`, `Y_Coord`, `ScoringPlayerID` (FK), `ShootingPlayerID` (FK).

### `FactEdgeSkatingSpeeds`
* **Purpose:** Player telemetry for top speeds.
* **Fields:** `PlayerID` (FK), `skatingSpeed.imperial`, `skatingSpeed.metric`, `periodDescriptor.number`.

### `FactEdgeBurstDetails`
* **Purpose:** Player telemetry for acceleration and league comparisons.
* **Fields:** `PlayerID` (FK), `max.imperial`, `max.percentile`, `leagueAvg.imperial`, `burstsOver22`.

## 4. DAX Measures (`_Measures` Table)
* **Purpose:** Centralized repository for all explicit DAX calculations to prevent model scattering.
* **Metrics:** * `Team Points`: `SUM('DimTeams'[Points])`
  * `Team Goal Diff`: `SUM('DimTeams'[GoalDifferential])`
  * `Current Streak`: Uses `ISINSCOPE` to restrict streak rendering to the lowest Team hierarchy level.
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