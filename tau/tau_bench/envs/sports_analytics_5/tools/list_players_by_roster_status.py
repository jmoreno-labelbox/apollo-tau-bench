# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require_tables


class ListPlayersByRosterStatus(Tool):
    """List players with a given roster_status (e.g., 'Active', 'IL-15')."""
    @staticmethod
    def invoke(data, **kwargs)->str:
        err = _require_tables(data, ["players"])
        if err:
            return json.dumps({"error": err}, indent=2)
        status = kwargs.get("roster_status")
        if not status:
            return json.dumps({"error":"roster_status is required."}, indent=2)
        rows = [p for p in data["players"] if p.get("roster_status")==status]
        return json.dumps(rows, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"list_players_by_roster_status","description":"Returns players matching a specific roster_status.","parameters":{"type":"object","properties":{"roster_status":{"type":"string"}},"required":["roster_status"]}}}
