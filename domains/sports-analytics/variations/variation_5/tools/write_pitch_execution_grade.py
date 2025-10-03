from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class WritePitchExecutionGrade(Tool):
    """Add pitch_execution_grades based on miss_distance and (optional) model fields."""

    @staticmethod
    def invoke(
        data,
        pitch_id: int,
        game_pk: int,
        intended_quadrant_model: str,
        actual_quadrant: str,
        miss_distance_inches: float,
        grade: str = None
    ) -> str:
        err = _require_tables(data, ["pitch_execution_grades"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        need = _check_required(
            {
                "pitch_id": pitch_id,
                "game_pk": game_pk,
                "intended_quadrant_model": intended_quadrant_model,
                "actual_quadrant": actual_quadrant,
                "miss_distance_inches": miss_distance_inches,
            },
            [
                "pitch_id",
                "game_pk",
                "intended_quadrant_model",
                "actual_quadrant",
                "miss_distance_inches",
            ],
        )
        if need:
            payload = {"error": need}
            out = json.dumps(payload, indent=2)
            return out
        rows = data["pitch_execution_grades"]
        new_id = _next_id(rows, "grade_id")
        # Use provided grade if given, otherwise compute it
        exec_grade = grade if grade is not None else _grade_execution(miss_distance_inches)
        row = {
            "grade_id": new_id,
            "pitch_id": pitch_id,
            "game_pk": game_pk,
            "intended_quadrant_model": intended_quadrant_model,
            "actual_quadrant": actual_quadrant,
            "miss_distance_inches": miss_distance_inches,
            "execution_grade": exec_grade,
        }
        rows.append(row)
        payload = {"grade_id": new_id, "execution_grade": exec_grade}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "WritePitchExecutionGrade",
                "description": "Creates a pitch_execution_grades row with deterministic grade policy.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pitch_id": {"type": "integer"},
                        "game_pk": {"type": "integer"},
                        "intended_quadrant_model": {"type": "string"},
                        "actual_quadrant": {"type": "string"},
                        "miss_distance_inches": {"type": "number"},
                    },
                    "required": [
                        "pitch_id",
                        "game_pk",
                        "intended_quadrant_model",
                        "actual_quadrant",
                        "miss_distance_inches",
                    ],
                },
            },
        }
