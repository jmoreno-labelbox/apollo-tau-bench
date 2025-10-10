# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class add_employee_benefits_conditionally(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str, benefit_plan_ids: List[str]) -> str:
        # Get current employee benefits
        employees = list(data.get("employees", {}).values())
        employee = next((e for e in employees if e["employee_id"] == employee_id), None)

        if not employee:
            return json.dumps({"error": f"Employee {employee_id} not found"}, indent=2)

        current_benefits = set(employee.get("benefit_plan_ids", []))
        new_benefits = set(benefit_plan_ids)

        # Only add benefits that aren't already present
        benefits_to_add = new_benefits - current_benefits
        final_benefits = list(current_benefits | new_benefits)

        # Update employee benefits
        employee["benefit_plan_ids"] = final_benefits

        return json.dumps({
            "success": f"Benefits updated for employee {employee_id}",
            "current_benefits": list(current_benefits),
            "requested_benefits": benefit_plan_ids,
            "benefits_actually_added": list(benefits_to_add),
            "final_benefits": final_benefits
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_employee_benefits_conditionally",
                "description": "Add benefit plans to an employee, but only if they don't already have them. Returns details about what was actually added.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "Unique ID of the employee"
                        },
                        "benefit_plan_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of benefit plan IDs to add (only new ones will be added)"
                        }
                    },
                    "required": ["employee_id", "benefit_plan_ids"],
                    "additionalProperties": False
                }
            }
        }
