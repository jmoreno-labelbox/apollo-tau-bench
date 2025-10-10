# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAllPitchesByPitcherIds(Tool):
    """Fetch all pitches thrown by any pitcher in the provided list of pitcher_ids."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pitcher_ids = kwargs.get("pitcher_ids")

        # 1) Validate
        if not isinstance(pitcher_ids, list) or len(pitcher_ids) == 0:
            return json.dumps(
                {"error": "Missing required field: pitcher_ids (non-empty list of integers)"},
                indent=2
            )

        # 2) Get DB
        pitches: List[Dict[str, Any]] = data.get("pitches", [])

        # 3) Filter
        id_set = set(pitcher_ids)
        matches = [p for p in pitches if p.get("pitcher_id") in id_set]
        if not matches:
            return json.dumps({"error": f"No pitches found for pitcher_ids {pitcher_ids}"}, indent=2)

        # 4) Deterministic order: game_pk, at_bat_index, pitch_number, pitch_id (ASC)
        # matches.sort(
        #     key=lambda p: (
        #         int(p.get("game_pk", 0)),
        #         int(p.get("at_bat_index", 0)),
        #         int(p.get("pitch_number", 0)),
        #         int(p.get("pitch_id", 0)),
        #     )
        # )
        pitch_ids = [int(p.get("pitch_id", 0)) for p in matches]
        # Deduplicate while preserving order, just in case
        pitch_ids = list(dict.fromkeys(pitch_ids))

        payload = {
            "pitch_ids": pitch_ids,
            "pitches": matches,
        }

        # 5) Return list of pitch records only
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
