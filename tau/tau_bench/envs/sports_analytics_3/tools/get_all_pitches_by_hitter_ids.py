# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAllPitchesByHitterIds(Tool):
    """Fetch all pitches faced by any hitter in the provided list of hitter_ids."""

    @staticmethod
    def invoke(data: Dict[str, Any], hitter_ids) -> str:

        # 1) Verify
        if not isinstance(hitter_ids, list) or len(hitter_ids) == 0:
            return json.dumps(
                {"error": "Missing required field: hitter_ids (non-empty list of integers)"},
                indent=2
            )

        # Retrieve database
        pitches: List[Dict[str, Any]] = list(data.get("pitches", {}).values())

        # 3) Selection
        id_set = set(hitter_ids)
        matches = [p for p in pitches if p.get("hitter_id") in id_set]
        if not matches:
            return json.dumps({"error": f"No pitches found for hitter_ids {hitter_ids}"}, indent=2)

        # 4) Fixed sequence: game_pk, at_bat_index, pitch_number, pitch_id (ascending)
        matches.sort(
            key=lambda p: (
                int(p.get("game_pk", 0)),
                int(p.get("at_bat_index", 0)),
                int(p.get("pitch_number", 0)),
                int(p.get("pitch_id", 0)),
            )
        )

        # 5) Output a list containing only pitch records.
        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_pitches_by_hitter_ids",
                "description": "Fetch all pitches where hitter_id is in the provided list. Returns a list of pitch records.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "hitter_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "Non-empty list of hitter IDs."
                        }
                    },
                    "required": ["hitter_ids"]
                }
            }
        }
