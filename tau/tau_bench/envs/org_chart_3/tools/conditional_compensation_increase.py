from tau_bench.envs.tool import Tool
import json
from typing import Any

class conditional_compensation_increase(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str,
        compensation_id: str,
        effective_date: str,
        condition: str,
        new_bonus_target_pct: float | None = None,
        new_salary: float | None = None,
        new_equity: float | None = None
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

        # Analyze and assess the condition
        should_update = False
        if "bonus_target_pct < 18" in condition:
            should_update = latest["bonus_target_pct"] < 18
        elif "base_salary < 75000" in condition:
            should_update = latest["base_salary"] < 75000
        # Include additional conditions as required

        if not should_update:
            payload = {
                    "success": f"Condition '{condition}' not met, no compensation change for {employee_id}"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Generate a new compensation record with the revised values
        new_comp = {
            "compensation_id": compensation_id,
            "employee_id": employee_id,
            "base_salary": (
                new_salary if new_salary is not None else latest["base_salary"]
            ),
            "currency": latest["currency"],
            "bonus_target_pct": (
                new_bonus_target_pct
                if new_bonus_target_pct is not None
                else latest["bonus_target_pct"]
            ),
            "equity_grant": (
                new_equity if new_equity is not None else latest["equity_grant"]
            ),
            "effective_date": effective_date,
        }

        # Delete the previous record with the same ID if it exists and insert the new one
        comp = [c for c in comp if c["compensation_id"] != compensation_id]
        comp.append(new_comp)
        data["compensation_records"] = comp
        payload = {
                "success": f"Compensation updated for {employee_id} based on condition '{condition}'",
                "new_compensation": new_comp,
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

        #Analyze and assess the condition
        should_update = False
        if "bonus_target_pct < 18" in condition:
            should_update = latest["bonus_target_pct"] < 18
        elif "base_salary < 75000" in condition:
            should_update = latest["base_salary"] < 75000
        #Include additional conditions as required

        if not should_update:
            payload = {
                    "success": f"Condition '{condition}' not met, no compensation change for {employee_id}"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #Generate a new compensation record with the revised values
        new_comp = {
            "compensation_id": compensation_id,
            "employee_id": employee_id,
            "base_salary": (
                new_salary if new_salary is not None else latest["base_salary"]
            ),
            "currency": latest["currency"],
            "bonus_target_pct": (
                new_bonus_target_pct
                if new_bonus_target_pct is not None
                else latest["bonus_target_pct"]
            ),
            "equity_grant": (
                new_equity if new_equity is not None else latest["equity_grant"]
            ),
            "effective_date": effective_date,
        }

        #Delete the previous record with the same ID if it exists and insert the new one
        comp = [c for c in comp if c["compensation_id"] != compensation_id]
        comp.append(new_comp)
        data["compensation_records"] = comp
        payload = {
                "success": f"Compensation updated for {employee_id} based on condition '{condition}'",
                "new_compensation": new_comp,
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
                "name": "ConditionalCompensationIncrease",
                "description": "Update employee compensation only if a specified condition is met.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "compensation_id": {"type": "string"},
                        "effective_date": {
                            "type": "string",
                            "description": "Effective date (YYYY-MM-DD)",
                        },
                        "condition": {
                            "type": "string",
                            "description": "Condition to check (e.g., 'bonus_target_pct < 18')",
                        },
                        "new_bonus_target_pct": {
                            "type": "number",
                            "description": "New bonus target percentage (optional)",
                        },
                        "new_salary": {
                            "type": "number",
                            "description": "New base salary (optional)",
                        },
                        "new_equity": {
                            "type": "number",
                            "description": "New equity grant (optional)",
                        },
                    },
                    "required": [
                        "employee_id",
                        "compensation_id",
                        "effective_date",
                        "condition",
                    ],
                    "additionalProperties": False,
                },
            },
        }
