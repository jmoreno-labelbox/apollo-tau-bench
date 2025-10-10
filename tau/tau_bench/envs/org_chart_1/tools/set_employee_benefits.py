# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class set_employee_benefits(Tool):
    """
    Overwrites the benefit_plan_ids array for an employee to match exactly the
    list supplied in `benefit_plan_ids`.
    """

    @staticmethod
    def invoke(
        data: Dict[str, Any], employee_id: str, benefit_plan_ids: List[str]
    ) -> str:
        employees = list(data.get("employees", {}).values())

        for e in employees:
            if e["employee_id"] == employee_id:
                e["benefit_plan_ids"] = benefit_plan_ids
                data["employees"] = employees
                return json.dumps(
                    {"success": f"benefits for {employee_id} updated"}, indent=2
                )

        return json.dumps({"error": f"employee_id {employee_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_employee_benefits",
                "description": "Replace an employee's benefit_plan_ids array with the supplied list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "benefit_plan_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Array of benefit_plan_id values",
                        },
                    },
                    "required": ["employee_id", "benefit_plan_ids"],
                    "additionalProperties": False,
                },
            },
        }
