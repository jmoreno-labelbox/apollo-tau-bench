from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class ListGamesByStatus(Tool):
    """Retrieve games based on game_status filter."""

    @staticmethod
    def invoke(data, game_status: str = None) -> str:
        err = _require_tables(data, ["games"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        if not game_status:
            payload = {"error": "game_status is required."}
            out = json.dumps(payload, indent=2)
            return out
        rows = [g for g in data["games"] if (g.get("game_status") == game_status)]
        payload = rows
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "listGamesByStatus",
                "description": "Lists games by exact game_status (e.g., 'Scheduled','Final','Cancelled').",
                "parameters": {
                    "type": "object",
                    "properties": {"game_status": {"type": "string"}},
                    "required": ["game_status"],
                },
            },
        }
