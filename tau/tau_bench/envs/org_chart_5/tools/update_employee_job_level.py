# Copyright Sierra Technologies

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class update_employee_job_level(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id, new_level) -> str:
        employee = find_employee(list(data.get("employees", {}).values()), employee_id)
        if not employee:
            return json.dumps(
                {"error": f"employee_id {employee_id} not found"}, indent=2
            )

        employee["level_id"] = new_level
        return json.dumps(
            {"success": f"Job level for {employee_id} updated to {new_level}"}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_employee_job_level",
                "description": "Change an employee's job level ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "new_level": {"type": "string"},
                    },
                    "required": ["employee_id", "new_level"],
                },
            },
        }
