from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetAllPitchesByPitcherIds(Tool):
    """Retrieve all pitches delivered by any pitcher in the supplied list of pitcher_ids."""

    @staticmethod
    def invoke(data: dict[str, Any], pitcher_ids: list[int] = None) -> str:
        #1) Confirm validity
        if not isinstance(pitcher_ids, list) or len(pitcher_ids) == 0:
            payload = {
                    "error": "Missing required field: pitcher_ids (non-empty list of integers)"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #2) Retrieve DB
        pitches: list[dict[str, Any]] = data.get("pitches", [])

        #3) Apply filter
        id_set = set(pitcher_ids)
        matches = [p for p in pitches if p.get("pitcher_id") in id_set]
        if not matches:
            payload = {"error": f"No pitches found for pitcher_ids {pitcher_ids}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #4) Order deterministically: game_pk, at_bat_index, pitch_number, pitch_id (ASC)
        #matches.sort(
        #key=lambda p: (
        #int(p.get("game_pk", 0)),
        #int(p.get("at_bat_index", 0)),
        #int(p.get("pitch_number", 0)),
        #int(p.get("pitch_id", 0)),
        #)
        #)
        pitch_ids = [int(p.get("pitch_id", 0)) for p in matches]
        #Remove duplicates while maintaining order, just in case
        pitch_ids = list(dict.fromkeys(pitch_ids))

        payload = {
            "pitch_ids": pitch_ids,
            "pitches": matches,
        }
        payload = payload
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAllPitchesByPitcherIds",
                "description": "Fetch all pitches where pitcher_id is in pitcher_ids. Returns a list of pitch records.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pitcher_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "Non-empty list of pitcher IDs.",
                        }
                    },
                    "required": ["pitcher_ids"],
                },
            },
        }
