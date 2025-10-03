from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class GetOpponentForTeamInGame(Tool):
    """Using a team_id and a game_pk, return the opposing team_id."""

    @staticmethod
    def invoke(data, game_pk, team_id: Any = None) -> str:
        err = _require_tables(data, ["games"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        need = _check_required({"game_pk": game_pk, "team_id": team_id}, ["game_pk", "team_id"])
        if need:
            payload = {"error": need}
            out = json.dumps(payload, indent=2)
            return out
        g = next(
            (g for g in data["games"] if g.get("game_pk") == game_pk), None
        )
        if not g:
            payload = {"error": "Game not found."}
            out = json.dumps(payload, indent=2)
            return out
        team = team_id
        if g.get("home_team_id") == team:
            opp = g.get("away_team_id")
        elif g.get("away_team_id") == team:
            opp = g.get("home_team_id")
        else:
            payload = {"error": "team_id not in specified game."}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"opponent_team_id": opp}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetOpponentForTeamInGame",
                "description": "Finds the opponent team_id for a team in a given game.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {"type": "integer"},
                        "team_id": {"type": "integer"},
                    },
                    "required": ["game_pk", "team_id"],
                },
            },
        }
