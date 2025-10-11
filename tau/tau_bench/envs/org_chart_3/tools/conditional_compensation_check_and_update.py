# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class conditional_compensation_check_and_update(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str, compensation_id: str, effective_date: str,
               salary_threshold: Optional[float] = None, target_salary: Optional[float] = None,
               bonus_threshold: Optional[float] = None, target_bonus: Optional[float] = None) -> str:
        # Retrieve current salary information.
        comp = data.get("compensation_records", [])
        current = [c for c in comp if c["employee_id"] == employee_id]
        current.sort(key=lambda c: c["effective_date"], reverse=True)

        if not current:
            return json.dumps({"error": "No current compensation found for employee"}, indent=2)

        latest = current[0]
        changes_made = []

        # Initialize with existing values.
        new_salary = latest["base_salary"]
        new_bonus = latest["bonus_target_pct"]

        # Verify salary criteria
        if salary_threshold is not None and target_salary is not None:
            if latest["base_salary"] < salary_threshold:
                new_salary = target_salary
                changes_made.append(f"salary increased from {latest['base_salary']} to {target_salary}")
            else:
                changes_made.append(f"salary {latest['base_salary']} already above threshold {salary_threshold}")

        # Verify bonus requirements
        if bonus_threshold is not None and target_bonus is not None:
            if latest["bonus_target_pct"] < bonus_threshold:
                new_bonus = target_bonus
                changes_made.append(f"bonus increased from {latest['bonus_target_pct']}% to {target_bonus}%")
            else:
                changes_made.append(f"bonus {latest['bonus_target_pct']}% already above threshold {bonus_threshold}%")

        # Generate a new record solely if modifications occurred.
        if new_salary != latest["base_salary"] or new_bonus != latest["bonus_target_pct"]:
            new_comp = {
                "compensation_id": compensation_id,
                "employee_id": employee_id,
                "base_salary": new_salary,
                "currency": latest["currency"],
                "bonus_target_pct": new_bonus,
                "equity_grant": latest["equity_grant"],
                "effective_date": effective_date
            }

            # Delete any existing record with the same ID before adding the new one.
            comp = [c for c in comp if c["compensation_id"] != compensation_id]
            comp.append(new_comp)
            data["compensation_records"] = comp

            return json.dumps({
                "success": f"Compensation updated for {employee_id}",
                "changes": changes_made,
                "new_compensation": new_comp
            }, indent=2)
        else:
            return json.dumps({
                "success": f"No compensation changes needed for {employee_id}",
                "analysis": changes_made
            }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "conditional_compensation_check_and_update",
                "description": "Check employee compensation against thresholds and update only if below thresholds.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "compensation_id": {"type": "string"},
                        "effective_date": {"type": "string", "description": "Effective date (YYYY-MM-DD)"},
                        "salary_threshold": {"type": "number", "description": "Minimum salary threshold to check against"},
                        "target_salary": {"type": "number", "description": "Target salary if below threshold"},
                        "bonus_threshold": {"type": "number", "description": "Minimum bonus percentage threshold to check against"},
                        "target_bonus": {"type": "number", "description": "Target bonus percentage if below threshold"}
                    },
                    "required": ["employee_id", "compensation_id", "effective_date"],
                    "additionalProperties": False
                }
            }
        }
