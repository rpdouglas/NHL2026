import os

def create_docs():
    # 1. Define paths relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, '..'))
    
    # 2. The FENCE variable protects markdown code blocks during writing
    FENCE = chr(96) * 3

    files_to_create = {}

    # --- FILE 1: CONTEXT DUMP ---
    files_to_create['docs/CONTEXT_DUMP.md'] = r"""# 🧠 NHL 2026: Platform Context

**Stack:** Power BI Desktop (TMDL Format) + Python (Code Extraction) + DAX + Power Query (M)
**Data Sources:** Live NHL Web API (`v1/gamecenter`, `v1/edge`, `v1/standings`) + Historical Kaggle Datasets (`game_plays.csv`, `game.csv`).
**Version:** v1.0.0 (Development)

## 🏗️ Architectural Pillars

### 1. The Lambda Architecture (Y-Intersection)
* **Rule:** We never force Power Query to stitch massive historical local files with live web APIs. 
* **Mechanism:** Live data (`FactLivePlays`) and Historical data (`FactHistoricalPlays`) are extracted independently in Power Query. They are merged instantly in RAM using the DAX `UNION` function (`FactPlayByPlay = UNION('FactLivePlays', 'FactHistoricalPlays')`).

### 2. Strict Star Schema
* **Rule:** Fact tables NEVER connect to other Fact tables.
* **Mechanism:** All relationships must flow strictly from Dimension tables (`DimGames`, `DimTeams`, `DimPlayers`) downstream to Fact tables (1-to-Many). Cross-filtering is single-directional unless explicitly required for a complex measure.

### 3. Memory & Performance Efficiency
* **Rule:** Keep the VertiPaq engine lean.
* **Mechanism:** * "Auto Date/Time" is strictly disabled globally.
    * All Staging queries (e.g., `Staging_EDGE`) have "Enable Load" unchecked.
    * The massive 750MB Kaggle CSV utilizes Early Filtering (>= 2021 season) to prevent RAM timeouts during development.

### 4. Explicit Data Typing
* **Rule:** No implicit type conversions. No `any` types in the final model.
* **Mechanism:** Every column in Power Query terminates with a strict `Table.TransformColumnTypes` step. IDs are `Int64.Type`, coordinates/speeds are `type number` (Decimal), and text strings are `type text`.
"""

    # --- FILE 2: SCHEMA ARCHITECTURE ---
    files_to_create['docs/SCHEMA_ARCHITECTURE.md'] = r"""# 🗄️ Schema Architecture & Data Graph

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
* **Fields:** `TeamID` (PK), `TeamName`, `TeamAbbrev`, `TeamLogoURL`, `Conference`, `Division`, `LeagueRank`, `Points`.

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
"""

    # --- FILE 3: PERSONAS ---
    files_to_create['docs/PERSONAS.md'] = r"""# 👥 Persona-Based Dashboard Design

Visuals and measures must pass the "Persona Check" based on the user's analytical goals and technical literacy.

## 1. The Casual Fan (High-Level)
* **Goal:** Wants to see the score, who scored, and basic team standings instantly.
* **Pain Point:** Overwhelmed by spreadsheets and complex scatter plots.
* **UX Constraint:** Big KPIs, prominent SVG team logos, simple bar charts, and clear conditional formatting (Win/Loss).

## 2. The Fantasy Manager (Mid-Level)
* **Goal:** Needs actionable intelligence to make roster decisions. Cares about player streaks, power-play time, and physical telemetry.
* **Pain Point:** Needs to compare multiple players simultaneously against a baseline.
* **UX Constraint:** Dense matrix tables, player headshots, and comparative Radar Plots (Player vs. League Average).

## 3. The Coach / Scout (Deep-Dive)
* **Goal:** Advanced tactical analysis. Wants to see spatial data, shooting tendencies, and expected goals (xG).
* **Pain Point:** Needs to filter by highly specific game states (e.g., 3rd period, down by 1 goal).
* **UX Constraint:** Rink-map SVG scatter plots, heatmaps, and complex spatial DAX filtering. Touch targets must allow for precise coordinate selection.
"""

    # --- FILE 4: SPRINT BOARD ---
    files_to_create['docs/SPRINT_BOARD.md'] = r"""# 🏃 Active Sprint Board

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
"""

    # --- FILE 5: PLANNING PROMPT ---
    files_to_create['docs/prompts/PLANNING.md'] = r"""# 📐 Power BI Planning Prompt (The Architect)

**Role:** Senior Data Architect.
**Objective:** Provide a structural plan before writing any M-Code or DAX.

**Phase 1: Ingestion & Mapping**
1. Analyze the provided `powerbi_codebase.txt`.
2. Identify the Fact and Dimension tables impacted by the request.

**Phase 2: Strategy**
Provide the plan.
* **Power Query (M):** Detail the extraction, transformation, and load steps. Address query folding and performance.
* **Data Modeling:** Define the relationships, cardinality (1:Many), and cross-filter direction.
* **DAX:** Outline the measure logic (Calculate, Filter, Variables).

**Phase 3: Anti-Regression**
* Will this break the Star Schema?
* Will this inflate VertiPaq memory?
* STOP and wait for approval.
"""

    # --- FILE 6: APPROVAL PROMPT ---
    files_to_create['docs/prompts/APPROVAL.md'] = r"""# ✅ Execution Prompt (The DAX Master)

**Decision:** I approve the plan. Proceed with Phase Execution.

**Strict Constraints:**
1. **The "Complete File" Rule:** You MUST provide the ENTIRE TMDL file or complete DAX measure from top to bottom. No placeholders.
2. **Strict Data Typing:** In Power Query, explicitly type every column (`Int64.Type`, `type text`). No implicit 'any'.
3. **DAX Formatting:** Use standard DAX formatting (variables on new lines, proper indentation) for readability.
4. **Deliverable:** Output the exact M-code or DAX required.
"""

    # --- FILE 7: FIX PROMPT ---
    files_to_create['docs/prompts/FIX.md'] = r"""# 🚑 Error Resolution Prompt (The Data Engineer)

**Role:** Senior Power BI SRE.
**Objective:** Restore model stability with ZERO collateral damage.

**INPUT:**
* **Error Message:** [PASTE POWER BI ERROR DIALOG OR DAX ERROR HERE]
* **Target Table/Measure:** [NAME OF FAILED ITEM]

**PROTOCOL:**
1. **Root Cause Analysis:** Why did the engine fail? (e.g., Circular dependency, text-to-number type mismatch, blank values in 1:Many relationship).
2. **Surgical Fix:** Provide the exact corrected, complete M-Code or DAX. Do not refactor unrelated logic.
3. **Verification:** Tell me what to check in the Model View to ensure the fix worked.
"""

    # 3. Write files to disk, swapping __FENCE__ for ```
    for relative_path, content in files_to_create.items():
        full_path = os.path.join(project_root, relative_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        safe_content = content.replace('__FENCE__', FENCE)
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(safe_content)
        print(f"✅ Created: {relative_path}")

    print("\n🚀 Documentation architecture generated successfully!")

if __name__ == "__main__":
    create_docs()