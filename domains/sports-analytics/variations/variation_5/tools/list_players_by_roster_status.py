from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class ListPlayersByRosterStatus(Tool):
    """Retrieve players based on specified roster_status (e.g., 'Active', 'IL-15')."""

    @staticmethod
    def invoke(data, roster_status: str = None) -> str:
        pass
        err = _require_tables(data, ["players"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        if not roster_status:
            payload = {"error": "roster_status is required."}
            out = json.dumps(payload, indent=2)
            return out
        rows = [p for p in data["players"] if p.get("roster_status") == roster_status]
        payload = rows
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "listPlayersByRosterStatus",
                "description": "Returns players matching a specific roster_status.",
                "parameters": {
                    "type": "object",
                    "properties": {"roster_status": {"type": "string"}},
                    "required": ["roster_status"],
                },
            },
        }
