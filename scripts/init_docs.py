import os

def sync_docs():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, '..'))
    
    FENCE = chr(96) * 3
    files_to_update = {}

    # --- FILE 1: SPRINT_BOARD.md ---
    files_to_update['docs/SPRINT_BOARD.md'] = r"""# 🏃 Active Sprint Board

**Current Phase:** Sprint 2.0 (Advanced Analytics & EDGE)

## ✅ Completed Sprints
- [x] **Sprint 0.1 - 0.3:** Data plumbing, Lambda architecture, and PK hardening.
- [x] **Sprint 1.0: The Core Reporting Flow.** - [x] PROJ-01: Standings Matrix
  - [x] PROJ-02: League Dashboard
  - [x] PROJ-03: Team Report (Drill-through base)
  - [x] PROJ-04: Player Scorecard (Target page)

## 🟡 Sprint 2.0: Advanced Analytics (Active)
- [ ] **PROJ-05: The EDGE Radar Plot.** Re-integrate burst telemetry DAX measures into the Player Scorecard.
- [ ] **PROJ-06: Spatial Rink Mapping.** Configure the custom SVG visual to plot `X_Coord` and `Y_Coord` from `FactPlayByPlay`.

## 🧊 Product Backlog (Sprint 3.0)
- [ ] **PROJ-07:** Expected Goals (xG) Distance DAX Model.
- [ ] **PROJ-08:** Trade Target Scatter Plot (Speed vs. Volume).
"""

    # --- FILE 2: ROADMAP.md ---
    files_to_update['docs/ROADMAP.md'] = r"""# 🗺️ NHL Analytics Product Roadmap

## 📅 Q2 2026: The Core Modules
| Status | ID | Epic Name | Persona Focus | Description |
| :--- | :--- | :--- | :--- | :--- |
| ✅ **Complete** | `EPIC-01` | **The Core Reporting Flow** | Casual Fan / Manager | Establish the Macro-to-Micro drill-through experience (League -> Team -> Player) using traditional box-score metrics. |
| 🟡 **Active** | `EPIC-02` | **The Fantasy Console (EDGE)** | Fantasy Manager | Deploy EDGE telemetry radar plots and speed scatter charts. |
| ⚪ Planned | `EPIC-03` | **The Coach's War Room** | Scout | Build the Expected Goals (xG) spatial engine using X/Y coordinates. |
| ⚪ Planned | `EPIC-04` | **Automated Deployment** | Admin | Migrate to Power BI Service with scheduled daily API refreshes. |
"""

    for relative_path, content in files_to_update.items():
        full_path = os.path.join(project_root, relative_path)
        if os.path.exists(full_path):
            safe_content = content.replace('__FENCE__', FENCE)
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(safe_content)
            print(f"✅ Synced: {relative_path}")

    print("\n🚀 Post-Sprint Audit complete. Sprint 1.0 is officially closed.")

if __name__ == "__main__":
    sync_docs()