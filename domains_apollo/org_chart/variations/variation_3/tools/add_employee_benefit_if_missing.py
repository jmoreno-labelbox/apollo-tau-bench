from tau_bench.envs.tool import Tool
import json
from typing import Any

class add_employee_benefit_if_missing(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str,
        benefit_plan_id: str,
        current_benefit_plan_ids: list[str]
    ) -> str:
        employees = data.get("employees", [])
        employee = next((e for e in employees if e["employee_id"] == employee_id), None)

        if not employee:
            payload = {"error": f"Employee {employee_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        current_benefits = set(employee.get("benefit_plan_ids", []))

        if benefit_plan_id in current_benefits:
            payload = {
                "success": f"Employee {employee_id} already has benefit {benefit_plan_id}, no change needed"
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Insert the benefit that is missing
        new_benefits = list(current_benefits)
        new_benefits.append(benefit_plan_id)
        employee["benefit_plan_ids"] = new_benefits
        payload = {
            "success": f"Benefit {benefit_plan_id} added to employee {employee_id}",
            "previous_benefits": list(current_benefits),
            "new_benefits": new_benefits,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        pass
        employees = data.get("employees", [])
        employee = next((e for e in employees if e["employee_id"] == employee_id), None)

        if not employee:
            payload = {"error": f"Employee {employee_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        current_benefits = set(employee.get("benefit_plan_ids", []))

        if benefit_plan_id in current_benefits:
            payload = {
                    "success": f"Employee {employee_id} already has benefit {benefit_plan_id}, no change needed"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #Insert the benefit that is missing
        new_benefits = list(current_benefits)
        new_benefits.append(benefit_plan_id)
        employee["benefit_plan_ids"] = new_benefits
        payload = {
                "success": f"Benefit {benefit_plan_id} added to employee {employee_id}",
                "previous_benefits": list(current_benefits),
                "new_benefits": new_benefits,
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
                "name": "AddEmployeeBenefitIfMissing",
                "description": "Add a benefit plan to an employee only if they don't already have it.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "benefit_plan_id": {
                            "type": "string",
                            "description": "Benefit plan ID to add",
                        },
                        "current_benefit_plan_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Known current benefit plan IDs (for reference)",
                        },
                    },
                    "required": [
                        "employee_id",
                        "benefit_plan_id",
                        "current_benefit_plan_ids",
                    ],
                    "additionalProperties": False,
                },
            },
        }
