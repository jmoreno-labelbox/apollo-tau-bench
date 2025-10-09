from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class increase_employee_compensation(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str,
        compensation_id: str,
        effective_date: str,
        salary_increase_pct: float | None = None,
        bonus_increase_pct: float | None = None,
        equity_increase_amount: float | None = None
    ) -> str:
        # Retrieve the current compensation
        comp = data.get("compensation_records", {}).values()
        current = [c for c in comp.values() if c["employee_id"] == employee_id]
        current.sort(key=lambda c: c["effective_date"], reverse=True)

        if not current:
            payload = {"error": "No current compensation found for employee"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        latest = current[0]

        # Compute new values
        new_salary = latest["base_salary"]
        new_bonus = latest["bonus_target_pct"]
        new_equity = latest["equity_grant"]

        if salary_increase_pct:
            new_salary = round(latest["base_salary"] * (1 + salary_increase_pct / 100))

        if bonus_increase_pct:
            new_bonus = latest["bonus_target_pct"] + bonus_increase_pct

        if equity_increase_amount:
            new_equity = latest["equity_grant"] + equity_increase_amount

        # Generate a new compensation record
        new_comp = {
            "compensation_id": compensation_id,
            "employee_id": employee_id,
            "base_salary": new_salary,
            "currency": latest["currency"],
            "bonus_target_pct": new_bonus,
            "equity_grant": new_equity,
            "effective_date": effective_date,
        }

        # Delete the old record with the same ID if it exists and insert the new one
        comp = [c for c in comp.values() if c["compensation_id"] != compensation_id]
        data["compensation_records"][new_comp["compensation_record_id"]] = new_comp
        data["compensation_records"] = comp
        payload = {
            "success": f"Compensation increased for {employee_id}",
            "new_compensation": new_comp,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        pass
        #Retrieve the current compensation
        comp = data.get("compensation_records", {}).values()
        current = [c for c in comp.values() if c["employee_id"] == employee_id]
        current.sort(key=lambda c: c["effective_date"], reverse=True)

        if not current:
            payload = {"error": "No current compensation found for employee"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        latest = current[0]

        #Compute new values
        new_salary = latest["base_salary"]
        new_bonus = latest["bonus_target_pct"]
        new_equity = latest["equity_grant"]

        if salary_increase_pct:
            new_salary = round(latest["base_salary"] * (1 + salary_increase_pct / 100))

        if bonus_increase_pct:
            new_bonus = latest["bonus_target_pct"] + bonus_increase_pct

        if equity_increase_amount:
            new_equity = latest["equity_grant"] + equity_increase_amount

        #Generate a new compensation record
        new_comp = {
            "compensation_id": compensation_id,
            "employee_id": employee_id,
            "base_salary": new_salary,
            "currency": latest["currency"],
            "bonus_target_pct": new_bonus,
            "equity_grant": new_equity,
            "effective_date": effective_date,
        }

        #Delete the old record with the same ID if it exists and insert the new one
        comp = [c for c in comp.values() if c["compensation_id"] != compensation_id]
        data["compensation_records"][new_comp["compensation_record_id"]] = new_comp
        data["compensation_records"] = comp
        payload = {
                "success": f"Compensation increased for {employee_id}",
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
                "name": "IncreaseEmployeeCompensation",
                "description": "Increase employee compensation by percentage or fixed amount based on current values.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "compensation_id": {
                            "type": "string",
                            "description": "New compensation record ID",
                        },
                        "effective_date": {
                            "type": "string",
                            "description": "Effective date for the increase (YYYY-MM-DD)",
                        },
                        "salary_increase_pct": {
                            "type": "number",
                            "description": "Percentage to increase base salary (optional)",
                        },
                        "bonus_increase_pct": {
                            "type": "number",
                            "description": "Percentage points to increase bonus target (optional)",
                        },
                        "equity_increase_amount": {
                            "type": "number",
                            "description": "Fixed amount to add to equity grant (optional)",
                        },
                    },
                    "required": ["employee_id", "compensation_id", "effective_date"],
                    "additionalProperties": False,
                },
            },
        }
