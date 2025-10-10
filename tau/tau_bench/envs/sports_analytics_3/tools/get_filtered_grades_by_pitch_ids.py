# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetFilteredGradesByPitchIds(Tool):
    """
    Fetch execution grade records for a list of pitch IDs, then EXCLUDE any rows
    whose execution_grade is in the provided grades list.

    Inputs (exact names; case-sensitive):
      - pitch_ids (List[int]) : Non-empty list of pitch IDs to search.
      - grades    (List[str]) : Non-empty list of grade labels to EXCLUDE
                                (exact, case-sensitive match, e.g., ["C", "D", "F"]).

    Behavior:
      - Looks up all rows where rec.pitch_id ∈ pitch_ids.
      - Filters OUT rows where rec.execution_grade ∈ grades.
      - Returns results sorted deterministically by (pitch_id ASC, grade_id ASC).
      - If no rows match the pitch_ids at all, returns a structured error.
      - If rows match pitch_ids but all are filtered out by grades, returns a structured error.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # ---- 1) Validate inputs
        pitch_ids = kwargs.get("pitch_ids")
        grades_to_exclude = kwargs.get("grades")

        if not isinstance(pitch_ids, list) or len(pitch_ids) == 0:
            return json.dumps(
                {"error": "Missing required field: pitch_ids (non-empty list of integers)"},
                indent=2
            )
        if not isinstance(grades_to_exclude, list) or len(grades_to_exclude) == 0:
            return json.dumps(
                {"error": "Missing required field: grades (non-empty list of strings to EXCLUDE)"},
                indent=2
            )

        # ---- 2) Get DB
        grades: List[Dict[str, Any]] = data.get("pitch_execution_grades", [])

        # ---- 3) Collect matches by pitch_ids
        id_set = set(pitch_ids)
        initial = [rec for rec in grades if rec.get("pitch_id") in id_set]

        if not initial:
            return json.dumps(
                {"error": f"No grades found for pitch_ids {pitch_ids}"},
                indent=2
            )

        # ---- 4) Filter OUT records whose execution_grade is in grades_to_exclude (exact, case-sensitive)
        excl_set = set(grades_to_exclude)
        filtered = [rec for rec in initial if rec.get("execution_grade") in excl_set]

        if not filtered:
            return json.dumps(
                {
                    "error": (
                        "All grades were filtered out. No remaining records after excluding "
                        f"{sorted(excl_set)} for pitch_ids {pitch_ids}"
                    )
                },
                indent=2
            )

        # ---- 5) Deterministic sort: pitch_id ASC, grade_id ASC
        filtered.sort(key=lambda r: (int(r.get("pitch_id", 0)), int(r.get("grade_id", 0))))

        return json.dumps(filtered, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_filtered_grades_by_pitch_ids",
                "description": "Fetch execution grade records for given pitch IDs and EXCLUDE rows whose execution_grade matches any provided grade.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pitch_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "Non-empty list of pitch IDs to retrieve grades for."
                        },
                        "grades": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Non-empty list of grade labels to EXCLUDE (exact, case-sensitive)."
                        }
                    },
                    "required": ["pitch_ids", "grades"]
                }
            }
        }
