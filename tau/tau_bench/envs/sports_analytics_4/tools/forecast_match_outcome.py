from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ForecastMatchOutcome(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], home_team_id: str = None, away_team_id: str = None, tags: Any = None) -> str:
        pass
        home_team = home_team_id
        away_team = away_team_id
        # Dummy deterministic model: the team with a higher average runs wins
        games = data.get("games", {}).values()

        def avg_runs(team):
            pass
            team_games = [
                g
                for g in games.values() if g.get("home_team_id") == team or g.get("away_team_id") == team
            ]
            # return result
            return sum(
                g.get("final_score", {}).values().get(str(team), 0) for g in team_games
            ) / max(len(team_games), 1)

        winner = home_team if avg_runs(home_team) >= avg_runs(away_team) else away_team
        payload = {"predicted_winner": winner}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        pass
        #return result
        return {
            "type": "function",
            "function": {
                "name": "forecastMatchOutcome",
                "description": "Predicts a match outcome between two teams using simple historical averages.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "home_team_id": {"type": "integer"},
                        "away_team_id": {"type": "integer"},
                    },
                    "required": ["home_team_id", "away_team_id"],
                },
            },
        }
