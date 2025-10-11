# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require_tables


class GetUmpireGameModel(Tool):
    """Fetch umpire_game_models row for a game."""
    @staticmethod
    def invoke(data, game_pk)->str:
        err = _require_tables(data, ["umpire_game_models"])
        if err:
            return json.dumps({"error": err}, indent=2)
        if game_pk is None:
            return json.dumps({"error":"game_pk is required."}, indent=2)
        row = next((u for u in data["umpire_game_models"] if u.get("game_pk")==game_pk), None)
        return json.dumps(row or {"error":"Not found."}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"get_umpire_game_model","description":"Returns the umpire model row for a game.","parameters":{"type":"object","properties":{"game_pk":{"type":"integer"}},"required":["game_pk"]}}}
