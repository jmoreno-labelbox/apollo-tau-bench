# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class conditional_benefit_maintenance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str, equity_threshold: float,
               maintain_benefits: List[str], reduced_benefits: List[str]) -> str:
        # Retrieve the current salary.
        comp = data.get("compensation_records", [])
        current = [c for c in comp if c["employee_id"] == employee_id]
        current.sort(key=lambda c: c["effective_date"], reverse=True)

        if not current:
            return json.dumps({"error": "No current compensation found for employee"}, indent=2)

        latest = current[0]
        current_equity = latest.get("equity_grant", 0)

        employees = list(data.get("employees", {}).values())
        employee = next((e for e in employees if e["employee_id"] == employee_id), None)

        if not employee:
            return json.dumps({"error": f"Employee {employee_id} not found"}, indent=2)

        if current_equity > equity_threshold:
            # Preserve all advantages.
            employee["benefit_plan_ids"] = maintain_benefits
            action_taken = "Benefits maintained due to high equity"
            final_benefits = maintain_benefits
        else:
            # Diminish advantages while on leave.
            employee["benefit_plan_ids"] = reduced_benefits
            action_taken = "Benefits reduced during leave due to lower equity"
            final_benefits = reduced_benefits

        data["employees"] = employees

        return json.dumps({
            "success": f"Benefit maintenance decision made for employee {employee_id}",
            "equity_amount": current_equity,
            "equity_threshold": equity_threshold,
            "condition_met": current_equity > equity_threshold,
            "action_taken": action_taken,
            "final_benefits": final_benefits
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "conditional_benefit_maintenance",
                "description": "Maintain or reduce employee benefits based on equity threshold during leave.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "equity_threshold": {"type": "number", "description": "Equity threshold for benefit maintenance"},
                        "maintain_benefits": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Benefits to maintain if equity is above threshold"
                        },
                        "reduced_benefits": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Reduced benefits if equity is below threshold"
                        }
                    },
                    "required": ["employee_id", "equity_threshold", "maintain_benefits", "reduced_benefits"],
                    "additionalProperties": False
                }
            }
        }
