# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetGradeByPitchId(Tool):
    """Fetch the execution grade record for a single pitch_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], pitch_id) -> str:

        # 1) Verify
        if pitch_id is None:
            return json.dumps({"error": "Missing required field: pitch_id"}, indent=2)

        # Retrieve database
        grades: List[Dict[str, Any]] = list(data.get("pitch_execution_grades", {}).values())

        # 3) Precise match
        for rec in grades:
            if rec.get("pitch_id") == pitch_id:
                return json.dumps(rec, indent=2)

        return json.dumps({"error": f"No grade found for pitch_id {pitch_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_grade_by_pitch_id",
                "description": "Fetch a single pitch execution grade record by pitch_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pitch_id": {
                            "type": "integer",
                            "description": "Exact pitch ID whose grade should be returned."
                        }
                    },
                    "required": ["pitch_id"]
                }
            }
        }
