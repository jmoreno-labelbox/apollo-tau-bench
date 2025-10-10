# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require_tables


class GetPlayerDetails(Tool):
    """Get a player by player_id or full_name."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["players"])
        if err:
            return json.dumps({"error": err}, indent=2)
        pid = kwargs.get("player_id")
        name = kwargs.get("full_name")
        row = None
        if pid is not None:
            row = next((p for p in data["players"] if p.get("player_id")==pid), None)
        elif name:
            row = next((p for p in data["players"] if p.get("full_name")==name), None)
        else:
            return json.dumps({"error":"Provide player_id or full_name."}, indent=2)
        return json.dumps(row or {"error":"Player not found."}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"get_player_details","description":"Fetch player by ID or exact full name.","parameters":{"type":"object","properties":{"player_id":{"type":"integer"},"full_name":{"type":"string"}},"required":[]}}}
