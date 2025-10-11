# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AllGames(Tool):
    @staticmethod
        # primary execution function
    def invoke(data: Dict[str, Any], windows = []) -> str:
        batch_results = {}

        # Retrieve actual data from JSON files.
        pitches = data.get("pitches", [])
        games = data.get("games", [])
        players = data.get("players", [])

        for window in windows:
            if "PA" in window:  # Window for plate appearances
                count = int(window.replace("PA", ""))
                # Limit the pitches by count filter.
                filtered_pitches = pitches[:count] if len(pitches) >= count else pitches
                batch_results[window] = {
                    "total_records": len(filtered_pitches),
                    "avg_exit_velocity": sum(p.get("exit_velocity", 0) for p in filtered_pitches if p.get("exit_velocity")) / max(len([p for p in filtered_pitches if p.get("exit_velocity")]), 1),
                    "pitch_types": list(set(p.get("pitch_type") for p in filtered_pitches if p.get("pitch_type"))),
                    "data_quality": "good"
                }
            elif "games" in window:  # Game interface
                count_str = window.replace("_games", "").replace("last_", "")
                if count_str == "full_season":
                    filtered_games = games
                else:
                    count = int(count_str)
                    filtered_games = games[-count:] if len(games) >= count else games
                batch_results[window] = {
                    "total_games": len(filtered_games),
                    "game_pks": [g.get("game_pk") for g in filtered_games],
                    "teams_involved": list(set([g.get("home_team_id") for g in filtered_games] + [g.get("away_team_id") for g in filtered_games])),
                    "data_quality": "good"
                }
            else:  # Alternative scenarios
                batch_results[window] = {
                    "data_available": len(pitches) > 0,
                    "records_count": len(pitches),
                    "players_count": len(players),
                    "data_quality": "good"
                }

        # return outcome
        return json.dumps({
            "batch_id": "batch_" + "_".join(windows),
            "windows_processed": len(windows),
            "results": batch_results
        }, indent=2)

    @staticmethod
        # metadata information
    def get_info() -> Dict[str, Any]:
        # return outcome
        return {
            "type": "function",
            "function": {
                "name": "getData",
                "description": "Collects game data across multiple time windows or contexts for batch analysis.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "windows": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of time windows or contexts to fetch data for (e.g., ['10PA', '20PA', '50PA'] or ['pre_trade', 'post_trade'])"
                        }
                    },
                    "required": ["windows"]
                }
            }
        }
