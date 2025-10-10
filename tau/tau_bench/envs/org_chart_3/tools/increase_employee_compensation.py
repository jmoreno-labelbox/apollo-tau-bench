# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class increase_employee_compensation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str, compensation_id: str, effective_date: str,
               salary_increase_pct: Optional[float] = None, bonus_increase_pct: Optional[float] = None,
               equity_increase_amount: Optional[float] = None) -> str:
        # Retrieve the current compensation.
        comp = data.get("compensation_records", [])
        current = [c for c in comp if c["employee_id"] == employee_id]
        current.sort(key=lambda c: c["effective_date"], reverse=True)

        if not current:
            return json.dumps({"error": "No current compensation found for employee"}, indent=2)

        latest = current[0]

        # Compute updated values.
        new_salary = latest["base_salary"]
        new_bonus = latest["bonus_target_pct"]
        new_equity = latest["equity_grant"]

        if salary_increase_pct:
            new_salary = round(latest["base_salary"] * (1 + salary_increase_pct / 100))

        if bonus_increase_pct:
            new_bonus = latest["bonus_target_pct"] + bonus_increase_pct

        if equity_increase_amount:
            new_equity = latest["equity_grant"] + equity_increase_amount

        # Generate a new salary record.
        new_comp = {
            "compensation_id": compensation_id,
            "employee_id": employee_id,
            "base_salary": new_salary,
            "currency": latest["currency"],
            "bonus_target_pct": new_bonus,
            "equity_grant": new_equity,
            "effective_date": effective_date
        }

        # Eliminate any existing record with the same ID before adding the new entry.
        comp = [c for c in comp if c["compensation_id"] != compensation_id]
        comp.append(new_comp)
        data["compensation_records"] = comp

        return json.dumps({"success": f"Compensation increased for {employee_id}", "new_compensation": new_comp}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "increase_employee_compensation",
                "description": "Increase employee compensation by percentage or fixed amount based on current values.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "compensation_id": {"type": "string", "description": "New compensation record ID"},
                        "effective_date": {"type": "string", "description": "Effective date for the increase (YYYY-MM-DD)"},
                        "salary_increase_pct": {"type": "number", "description": "Percentage to increase base salary (optional)"},
                        "bonus_increase_pct": {"type": "number", "description": "Percentage points to increase bonus target (optional)"},
                        "equity_increase_amount": {"type": "number", "description": "Fixed amount to add to equity grant (optional)"}
                    },
                    "required": ["employee_id", "compensation_id", "effective_date"],
                    "additionalProperties": False
                }
            }
        }
