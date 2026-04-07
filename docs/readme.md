# 🏒 NHL 2026: Advanced Telemetry & Analytics Platform

**NHL 2026** is a high-performance Power BI solution providing deep insights into NHL team performance and player telemetry. It combines live NHL Web API data with massive historical datasets using a sophisticated Lambda-style architecture.

## 🏗️ Technical Stack
* **Format:** Tabular Model Definition Language (TMDL)
* **Engine:** Power BI VertiPaq (In-Memory Columnar)
* **Logic:** DAX (Metrics) + M (API Consumption)
* **Data Sources:** NHL API (`v1/gamecenter`, `v1/edge`), Kaggle Historical Datasets

## 🧠 Architectural Pillars
* **Lambda Architecture (Y-Intersection):** Independent extraction of live and historical plays unified via DAX `UNION` for maximum efficiency.
* **Strict Star Schema:** 1-to-Many relationships flowing from Dimensions to Facts to ensure model stability.
* **Memory Efficiency:** "Auto Date/Time" disabled and early filtering (>= 2021 season) applied to large datasets to prevent RAM timeouts.
* **Explicit Data Typing:** Strict adherence to `Table.TransformColumnTypes` in M to prevent implicit conversion errors.

## 🗄️ Data Model Topology
The model follows a rigorous hierarchy designed for drill-through exploration:
* **DimGames:** Unified tracking for all game types.
* **DimTeams:** The digital rolodex for franchise data and standings.
* **DimPlayers:** The link between rosters and advanced telemetry facts.
* **FactPlayByPlay:** The unified event ledger for all on-ice actions.
* **FactEdge (Speeds/Bursts):** High-velocity telemetry for player speed and acceleration.

## 🗺️ NHL Analytics Product Roadmap

### 📅 Q2 2026: The Core Modules
| Status | ID | Epic Name | Persona Focus | Description |
| :--- | :--- | :--- | :--- | :--- |
| ✅ **Complete** | `EPIC-01` | **The Core Reporting Flow** | Casual Fan / Manager | Establish the Macro-to-Micro drill-through experience (League -> Team -> Player) using traditional box-score metrics. |
| 🟡 **Active** | `EPIC-02` | **The Fantasy Console (EDGE)** | Fantasy Manager | Deploy EDGE telemetry radar plots and speed scatter charts. |
| ⚪ Planned | `EPIC-03` | **The Coach's War Room** | Scout | Build the Expected Goals (xG) spatial engine using X/Y coordinates. |
| ⚪ Planned | `EPIC-04` | **Automated Deployment** | Admin | Migrate to Power BI Service with scheduled daily API refreshes. |

## 🚀 Getting Started
1.  Ensure you have **Power BI Desktop** installed with **Developer Mode** enabled.
2.  Open the `.pbip` file to load the TMDL-based model.
3.  Configure your local file paths for historical CSV data in the Power Query parameters.