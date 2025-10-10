# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require_tables


class ListGamesByStatus(Tool):
    """List games filtered by game_status."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        err = _require_tables(data, ["games"])
        if err:
            return json.dumps({"error": err}, indent=2)
        status = kwargs.get("game_status")
        if not status:
            return json.dumps({"error": "game_status is required."}, indent=2)
        rows = [g for g in data["games"] if (g.get("game_status") == status)]
        return json.dumps(rows, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"list_games_by_status","description":"Lists games by exact game_status (e.g., 'Scheduled','Final','Cancelled').","parameters":{"type":"object","properties":{"game_status":{"type":"string"}},"required":["game_status"]}}}
