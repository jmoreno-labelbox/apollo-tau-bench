from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class WriteUmpireGameModel(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        game_pk = kwargs.get("game_pk")
        zone_shift_x = kwargs.get("zone_shift_x")
        zone_shift_z = kwargs.get("zone_shift_z")
        calibration_error_pct = kwargs.get("calibration_error_pct")
        data.setdefault("umpire_game_models", []).append(
            {
                "umpire_game_id": f"ump_{len(data.get('umpire_game_models', {}))+1}",
                "game_pk": game_pk,
                "zone_shift_x": zone_shift_x,
                "zone_shift_z": zone_shift_z,
                "calibration_error_pct": calibration_error_pct,
            }
        )
        payload = {"status": "ok"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "WriteUmpireGameModel",
                "description": "Writes umpire game model data to database.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {"type": "string"},
                        "zone_shift_x": {"type": "number"},
                        "zone_shift_z": {"type": "number"},
                        "calibration_error_pct": {"type": "number"},
                    },
                    "required": ["game_pk"],
                },
            },
        }
