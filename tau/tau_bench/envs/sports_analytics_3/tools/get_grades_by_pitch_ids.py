from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetGradesByPitchIds(Tool):
    """
    Retrieve execution grade records for a collection of pitch IDs.
    Returns all matching rows sorted deterministically by pitch_id in ascending order, grade_id in ascending order.
    """

    @staticmethod
    def invoke(data: dict[str, Any], pitch_ids: list[int] = None,
    grades: Any = None,
    ) -> str:
        #1) Confirm validity
        if not isinstance(pitch_ids, list) or len(pitch_ids) == 0:
            payload = {
                    "error": "Missing required field: pitch_ids (non-empty list of integers)"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #2) Retrieve DB
        grades: list[dict[str, Any]] = data.get("pitch_execution_grades", {}).values()

        #3) Gather matches
        id_set = set(pitch_ids)
        matches = [rec for rec in grades.values() if rec.get("pitch_id") in id_set]

        if not matches:
            payload = {"No grades found": f"No grades found for pitch_ids {pitch_ids}"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetGradesByPitchIds",
                "description": "Fetch execution grade records for the given list of pitch IDs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pitch_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "List of pitch IDs to retrieve grades for.",
                        }
                    },
                    "required": ["pitch_ids"],
                },
            },
        }
