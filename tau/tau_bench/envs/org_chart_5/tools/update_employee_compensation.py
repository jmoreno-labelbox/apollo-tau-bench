# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class update_employee_compensation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id, new_comp) -> str:
        if not find_employee(list(data.get("employees", {}).values()), employee_id):
            return json.dumps(
                {"error": f"employee_id {employee_id} not found"}, indent=2
            )

        new_comp_record = new_comp.copy()
        new_comp_record["employee_id"] = employee_id
        if "compensation_id" not in new_comp_record:
            return json.dumps(
                {"error": "new_comp payload must include a unique compensation_id"},
                indent=2,
            )

        data.get("compensation_records", []).append(new_comp_record)
        return json.dumps(
            {
                "success": f"Compensation record {new_comp_record['compensation_id']} added for {employee_id}"
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_employee_compensation",
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
