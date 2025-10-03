from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetFilteredGradesByPitchIds(Tool):
    """
    Retrieve execution grade records for a collection of pitch IDs, then EXCLUDE any rows
    whose execution_grade matches the provided grades list.

    Inputs (exact names; case-sensitive):
      - pitch_ids (List[int]) : Non-empty list of pitch IDs to search.
      - grades    (List[str]) : Non-empty list of grade labels to EXCLUDE
                                (exact, case-sensitive match, e.g., ["C", "D", "F"]).

    Behavior:
      - Looks up all rows where rec.pitch_id is in pitch_ids.
      - Excludes rows where rec.execution_grade is in grades.
      - Returns results sorted deterministically by (pitch_id in ascending order, grade_id in ascending order).
      - If no rows match the pitch_ids, returns a structured error.
      - If rows match pitch_ids but all are excluded by grades, returns a structured error.
    """

    @staticmethod
    def invoke(data: dict[str, Any], pitch_ids: list[int] = None, grades_to_exclude: list[str] = None,
    grades: Any = None,
    ) -> str:
        #---- 1) Confirm inputs
        if not isinstance(pitch_ids, list) or len(pitch_ids) == 0:
            payload = {
                    "error": "Missing required field: pitch_ids (non-empty list of integers)"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        if not isinstance(grades_to_exclude, list) or len(grades_to_exclude) == 0:
            payload = {
                    "error": "Missing required field: grades (non-empty list of strings to EXCLUDE)"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #---- 2) Retrieve DB
        grades: list[dict[str, Any]] = data.get("pitch_execution_grades", [])

        #---- 3) Gather matches based on pitch_ids
        id_set = set(pitch_ids)
        initial = [rec for rec in grades if rec.get("pitch_id") in id_set]

        if not initial:
            payload = {"error": f"No grades found for pitch_ids {pitch_ids}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #---- 4) Exclude records where execution_grade matches grades_to_exclude (exact, case-sensitive)
        excl_set = set(grades_to_exclude)
        filtered = [rec for rec in initial if rec.get("execution_grade") in excl_set]

        if not filtered:
            payload = {
                    "error": (
                        "All grades were filtered out. No remaining records after excluding "
                        f"{sorted(excl_set)} for pitch_ids {pitch_ids}"
                    )
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #---- 5) Sort deterministically: pitch_id ASC, grade_id ASC
        filtered.sort(
            key=lambda r: (int(r.get("pitch_id", 0)), int(r.get("grade_id", 0)))
        )
        payload = filtered
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFilteredGradesByPitchIds",
                "description": "Fetch execution grade records for given pitch IDs and EXCLUDE rows whose execution_grade matches any provided grade.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pitch_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "Non-empty list of pitch IDs to retrieve grades for.",
                        },
                        "grades": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Non-empty list of grade labels to EXCLUDE (exact, case-sensitive).",
                        },
                    },
                    "required": ["pitch_ids", "grades"],
                },
            },
        }
