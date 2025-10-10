# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetGradesByGradeForGame(Tool):
    """
    Return all pitch execution grade records for a given game that match any of the
    provided grade values.

    Inputs:
      - game_pk (int)           [required]
      - grades (List[str])      [required] list of execution_grade values to match

    Behavior:
      - Exact (case-sensitive) match on execution_grade.
      - Filters records where record.game_pk == game_pk AND record.execution_grade in grades.
      - Deterministic ordering by pitch_id ASC, then grade_id ASC.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        game_pk = kwargs.get("game_pk")
        grades_filter = kwargs.get("grades")

        # 1) Verify
        if game_pk is None:
            return json.dumps({"error": "Missing required field: game_pk"}, indent=2)
        if not isinstance(grades_filter, list) or len(grades_filter) == 0:
            return json.dumps({"error": "Missing required field: grades (non-empty list of strings)"}, indent=2)

        # Retrieve database
        records: List[Dict[str, Any]] = list(data.get("pitch_execution_grades", {}).values())

        # 3) Exact case-sensitive filtering
        allowed = set(grades_filter)
        matches = [
            r for r in records
            if r.get("game_pk") == game_pk and r.get("execution_grade") in allowed
        ]

        if not matches:
            return json.dumps(
                {"error": f"No grades found for game_pk {game_pk} with execution_grade in {grades_filter}"},
                indent=2
            )

        # 4) Fixed sequence
        matches.sort(key=lambda r: (int(r.get("pitch_id", 0)), int(r.get("grade_id", 0))))

        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_grades_by_grade_for_game",
                "description": "Fetch pitch execution grade records for a game where execution_grade matches any of the provided values.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {
                            "type": "integer",
                            "description": "Game primary key to filter on."
                        },
                        "grades": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of execution_grade values to match (case-sensitive)."
                        }
                    },
                    "required": ["game_pk", "grades"]
                }
            }
        }
