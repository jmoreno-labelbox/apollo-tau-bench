# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ExecData(Tool):
    @staticmethod
        # main invoke function
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        game_pk = kwargs.get("game_pk")
        grades_count = kwargs.get("grades_count")
        data.setdefault("pitch_execution_grades", []).append({
            "grade_id": f"grade_{len(data.get('pitch_execution_grades', []))+1}",
            "game_pk": game_pk,
            "grades_count": grades_count
        })
        # return result
        return json.dumps({"status": "ok"}, indent=2)

    @staticmethod
        # info metadata
    def get_info() -> Dict[str, Any]:
        # return result
        return {"type": "function", "function": {"name": "makeGrades", "description": "Persists pitch execution grades to database.", "parameters": {"type": "object", "properties": {"game_pk": {"type": "string"}, "grades_count": {"type": "integer"}}, "required": ["game_pk"]}}}
