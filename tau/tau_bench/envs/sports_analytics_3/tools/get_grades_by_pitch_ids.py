# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetGradesByPitchIds(Tool):
    """
    Fetch execution grade records for a list of pitch IDs.
    Returns all matching rows sorted deterministically by pitch_id ASC, grade_id ASC.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        pitch_ids = kwargs.get("pitch_ids")

        # 1) Validate
        if not isinstance(pitch_ids, list) or len(pitch_ids) == 0:
            return json.dumps({"error": "Missing required field: pitch_ids (non-empty list of integers)"}, indent=2)

        # 2) Get DB
        grades: List[Dict[str, Any]] = list(data.get("pitch_execution_grades", {}).values())

        # 3) Collect matches
        id_set = set(pitch_ids)
        matches = [rec for rec in grades if rec.get("pitch_id") in id_set]

        if not matches:
            return json.dumps({"No grades found": f"No grades found for pitch_ids {pitch_ids}"}, indent=2)

        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_grades_by_pitch_ids",
                "description": "Fetch execution grade records for the given list of pitch IDs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pitch_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "List of pitch IDs to retrieve grades for."
                        }
                    },
                    "required": ["pitch_ids"]
                }
            }
        }
