# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class add_employee_benefit_if_missing(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str, benefit_plan_id: str, current_benefit_plan_ids: List[str]) -> str:
        employees = list(data.get("employees", {}).values())
        employee = next((e for e in employees if e["employee_id"] == employee_id), None)

        if not employee:
            return json.dumps({"error": f"Employee {employee_id} not found"}, indent=2)

        current_benefits = set(employee.get("benefit_plan_ids", []))

        if benefit_plan_id in current_benefits:
            return json.dumps({"success": f"Employee {employee_id} already has benefit {benefit_plan_id}, no change needed"}, indent=2)

        # Add the missing benefit
        new_benefits = list(current_benefits)
        new_benefits.append(benefit_plan_id)
        employee["benefit_plan_ids"] = new_benefits

        return json.dumps({
            "success": f"Benefit {benefit_plan_id} added to employee {employee_id}",
            "previous_benefits": list(current_benefits),
            "new_benefits": new_benefits
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_employee_benefit_if_missing",
                "description": "Add a benefit plan to an employee only if they don't already have it.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "benefit_plan_id": {"type": "string", "description": "Benefit plan ID to add"},
                        "current_benefit_plan_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Known current benefit plan IDs (for reference)"
                        }
                    },
                    "required": ["employee_id", "benefit_plan_id", "current_benefit_plan_ids"],
                    "additionalProperties": False
                }
            }
        }
