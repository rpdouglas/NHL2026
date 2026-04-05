# 🧠 NHL 2026: Platform Context

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
