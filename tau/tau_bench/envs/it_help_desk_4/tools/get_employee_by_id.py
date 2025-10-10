# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetEmployeeById(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str) -> str:
        emp = _find_one(data["employees"], employee_id=employee_id)
        return json.dumps({"status": "ok", "employee": emp})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_employee_by_id",
                "description": "Retrieve a single employee record by employee_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                },
            },
        }
