# 📏 DAX Measure Dictionary

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
