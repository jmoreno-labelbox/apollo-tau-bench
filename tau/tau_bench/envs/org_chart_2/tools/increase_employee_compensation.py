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
        equity_increase_amount: int | None = None,
    ) -> str:
        comp_records = data.get("compensation_records", {}).values()
        # Retrieve the current compensation
        current_comp_list = [c for c in comp_records.values() if c["employee_id"] == employee_id]
        if not current_comp_list:
            payload = {
                "error": f"No compensation record found for employee_id {employee_id}"
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        current_comp_list.sort(key=lambda c: c["effective_date"], reverse=True)
        current_comp = current_comp_list[0]

        # Begin with existing values
        new_comp = current_comp.copy()

        # Revise with the new necessary values
        new_comp["compensation_id"] = compensation_id
        new_comp["effective_date"] = effective_date

        # Determine new salary if relevant
        if salary_increase_pct is not None:
            new_comp["base_salary"] = int(
                current_comp["base_salary"] * (1 + salary_increase_pct / 100)
            )

        # Assess new equity if relevant
        if equity_increase_amount is not None:
            new_comp["equity_grant"] = (
                current_comp["equity_grant"] + equity_increase_amount
            )

        # Insert the new record while maintaining history
        data["compensation_records"][new_comp["compensation_record_id"]] = new_comp
        data["compensation_records"] = comp_records
        payload = {
            "success": f"New compensation record {compensation_id} created for {employee_id}",
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
