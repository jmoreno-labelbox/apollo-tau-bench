# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CompareTeamStats(Tool):
    @staticmethod
        # main invoke function
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        team_a = kwargs.get("team_a")
        team_b = kwargs.get("team_b")
        games = data.get("games", [])
        def avg_runs(team):
            team_games = [g for g in games if g.get("home_team_id") == team or g.get("away_team_id") == team]
        # return result
            return sum(g.get("final_score", {}).get(str(team), 0) for g in team_games) / max(len(team_games), 1)
        # return result
        return json.dumps({
            "team_a_avg_runs": avg_runs(team_a),
            "team_b_avg_runs": avg_runs(team_b)
        }, indent=2)

    @staticmethod
        # info metadata
    def get_info() -> Dict[str, Any]:
        # return result
        return {
            "type": "function",
            "function": {
                "name": "compare_team_stats",
                "description": "Compares two teams based on average runs scored across available games.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_a": {"type": "integer"},
                        "team_b": {"type": "integer"}
                    },
                    "required": ["team_a", "team_b"]
                }
            }
        }
