# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require_tables


class GetGameDetails(Tool):
    """Get full game row by game_pk."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require_tables(data, ["games"])
        if err:
            return json.dumps({"error": err}, indent=2)
        game_pk = kwargs.get("game_pk")
        if not game_pk:
            return json.dumps({"error": "game_pk is required."}, indent=2)
        row = next((g for g in data["games"] if g.get("game_pk") == game_pk), None)
        return json.dumps(row or {"error": f"Game '{game_pk}' not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"get_game_details","description":"Returns the games row for a given game_pk.","parameters":{"type":"object","properties":{"game_pk":{"type":"integer"}},"required":["game_pk"]}}}
