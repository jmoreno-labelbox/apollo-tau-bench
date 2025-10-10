# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class WritePitchExecutionGrades(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        game_pk = kwargs.get("game_pk")
        grades_count = kwargs.get("grades_count")
        data.setdefault("pitch_execution_grades", []).append({
            "grade_id": f"grade_{len(data.get('pitch_execution_grades', []))+1}",
            "game_pk": game_pk,
            "grades_count": grades_count
        })
        return json.dumps({"status": "ok"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "write_pitch_execution_grades", "description": "Writes pitch execution grades to database.", "parameters": {"type": "object", "properties": {"game_pk": {"type": "string"}, "grades_count": {"type": "integer"}}, "required": ["game_pk"]}}}
