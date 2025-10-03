from tau_bench.envs.tool import Tool
import json
from collections import Counter
from typing import Any

class update_employee_compensation(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, new_comp: dict = None) -> str:
        if not find_employee(data.get("employees", []), employee_id):
            payload = {"error": f"employee_id {employee_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        new_comp_record = new_comp.copy()
        new_comp_record["employee_id"] = employee_id
        if "compensation_id" not in new_comp_record:
            payload = {"error": "new_comp payload must include a unique compensation_id"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        data.get("compensation_records", []).append(new_comp_record)
        payload = {
                "success": f"Compensation record {new_comp_record['compensation_id']} added for {employee_id}"
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateEmployeeCompensation",
                "description": "Adds a new compensation record for an employee, preserving history.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "new_comp": {
                            "type": "object",
                            "description": "New compensation details including a unique compensation_id",
                        },
                    },
                    "required": ["employee_id", "new_comp"],
                },
            },
        }
