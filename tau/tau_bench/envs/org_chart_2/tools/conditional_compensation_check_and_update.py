# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class conditional_compensation_check_and_update(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        employee_id: str,
        compensation_id: str,
        effective_date: str,
        salary_threshold: Optional[float] = None,
        target_salary: Optional[float] = None,
        bonus_threshold: Optional[float] = None,
        target_bonus: Optional[float] = None,
        equity_increase_amount: Optional[float] = None,
    ) -> str:
        # Retrieve current salary information.
        comp = data.get("compensation_records", [])
        current = [c for c in comp if c["employee_id"] == employee_id]
        current.sort(key=lambda c: c["effective_date"], reverse=True)

        if not current:
            return json.dumps(
                {"error": "No current compensation found for employee"}, indent=2
            )

        latest = current[0]
        changes_made = []

        # Initialize with existing values.
        new_salary = latest["base_salary"]
        new_bonus = latest["bonus_target_pct"]
        new_equity = latest["equity_grant"]

        # Verify salary criteria
        if salary_threshold is not None and target_salary is not None:
            if latest["base_salary"] < salary_threshold:
                new_salary = target_salary
                changes_made.append(
                    f"salary increased from ${latest['base_salary']:,} to ${target_salary:,}"
                )
            else:
                changes_made.append(
                    f"salary ${latest['base_salary']:,} already above threshold ${salary_threshold:,}"
                )

        # Verify bonus eligibility criteria
        if bonus_threshold is not None and target_bonus is not None:
            if latest["bonus_target_pct"] < bonus_threshold:
                new_bonus = target_bonus
                changes_made.append(
                    f"bonus increased from {latest['bonus_target_pct']}% to {target_bonus}%"
                )
            else:
                changes_made.append(
                    f"bonus {latest['bonus_target_pct']}% already above threshold {bonus_threshold}%"
                )

        # Manage equity growth
        if equity_increase_amount is not None:
            new_equity = latest["equity_grant"] + equity_increase_amount
            changes_made.append(
                f"equity increased by ${equity_increase_amount:,} from ${latest['equity_grant']:,} to ${new_equity:,}"
            )

        # Generate a new salary record.
        new_comp = {
            "compensation_id": compensation_id,
            "employee_id": employee_id,
            "base_salary": new_salary,
            "currency": latest["currency"],
            "bonus_target_pct": new_bonus,
            "equity_grant": new_equity,
            "effective_date": effective_date,
        }

        # Delete any existing record with the same ID and insert the new one.
        comp = [c for c in comp if c["compensation_id"] != compensation_id]
        comp.append(new_comp)
        data["compensation_records"] = comp

        return json.dumps(
            {
                "success": f"Compensation audit completed for {employee_id}",
                "changes": changes_made,
                "new_compensation": new_comp,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "conditional_compensation_check_and_update",
                "description": "Check employee compensation against thresholds and update only if below thresholds, with equity adjustment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "compensation_id": {"type": "string"},
                        "effective_date": {
                            "type": "string",
                            "description": "Effective date (YYYY-MM-DD)",
                        },
                        "salary_threshold": {
                            "type": "number",
                            "description": "Minimum salary threshold to check against",
                        },
                        "target_salary": {
                            "type": "number",
                            "description": "Target salary if below threshold",
                        },
                        "bonus_threshold": {
                            "type": "number",
                            "description": "Minimum bonus percentage threshold to check against",
                        },
                        "target_bonus": {
                            "type": "number",
                            "description": "Target bonus percentage if below threshold",
                        },
                        "equity_increase_amount": {
                            "type": "number",
                            "description": "Fixed amount to add to equity grant",
                        },
                    },
                    "required": ["employee_id", "compensation_id", "effective_date"],
                    "additionalProperties": False,
                },
            },
        }
