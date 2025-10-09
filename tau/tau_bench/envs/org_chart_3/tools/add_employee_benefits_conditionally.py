from tau_bench.envs.tool import Tool
import json
from typing import Any

class add_employee_benefits_conditionally(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], employee_id: str, benefit_plan_ids: list[str]
    ) -> str:
        # Retrieve the current benefits for employees
        employees = data.get("employees", [])
        employee = next((e for e in employees if e["employee_id"] == employee_id), None)

        if not employee:
            payload = {"error": f"Employee {employee_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        current_benefits = set(employee.get("benefit_plan_ids", []))
        new_benefits = set(benefit_plan_ids)

        # Add only those benefits that are not currently included
        benefits_to_add = new_benefits - current_benefits
        final_benefits = list(current_benefits | new_benefits)

        # Revise employee benefits
        employee["benefit_plan_ids"] = final_benefits
        payload = {
            "success": f"Benefits updated for employee {employee_id}",
            "current_benefits": list(current_benefits),
            "requested_benefits": benefit_plan_ids,
            "benefits_actually_added": list(benefits_to_add),
            "final_benefits": final_benefits,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        pass
        #Retrieve the current benefits for employees
        employees = data.get("employees", [])
        employee = next((e for e in employees if e["employee_id"] == employee_id), None)

        if not employee:
            payload = {"error": f"Employee {employee_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        current_benefits = set(employee.get("benefit_plan_ids", []))
        new_benefits = set(benefit_plan_ids)

        #Add only those benefits that are not currently included
        benefits_to_add = new_benefits - current_benefits
        final_benefits = list(current_benefits | new_benefits)

        #Revise employee benefits
        employee["benefit_plan_ids"] = final_benefits
        payload = {
                "success": f"Benefits updated for employee {employee_id}",
                "current_benefits": list(current_benefits),
                "requested_benefits": benefit_plan_ids,
                "benefits_actually_added": list(benefits_to_add),
                "final_benefits": final_benefits,
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
                "name": "addEmployeeBenefitsConditionally",
                "description": "Add benefit plans to an employee, but only if they don't already have them. Returns details about what was actually added.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "Unique ID of the employee",
                        },
                        "benefit_plan_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of benefit plan IDs to add (only new ones will be added)",
                        },
                    },
                    "required": ["employee_id", "benefit_plan_ids"],
                    "additionalProperties": False,
                },
            },
        }
