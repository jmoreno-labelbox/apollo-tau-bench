from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetEmployeeLicenses(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None) -> str:
        if employee_id is None:
            payload = {"status": "error", "reason": "The employee_id field is required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        license_assignments = data.get("license_assignments", [])
        licenses = []

        for assignment in license_assignments:
            if assignment["employee_id"] == employee_id:
                licenses.append(assignment["license_id"])
        payload = licenses
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getEmployeeLicenses",
                "description": "Finds licenses associated with a specified employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The id of the employee to search for.",
                        },
                    },
                    "required": ["employee_id"],
                },
            },
        }
