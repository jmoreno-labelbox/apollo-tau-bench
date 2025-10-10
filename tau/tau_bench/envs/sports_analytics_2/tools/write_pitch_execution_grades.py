# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class WritePitchExecutionGrades(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], game_pk, grades_count) -> str:
        grades = data.setdefault("pitch_execution_grades", {})
        # Create the subsequent identifier.
        next_id = str(len(grades) + 1)
        grades[next_id] = {
            "grade_id": f"grade_{next_id}",
            "game_pk": game_pk,
            "grades_count": grades_count
        }
        return json.dumps({"status": "ok"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "write_pitch_execution_grades", "description": "Writes pitch execution grades to database.", "parameters": {"type": "object", "properties": {"game_pk": {"type": "string"}, "grades_count": {"type": "integer"}}, "required": ["game_pk"]}}}
