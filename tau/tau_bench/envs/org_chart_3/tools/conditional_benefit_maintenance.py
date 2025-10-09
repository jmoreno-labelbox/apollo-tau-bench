from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class conditional_benefit_maintenance(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str,
        equity_threshold: float,
        maintain_benefits: list[str],
        reduced_benefits: list[str]
    ) -> str:
        # Retrieve the current compensation
        comp = data.get("compensation_records", [])
        current = [c for c in comp if c["employee_id"] == employee_id]
        current.sort(key=lambda c: c["effective_date"], reverse=True)

        if not current:
            payload = {"error": "No current compensation found for employee"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        latest = current[0]
        current_equity = latest.get("equity_grant", 0)

        employees = data.get("employees", [])
        employee = next((e for e in employees if e["employee_id"] == employee_id), None)

        if not employee:
            payload = {"error": f"Employee {employee_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        if current_equity > equity_threshold:
            # Ensure full benefits are maintained
            employee["benefit_plan_ids"] = maintain_benefits
            action_taken = "Benefits maintained due to high equity"
            final_benefits = maintain_benefits
        else:
            # Diminish benefits while on leave
            employee["benefit_plan_ids"] = reduced_benefits
            action_taken = "Benefits reduced during leave due to lower equity"
            final_benefits = reduced_benefits

        data["employees"] = employees
        payload = {
                "success": f"Benefit maintenance decision made for employee {employee_id}",
                "equity_amount": current_equity,
                "equity_threshold": equity_threshold,
                "condition_met": current_equity > equity_threshold,
                "action_taken": action_taken,
                "final_benefits": final_benefits,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        pass
        #Retrieve the current compensation
        comp = data.get("compensation_records", [])
        current = [c for c in comp if c["employee_id"] == employee_id]
        current.sort(key=lambda c: c["effective_date"], reverse=True)

        if not current:
            payload = {"error": "No current compensation found for employee"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        latest = current[0]
        current_equity = latest.get("equity_grant", 0)

        employees = data.get("employees", [])
        employee = next((e for e in employees if e["employee_id"] == employee_id), None)

        if not employee:
            payload = {"error": f"Employee {employee_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        if current_equity > equity_threshold:
            #Ensure full benefits are maintained
            employee["benefit_plan_ids"] = maintain_benefits
            action_taken = "Benefits maintained due to high equity"
            final_benefits = maintain_benefits
        else:
            #Diminish benefits while on leave
            employee["benefit_plan_ids"] = reduced_benefits
            action_taken = "Benefits reduced during leave due to lower equity"
            final_benefits = reduced_benefits

        data["employees"] = employees
        payload = {
                "success": f"Benefit maintenance decision made for employee {employee_id}",
                "equity_amount": current_equity,
                "equity_threshold": equity_threshold,
                "condition_met": current_equity > equity_threshold,
                "action_taken": action_taken,
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
                "name": "ConditionalBenefitMaintenance",
                "description": "Maintain or reduce employee benefits based on equity threshold during leave.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "equity_threshold": {
                            "type": "number",
                            "description": "Equity threshold for benefit maintenance",
                        },
                        "maintain_benefits": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Benefits to maintain if equity is above threshold",
                        },
                        "reduced_benefits": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Reduced benefits if equity is below threshold",
                        },
                    },
                    "required": [
                        "employee_id",
                        "equity_threshold",
                        "maintain_benefits",
                        "reduced_benefits",
                    ],
                    "additionalProperties": False,
                },
            },
        }
