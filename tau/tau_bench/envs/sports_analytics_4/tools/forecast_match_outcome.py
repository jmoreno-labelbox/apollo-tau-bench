# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ForecastMatchOutcome(Tool):
    @staticmethod
        # main invoke function
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        home_team = kwargs.get("home_team_id")
        away_team = kwargs.get("away_team_id")
        # Dummy deterministic model: higher average runs wins
        games = data.get("games", [])
        def avg_runs(team):
            team_games = [g for g in games if g.get("home_team_id") == team or g.get("away_team_id") == team]
        # return result
            return sum(g.get("final_score", {}).get(str(team), 0) for g in team_games) / max(len(team_games), 1)
        winner = home_team if avg_runs(home_team) >= avg_runs(away_team) else away_team
        # return result
        return json.dumps({"predicted_winner": winner}, indent=2)

    @staticmethod
        # info metadata
    def get_info() -> Dict[str, Any]:
        # return result
        return {
            "type": "function",
            "function": {
                "name": "forecast_match_outcome",
                "description": "Predicts a match outcome between two teams using simple historical averages.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "home_team_id": {"type": "integer"},
                        "away_team_id": {"type": "integer"}
                    },
                    "required": ["home_team_id", "away_team_id"]
                }
            }
        }
