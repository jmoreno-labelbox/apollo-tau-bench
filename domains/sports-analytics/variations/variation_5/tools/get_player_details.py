from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class GetPlayerDetails(Tool):
    """Retrieve a player using player_id or full_name."""

    @staticmethod
    def invoke(data, player_id: str = None, full_name: str = None) -> str:
        err = _require_tables(data, ["players"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        pid = player_id
        name = full_name
        row = None
        if pid is not None:
            row = next((p for p in data["players"] if p.get("player_id") == pid), None)
        elif name:
            row = next((p for p in data["players"] if p.get("full_name") == name), None)
        else:
            payload = {"error": "Provide player_id or full_name."}
            out = json.dumps(payload, indent=2)
            return out
        payload = row or {"error": "Player not found."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetPlayerDetails",
                "description": "Fetch player by ID or exact full name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "player_id": {"type": "integer"},
                        "full_name": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
