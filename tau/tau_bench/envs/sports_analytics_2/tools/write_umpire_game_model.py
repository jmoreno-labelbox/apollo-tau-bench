# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class WriteUmpireGameModel(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], calibration_error_pct, game_pk, zone_shift_x, zone_shift_z) -> str:
        models = data.setdefault("umpire_game_models", {})
        # Create the subsequent ID.
        next_id = str(len(models) + 1)
        models[next_id] = {
            "umpire_game_id": f"ump_{next_id}",
            "game_pk": game_pk,
            "zone_shift_x": zone_shift_x,
            "zone_shift_z": zone_shift_z,
            "calibration_error_pct": calibration_error_pct
        }
        return json.dumps({"status": "ok"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "write_umpire_game_model", "description": "Writes umpire game model data to database.", "parameters": {"type": "object", "properties": {"game_pk": {"type": "string"}, "zone_shift_x": {"type": "number"}, "zone_shift_z": {"type": "number"}, "calibration_error_pct": {"type": "number"}}, "required": ["game_pk"]}}}
