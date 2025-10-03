from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class GetGameDetails(Tool):
    """Retrieve complete game row using game_pk."""

    @staticmethod
    def invoke(data: dict[str, Any], game_pk: str = None) -> str:
        err = _require_tables(data, ["games"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        if not game_pk:
            payload = {"error": "game_pk is required."}
            out = json.dumps(payload, indent=2)
            return out
        row = next((g for g in data["games"] if g.get("game_pk") == game_pk), None)
        payload = row or {"error": f"Game '{game_pk}' not found."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetGameDetails",
                "description": "Returns the games row for a given game_pk.",
                "parameters": {
                    "type": "object",
                    "properties": {"game_pk": {"type": "integer"}},
                    "required": ["game_pk"],
                },
            },
        }
