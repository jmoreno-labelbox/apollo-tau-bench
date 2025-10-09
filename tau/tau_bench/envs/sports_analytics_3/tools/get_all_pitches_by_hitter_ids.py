from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetAllPitchesByHitterIds(Tool):
    """Retrieve all pitches encountered by any hitter in the supplied list of hitter_ids."""

    @staticmethod
    def invoke(data: dict[str, Any], hitter_ids: list[int] = None) -> str:
        #1) Confirm validity
        if not isinstance(hitter_ids, list) or len(hitter_ids) == 0:
            payload = {
                    "error": "Missing required field: hitter_ids (non-empty list of integers)"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #2) Retrieve DB
        pitches: list[dict[str, Any]] = data.get("pitches", {}).values()

        #3) Apply filter
        id_set = set(hitter_ids)
        matches = [p for p in pitches.values() if p.get("hitter_id") in id_set]
        if not matches:
            payload = {"error": f"No pitches found for hitter_ids {hitter_ids}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #4) Order deterministically: game_pk, at_bat_index, pitch_number, pitch_id (ASC)
        matches.sort(
            key=lambda p: (
                int(p.get("game_pk", 0)),
                int(p.get("at_bat_index", 0)),
                int(p.get("pitch_number", 0)),
                int(p.get("pitch_id", 0)),
            )
        )
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAllPitchesByHitterIds",
                "description": "Fetch all pitches where hitter_id is in the provided list. Returns a list of pitch records.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "hitter_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "Non-empty list of hitter IDs.",
                        }
                    },
                    "required": ["hitter_ids"],
                },
            },
        }
