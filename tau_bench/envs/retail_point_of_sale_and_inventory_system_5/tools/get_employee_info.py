from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class GetEmployeeInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None) -> str:
        employees = data.get("employees", [])
        result = [item for item in employees if item["employee_id"] == employee_id]
        if result:
            payload = result[0]
            out = json.dumps(payload)
            return out
        payload = {"error": f"Employee {employee_id} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetEmployeeInfo",
                "parameters": {"employee_id": {"type": "string"}},
                "required": ["employee_id"],
            },
        }
