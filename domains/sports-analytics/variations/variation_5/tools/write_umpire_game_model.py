from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class WriteUmpireGameModel(Tool):
    """Add an entry for umpire_game_models."""

    @staticmethod
    def invoke(
        data,
        game_pk=None,
        umpire_id=None,
        zone_shift_x=None,
        zone_shift_z=None,
        calibration_error_pct=None,
        confidence_interval=None,
    ) -> str:
        err = _require_tables(data, ["umpire_game_models"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        need = _check_required(
            {
                "game_pk": game_pk,
                "umpire_id": umpire_id,
                "zone_shift_x": zone_shift_x,
                "zone_shift_z": zone_shift_z,
                "calibration_error_pct": calibration_error_pct,
                "confidence_interval": confidence_interval,
            },
            [
                "game_pk",
                "umpire_id",
                "zone_shift_x",
                "zone_shift_z",
                "calibration_error_pct",
                "confidence_interval",
            ],
        )
        if need:
            payload = {"error": need}
            out = json.dumps(payload, indent=2)
            return out
        rows = data["umpire_game_models"]
        new_id = _next_id(rows, "umpire_game_id")
        row = {
            "umpire_game_id": new_id,
            "game_pk": game_pk,
            "umpire_id": umpire_id,
            "zone_shift_x": zone_shift_x,
            "zone_shift_z": zone_shift_z,
            "calibration_error_pct": calibration_error_pct,
            "confidence_interval": confidence_interval,
        }
        rows.append(row)
        payload = {"umpire_game_id": new_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "WriteUmpireGameModel",
                "description": "Creates umpire_game_models row for a game.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {"type": "integer"},
                        "umpire_id": {"type": "integer"},
                        "zone_shift_x": {"type": "number"},
                        "zone_shift_z": {"type": "number"},
                        "calibration_error_pct": {"type": "number"},
                        "confidence_interval": {"type": "number"},
                    },
                    "required": [
                        "game_pk",
                        "umpire_id",
                        "zone_shift_x",
                        "zone_shift_z",
                        "calibration_error_pct",
                        "confidence_interval",
                    ],
                },
            },
        }
