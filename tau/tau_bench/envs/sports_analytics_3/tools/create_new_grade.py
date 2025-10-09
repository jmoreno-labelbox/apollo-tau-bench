from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateNewGrade(Tool):
    """
    Establish a new pitch execution grade.
    Required fields:
      - pitch_id (int)
      - game_pk (int)
      - intended_quadrant_model (string)
      - actual_quadrant (string)
      - miss_distance_inches (float)
      - execution_grade (string)
    Auto-generates grade_id as max existing + 1 (starting at 1).
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        pitch_id: int = None,
        game_pk: int = None,
        intended_quadrant_model: str = None,
        actual_quadrant: str = None,
        miss_distance_inches: float = None,
        execution_grade: str = None
    ) -> str:
        #1) Confirm required fields
        missing = []
        if pitch_id is None:
            missing.append("pitch_id")
        if game_pk is None:
            missing.append("game_pk")
        if intended_quadrant_model is None:
            missing.append("intended_quadrant_model")
        if actual_quadrant is None:
            missing.append("actual_quadrant")
        if miss_distance_inches is None:
            missing.append("miss_distance_inches")
        if not isinstance(execution_grade, str) or execution_grade == "":
            missing.append("execution_grade")

        if missing:
            payload = {"error": f"Missing required field(s): {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #2) Retrieve DB
        grades: list[dict[str, Any]] = data.get("pitch_execution_grades", {}).values()

        #3) Create a new grade_id
        new_id = get_next_grade_id(data)

        #4) Establish a new record
        new_record = {
            "grade_id": new_id,
            "pitch_id": pitch_id,
            "game_pk": game_pk,
            "intended_quadrant_model": intended_quadrant_model,
            "actual_quadrant": actual_quadrant,
            "miss_distance_inches": miss_distance_inches,
            "execution_grade": execution_grade,
        }
        grades.append(new_record)
        payload = new_record
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateNewGrade",
                "description": "Create a new pitch execution grade with auto-generated grade_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pitch_id": {
                            "type": "integer",
                            "description": "Pitch ID this grade belongs to.",
                        },
                        "game_pk": {
                            "type": "integer",
                            "description": "Game primary key.",
                        },
                        "intended_quadrant_model": {
                            "type": "integer",
                            "description": "Intended quadrant from the model.",
                        },
                        "actual_quadrant": {
                            "type": "integer",
                            "description": "Actual quadrant observed.",
                        },
                        "miss_distance_inches": {
                            "type": "number",
                            "description": "Distance missed in inches.",
                        },
                        "execution_grade": {
                            "type": "string",
                            "description": "Execution grade value.",
                        },
                    },
                    "required": [
                        "pitch_id",
                        "game_pk",
                        "intended_quadrant_model",
                        "actual_quadrant",
                        "miss_distance_inches",
                        "execution_grade",
                    ],
                },
            },
        }
