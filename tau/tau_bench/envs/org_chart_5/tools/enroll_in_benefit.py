from tau_bench.envs.tool import Tool
import json
from collections import Counter
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class enroll_in_benefit(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, benefit_id: str = None) -> str:
        employee = find_employee(data.get("employees", {}).values(), employee_id)
        if not employee:
            payload = {"error": f"employee_id {employee_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        if "benefit_plan_ids" not in employee:
            employee["benefit_plan_ids"] = []

        if benefit_id not in employee["benefit_plan_ids"]:
            employee["benefit_plan_ids"].append(benefit_id)
            payload = {"success": f"Employee {employee_id} enrolled in benefit {benefit_id}"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = {
                    "success": f"Employee {employee_id} was already enrolled in benefit {benefit_id}"
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
                "name": "EnrollInBenefit",
                "description": "Enroll an employee IND a specific benefit plan (non-destructive).",
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
