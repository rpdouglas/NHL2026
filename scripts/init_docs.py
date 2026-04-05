import os

def update_planning_docs():
    # 1. Setup paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, '..'))
    
    # 2. Protection variable for markdown code blocks
    FENCE = chr(96) * 3
    files_to_create = {}

    # --- FILE 1: ROADMAP.md ---
    files_to_create['docs/ROADMAP.md'] = r"""# 🗺️ NHL Analytics Product Roadmap

## 📅 Q2 2026: The Core Modules
| Status | ID | Epic Name | Persona Focus | Description |
| :--- | :--- | :--- | :--- | :--- |
| 🟡 **Active** | `EPIC-01` | **The Visual Foundation** | All | Establish base visuals, SVG mapping, and core DAX metrics. |
| ⚪ Planned | `EPIC-02` | **The Fantasy Console** | Manager | Deploy EDGE telemetry radar plots and value scatter charts. |
| ⚪ Planned | `EPIC-03` | **The Coach's War Room** | Scout | Build the Expected Goals (xG) spatial engine using X/Y coordinates. |
| ⚪ Planned | `EPIC-04` | **Automated Deployment** | Admin | Migrate to Power BI Service with scheduled daily API refreshes. |
"""

    # --- FILE 2: SPRINT_BOARD.md ---
    files_to_create['docs/SPRINT_BOARD.md'] = r"""# 🏃 Active Sprint Board

**Current Phase:** Sprint 1.0 (The Visual Foundation)

## ✅ Completed Sprints
- [x] **Sprint 0.1:** Core API connections established (Plays, Teams, Players, EDGE).
- [x] **Sprint 0.2:** Lambda Architecture deployed (DAX UNION).
- [x] **Sprint 0.3:** Schema hardening, PK uniqueness, and 2025-2026 season rollover.

## 🟡 Sprint 1.0: The Visual Foundation (Active)
- [ ] **PROJ-01:** The Standings Matrix. Build a hierarchical matrix visual (Conference -> Division -> Team) using the `DimTeams` table.
- [ ] **PROJ-02:** The EDGE Radar Plot. Build DAX measures calculating Player Speed/Bursts vs. League Average.
- [ ] **PROJ-03:** Spatial Rink Mapping. Configure the custom SVG visual to plot `X_Coord` and `Y_Coord` from `FactPlayByPlay`.

## 🧊 Product Backlog
- [ ] **PROJ-04:** Expected Goals (xG) DAX Model (Distance from net calculation).
- [ ] **PROJ-05:** Trade Target Scatter Plot (Speed vs. Volume).
"""

    # 3. Write the files safely to disk
    for relative_path, content in files_to_create.items():
        full_path = os.path.join(project_root, relative_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        safe_content = content.replace('__FENCE__', FENCE)
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(safe_content)
        print(f"✅ Updated: {relative_path}")

    print("\n🚀 Project Roadmap and Sprint Board updated successfully!")

if __name__ == "__main__":
    update_planning_docs()