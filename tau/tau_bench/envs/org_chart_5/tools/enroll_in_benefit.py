# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class enroll_in_benefit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], benefit_id, employee_id) -> str:
        employee = find_employee(list(data.get("employees", {}).values()), employee_id)
        if not employee:
            return json.dumps(
                {"error": f"employee_id {employee_id} not found"}, indent=2
            )

        if "benefit_plan_ids" not in employee:
            employee["benefit_plan_ids"] = []

        if benefit_id not in employee["benefit_plan_ids"]:
            employee["benefit_plan_ids"].append(benefit_id)
            return json.dumps(
                {"success": f"Employee {employee_id} enrolled in benefit {benefit_id}"},
                indent=2,
            )
        else:
            return json.dumps(
                {
                    "success": f"Employee {employee_id} was already enrolled in benefit {benefit_id}"
                },
                indent=2,
            )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "enroll_in_benefit",
                "description": "Enroll an employee in a specific benefit plan (non-destructive).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "benefit_id": {"type": "string"},
                    },
                    "required": ["employee_id", "benefit_id"],
                },
            },
        }
