from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class Umpiregame(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], game_pk: str = None, zone_shift_x: float = None, zone_shift_z: float = None, calibration_error_pct: float = None) -> str:
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
    #metadata information
    def get_info() -> dict[str, Any]:
        pass
        #return result
        return {
            "type": "function",
            "function": {
                "name": "makeUmp",
                "description": "Persists umpire game model data to database.",
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
