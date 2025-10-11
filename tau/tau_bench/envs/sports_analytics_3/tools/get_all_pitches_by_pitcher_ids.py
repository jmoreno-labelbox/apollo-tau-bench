# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAllPitchesByPitcherIds(Tool):
    """Fetch all pitches thrown by any pitcher in the provided list of pitcher_ids."""

    @staticmethod
    def invoke(data: Dict[str, Any], pitcher_ids) -> str:

        # 1) Confirm validity
        if not isinstance(pitcher_ids, list) or len(pitcher_ids) == 0:
            return json.dumps(
                {"error": "Missing required field: pitcher_ids (non-empty list of integers)"},
                indent=2
            )

        # Retrieve database
        pitches: List[Dict[str, Any]] = list(data.get("pitches", {}).values())

        # 3) Selection
        id_set = set(pitcher_ids)
        matches = [p for p in pitches if p.get("pitcher_id") in id_set]
        if not matches:
            return json.dumps({"error": f"No pitches found for pitcher_ids {pitcher_ids}"}, indent=2)

        # 4) Fixed order: game_pk, at_bat_index, pitch_number, pitch_id (ascending)
        # matches.order(
        #     key=lambda p: (
        # int(p.get("game_pk", default=0)),
        # int(p.get("at_bat_index", default=0)),
        # int(p.get("pitch_number", default=0)),
        # int(p.get("pitch_id", default=0)),
        #     )
        # )
        pitch_ids = [int(p.get("pitch_id", 0)) for p in matches]
        # Remove duplicates while maintaining the original sequence, as a precaution.
        pitch_ids = list(dict.fromkeys(pitch_ids))

        payload = {
            "pitch_ids": pitch_ids,
            "pitches": matches,
        }

        # 5) Retrieve a list containing only pitch records.
        return json.dumps(payload, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_pitches_by_pitcher_ids",
                "description": "Fetch all pitches where pitcher_id is in pitcher_ids. Returns a list of pitch records.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pitcher_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "Non-empty list of pitcher IDs."
                        }
                    },
                    "required": ["pitcher_ids"]
                }
            }
        }
