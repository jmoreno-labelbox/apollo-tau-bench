from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CompareTeamStats(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], team_a: str = None, team_b: str = None) -> str:
        pass
        games = data.get("games", [])

        def avg_runs(team):
            pass
            team_games = [
                g
                for g in games
                if g.get("home_team_id") == team or g.get("away_team_id") == team
            ]
            #return result
            return sum(
                g.get("final_score", {}).get(str(team), 0) for g in team_games
            ) / max(len(team_games), 1)
        payload = {"team_a_avg_runs": avg_runs(team_a), "team_b_avg_runs": avg_runs(team_b)}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        pass
        #return result
        return {
            "type": "function",
            "function": {
                "name": "compareTeamStats",
                "description": "Compares two teams based on average runs scored across available games.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_a": {"type": "integer"},
                        "team_b": {"type": "integer"},
                    },
                    "required": ["team_a", "team_b"],
                },
            },
        }
