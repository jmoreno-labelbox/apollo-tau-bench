# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class conditional_bonus_target_normalization(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str, compensation_id: str,
               effective_date: str, target_bonus_pct: float) -> str:
        # Retrieve the current compensation.
        comp = data.get("compensation_records", [])
        current = [c for c in comp if c["employee_id"] == employee_id]
        current.sort(key=lambda c: c["effective_date"], reverse=True)

        if not current:
            return json.dumps({"error": "No current compensation found for employee"}, indent=2)

        latest = current[0]
        current_bonus = latest.get("bonus_target_pct", 0)

        if current_bonus < target_bonus_pct:
            # Adjust bonus target to revert to default settings.
            new_comp = {
                "compensation_id": compensation_id,
                "employee_id": employee_id,
                "base_salary": latest["base_salary"],
                "currency": latest["currency"],
                "bonus_target_pct": target_bonus_pct,
                "equity_grant": latest["equity_grant"],
                "effective_date": effective_date
            }

            # Delete any existing record with the same ID before adding the new one.
            comp = [c for c in comp if c["compensation_id"] != compensation_id]
            comp.append(new_comp)
            data["compensation_records"] = comp

            return json.dumps({
                "success": f"Bonus target normalized for employee {employee_id}",
                "previous_bonus": current_bonus,
                "new_bonus": target_bonus_pct,
                "action_taken": f"Bonus increased from {current_bonus}% to {target_bonus_pct}%",
                "new_compensation": new_comp
            }, indent=2)
        else:
            return json.dumps({
                "success": f"Bonus target normalization skipped for employee {employee_id}",
                "current_bonus": current_bonus,
                "target_bonus": target_bonus_pct,
                "action_taken": f"Bonus {current_bonus}% already at or above target {target_bonus_pct}%"
            }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "conditional_bonus_target_normalization",
                "description": "Normalize employee bonus target to default level only if current bonus is below target.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "compensation_id": {"type": "string"},
                        "effective_date": {"type": "string", "description": "Effective date (YYYY-MM-DD)"},
                        "target_bonus_pct": {"type": "number", "description": "Target bonus percentage for normalization"}
                    },
                    "required": ["employee_id", "compensation_id", "effective_date", "target_bonus_pct"],
                    "additionalProperties": False
                }
            }
        }
