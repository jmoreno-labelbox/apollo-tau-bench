from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetGradesByGradeForGame(Tool):
    """
    Retrieve all pitch execution grade records for a specified game that match any of the
    provided grade values.

    Inputs:
      - game_pk (int)           [required]
      - grades (List[str])      [required] list of execution_grade values to match

    Behavior:
      - Exact (case-sensitive) match on execution_grade.
      - Filters records where record.game_pk equals game_pk AND record.execution_grade is in grades.
      - Deterministic ordering by pitch_id in ascending order, then grade_id in ascending order.
    """

    @staticmethod
    def invoke(data: dict[str, Any], game_pk: int = None, grades: list[str] = None) -> str:
        #1) Confirm validity
        if game_pk is None:
            payload = {"error": "Missing required field: game_pk"}
            out = json.dumps(payload, indent=2)
            return out
        if not isinstance(grades, list) or len(grades) == 0:
            payload = {"error": "Missing required field: grades (non-empty list of strings)"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #2) Retrieve DB
        records: list[dict[str, Any]] = data.get("pitch_execution_grades", [])

        #3) Apply filter (exact, case-sensitive)
        allowed = set(grades)
        matches = [
            r
            for r in records
            if r.get("game_pk") == game_pk and r.get("execution_grade") in allowed
        ]

        if not matches:
            payload = {
                    "error": f"No grades found for game_pk {game_pk} with execution_grade in {grades}"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #4) Order deterministically
        matches.sort(
            key=lambda r: (int(r.get("pitch_id", 0)), int(r.get("grade_id", 0)))
        )
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getGradesByGradeForGame",
                "description": "Fetch pitch execution grade records for a game where execution_grade matches any of the provided values.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {
                            "type": "integer",
                            "description": "Game primary key to filter on.",
                        },
                        "grades": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of execution_grade values to match (case-sensitive).",
                        },
                    },
                    "required": ["game_pk", "grades"],
                },
            },
        }
