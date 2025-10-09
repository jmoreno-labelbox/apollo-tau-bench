from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FetchBatchGameData(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        windows = kwargs.get("windows", [])
        batch_results = {}

        #Retrieve actual data from JSON files
        pitches = data.get("pitches", {}).values()
        games = data.get("games", {}).values()
        players = data.get("players", {}).values()

        for window in windows:
            if "PA" in window:  #Window for plate appearances
                count = int(window.replace("PA", ""))
                #Limit pitch filtering based on count
                filtered_pitches = pitches[:count] if len(pitches) >= count else pitches
                batch_results[window] = {
                    "total_records": len(filtered_pitches),
                    "avg_exit_velocity": sum(
                        p.get("exit_velocity", 0)
                        for p in filtered_pitches
                        if p.get("exit_velocity")
                    )
                    / max(
                        len([p for p in filtered_pitches.values() if p.get("exit_velocity")]), 1
                    ),
                    "pitch_types": list(
                        {
                            p.get("pitch_type")
                            for p in filtered_pitches
                            if p.get("pitch_type")
                        }
                    ),
                    "data_quality": "good",
                }
            elif "games" in window:  #Window for games
                count_str = window.replace("_games", "").replace("last_", "")
                if count_str == "full_season":
                    filtered_games = games
                else:
                    count = int(count_str)
                    filtered_games = games[-count:] if len(games) >= count else games
                batch_results[window] = {
                    "total_games": len(filtered_games),
                    "game_pks": [g.get("game_pk") for g in filtered_games],
                    "teams_involved": list(
                        set(
                            [g.get("home_team_id") for g in filtered_games]
                            + [g.get("away_team_id") for g in filtered_games]
                        )
                    ),
                    "data_quality": "good",
                }
            else:  #Additional contexts
                batch_results[window] = {
                    "data_available": len(pitches) > 0,
                    "records_count": len(pitches),
                    "players_count": len(players),
                    "data_quality": "good",
                }
        payload = {
                "batch_id": "batch_" + "_".join(windows),
                "windows_processed": len(windows),
                "results": batch_results,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchBatchGameData",
                "description": "Fetches game data across multiple time windows or contexts for batch analysis.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "windows": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of time windows or contexts to fetch data for (e.g., ['10PA', '20PA', '50PA'] or ['pre_trade', 'post_trade'])",
                        }
                    },
                    "required": ["windows"],
                },
            },
        }
