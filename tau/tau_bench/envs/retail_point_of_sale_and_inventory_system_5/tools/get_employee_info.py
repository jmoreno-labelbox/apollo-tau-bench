# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetEmployeeInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id) -> str:
        employees = list(data.get("employees", {}).values())
        result = [item for item in employees if item["employee_id"] == employee_id]
        if result:
            return json.dumps(result[0])
        return json.dumps({"error": f"Employee {employee_id} not found"})
    @staticmethod
    def get_info() -> Dict[str, Any]:

        return {
            "type": "function",
            "function": {
                "name": "get_employee_info",
                "description": "Tool function: get_employee_info",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }
