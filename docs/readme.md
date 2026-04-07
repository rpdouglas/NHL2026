# 🏒 NHL 2026: Advanced Telemetry & Analytics Platform

**NHL 2026** is a high-performance Power BI solution designed to provide deep insights into NHL team performance and player telemetry. By combining live NHL Web API data with massive historical datasets, it offers a "Lambda-style" architecture for seamless data unification.

## 🏗️ Technical Stack
* **Format:** Tabular Model Definition Language (TMDL)
* **Engine:** Power BI VertiPaq (In-Memory Columnar)
* **Logic:** DAX (Metrics) + M (Power Query API Consumption)
* **Data Sources:** Live NHL API (`v1/gamecenter`, `v1/edge`), Kaggle Historical Datasets

## 🧠 Architectural Pillars
* **Lambda Architecture (Y-Intersection):** Live and historical plays are extracted independently and merged via DAX `UNION` for maximum performance.
* **Strict Star Schema:** Fact tables never connect to other Fact tables; all filters flow from Dimensions.
* **API Governance:** Implements implicit rate limiting (300ms delays) and record sanitization to ensure robust API ingestion.
* **Performance First:** "Auto Date/Time" is disabled, and large files utilize Early Filtering (>= 2021) to minimize RAM footprint.

## 🗄️ Data Model
The model centers around three core dimension tables:
* **DimGames:** Unified game ledger (Live + Historical).
* **DimTeams:** Franchise details, conference/division hierarchy, and current standings.
* **DimPlayers:** Roster management and player-specific bio data.

These filter specialized Fact tables including **FactPlayByPlay**, **FactEdgeSkatingSpeeds**, and **FactEdgeBurstDetails**.

## 📏 Key Metrics
| Category | Measures |
| :--- | :--- |
| **Team Performance** | Points, Goal Differential, Current Streak, Wins/Losses |
| **Player Stats** | Goals, Assists, Total Points, Games Played |
| **EDGE Telemetry** | Max Speed (mph), League Avg Speed, Bursts > 22mph |

## 🚀 Getting Started
1.  Ensure you have **Power BI Desktop** (latest version) and **Developer Mode** enabled.
2.  The project is stored in TMDL format. Open the `.pbip` file to load the model.
3.  Historical data requires `game.csv` and `game_plays.csv` to be located in the paths specified in the Power Query parameters.