# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class remove_from_benefit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        benefit_id = kwargs.get("benefit_id")
        employee = find_employee(list(data.get("employees", {}).values()), employee_id)
        if not employee:
            return json.dumps(
                {"error": f"employee_id {employee_id} not found"}, indent=2
            )

        if (
            "benefit_plan_ids" in employee
            and benefit_id in employee["benefit_plan_ids"]
        ):
            employee["benefit_plan_ids"].remove(benefit_id)
            return json.dumps(
                {
                    "success": f"Employee {employee_id} removed from benefit {benefit_id}"
                },
                indent=2,
            )
        else:
            return json.dumps(
                {
                    "success": f"Employee {employee_id} was not enrolled in benefit {benefit_id}"
                },
                indent=2,
            )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_from_benefit",
                "description": "Remove an employee from a specific benefit plan.",
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
