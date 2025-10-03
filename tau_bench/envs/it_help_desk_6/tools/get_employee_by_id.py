from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetEmployeeById(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str) -> str:
        pass
        emp = _find_one(data["employees"], employee_id=employee_id)
        payload = {"status": "ok", "employee": emp}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetEmployeeById",
                "description": "Retrieve a single employee record by employee_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                },
            },
        }
