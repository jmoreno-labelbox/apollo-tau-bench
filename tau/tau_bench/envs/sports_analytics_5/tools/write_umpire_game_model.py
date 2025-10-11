# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require_tables


class WriteUmpireGameModel(Tool):
    """Insert an umpire_game_models row."""
    @staticmethod
    def invoke(data, calibration_error_pct, confidence_interval, game_pk, umpire_id, zone_shift_x, zone_shift_z)->str:
        err = _require_tables(data, ["umpire_game_models"])
        if err:
            return json.dumps({"error": err}, indent=2)
        need = _check_required(kwargs, ["game_pk","umpire_id","zone_shift_x","zone_shift_z","calibration_error_pct","confidence_interval"])
        if need:
            return json.dumps({"error": need}, indent=2)
        rows = list(data.get("umpire_game_models", {}).values())
        new_id = _next_id(rows, "umpire_game_id")
        row = {
            "umpire_game_id": new_id,
            "game_pk": game_pk,
            "umpire_id": umpire_id,
            "zone_shift_x": zone_shift_x,
            "zone_shift_z": zone_shift_z,
            "calibration_error_pct": calibration_error_pct,
            "confidence_interval": confidence_interval
        }
        rows.append(row)
        return json.dumps({"umpire_game_id": new_id}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"write_umpire_game_model","description":"Creates umpire_game_models row for a game.","parameters":{"type":"object","properties":{"game_pk":{"type":"integer"},"umpire_id":{"type":"integer"},"zone_shift_x":{"type":"number"},"zone_shift_z":{"type":"number"},"calibration_error_pct":{"type":"number"},"confidence_interval":{"type":"number"}},"required":["game_pk","umpire_id","zone_shift_x","zone_shift_z","calibration_error_pct","confidence_interval"]}}}
