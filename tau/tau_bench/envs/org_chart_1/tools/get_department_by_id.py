# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_department_by_id(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], department_id: str) -> str:
        depts = list(data.get("departments", {}).values())
        for d in depts:
            if d["department_id"] == department_id:
                return json.dumps(d, indent=2)
        return json.dumps(
            {"error": f"department_id {department_id} not found"}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_department_by_id",
                "description": "Fetch department details by department_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"department_id": {"type": "string"}},
                    "required": ["department_id"],
                    "additionalProperties": False,
                },
            },
        }
