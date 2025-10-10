# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class Umpiregame(Tool):
    @staticmethod
        # primary execution method
    def invoke(data: Dict[str, Any], calibration_error_pct, game_pk, zone_shift_x, zone_shift_z) -> str:
        data.setdefault("umpire_game_models", []).append({
            "umpire_game_id": f"ump_{len(data.get('umpire_game_models', []))+1}",
            "game_pk": game_pk,
            "zone_shift_x": zone_shift_x,
            "zone_shift_z": zone_shift_z,
            "calibration_error_pct": calibration_error_pct
        })
        # output result
        return json.dumps({"status": "ok"}, indent=2)

    @staticmethod
        # metadata information
    def get_info() -> Dict[str, Any]:
        # return output
        return {"type": "function", "function": {"name": "makeUmp", "description": "Persists umpire game model data to database.", "parameters": {"type": "object", "properties": {"game_pk": {"type": "string"}, "zone_shift_x": {"type": "number"}, "zone_shift_z": {"type": "number"}, "calibration_error_pct": {"type": "number"}}, "required": ["game_pk"]}}}
