# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class increase_employee_compensation(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        employee_id: str,
        compensation_id: str,
        effective_date: str,
        salary_increase_pct: Optional[float] = None,
        equity_increase_amount: Optional[int] = None,
    ) -> str:

        comp_records = data.get("compensation_records", [])
        # Get current compensation
        current_comp_list = [c for c in comp_records if c["employee_id"] == employee_id]
        if not current_comp_list:
            return json.dumps(
                {
                    "error": f"No compensation record found for employee_id {employee_id}"
                },
                indent=2,
            )

        current_comp_list.sort(key=lambda c: c["effective_date"], reverse=True)
        current_comp = current_comp_list[0]

        # Start with current values
        new_comp = current_comp.copy()

        # Update with new required values
        new_comp["compensation_id"] = compensation_id
        new_comp["effective_date"] = effective_date

        # Calculate new salary if applicable
        if salary_increase_pct is not None:
            new_comp["base_salary"] = int(
                current_comp["base_salary"] * (1 + salary_increase_pct / 100)
            )

        # Calculate new equity if applicable
        if equity_increase_amount is not None:
            new_comp["equity_grant"] = (
                current_comp["equity_grant"] + equity_increase_amount
            )

        # Add the new record, preserving history
        comp_records.append(new_comp)
        data["compensation_records"] = comp_records
        return json.dumps(
            {
                "success": f"New compensation record {compensation_id} created for {employee_id}",
                "new_compensation": new_comp,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "increase_employee_compensation",
                "description": "Increase salary by a percentage and/or equity by a fixed amount, creating a new compensation record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "compensation_id": {"type": "string"},
                        "effective_date": {"type": "string"},
                        "salary_increase_pct": {"type": "number"},
                        "equity_increase_amount": {"type": "integer"},
                    },
                    "required": ["employee_id", "compensation_id", "effective_date"],
                },
            },
        }
