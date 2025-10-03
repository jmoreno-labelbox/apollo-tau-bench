from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class GetUmpireGameModel(Tool):
    """Retrieve the umpire_game_models entry for a game."""

    @staticmethod
    def invoke(data, game_pk=None) -> str:
        err = _require_tables(data, ["umpire_game_models"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        if game_pk is None:
            payload = {"error": "game_pk is required."}
            out = json.dumps(payload, indent=2)
            return out
        row = next(
            (u for u in data["umpire_game_models"] if u.get("game_pk") == game_pk), None
        )
        payload = row or {"error": "Not found."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "getUmpireGameModel",
                "description": "Returns the umpire model row for a game.",
                "parameters": {
                    "type": "object",
                    "properties": {"game_pk": {"type": "integer"}},
                    "required": ["game_pk"],
                },
            },
        }
