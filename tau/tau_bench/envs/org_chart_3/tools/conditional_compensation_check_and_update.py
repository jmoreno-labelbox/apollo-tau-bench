from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class conditional_compensation_check_and_update(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str,
        compensation_id: str,
        effective_date: str,
        salary_threshold: float | None = None,
        target_salary: float | None = None,
        bonus_threshold: float | None = None,
        target_bonus: float | None = None
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
        changes_made = []

        # Begin with the existing values
        new_salary = latest["base_salary"]
        new_bonus = latest["bonus_target_pct"]

        # Evaluate the salary condition
        if salary_threshold is not None and target_salary is not None:
            if latest["base_salary"] < salary_threshold:
                new_salary = target_salary
                changes_made.append(
                    f"salary increased from {latest['base_salary']} to {target_salary}"
                )
            else:
                changes_made.append(
                    f"salary {latest['base_salary']} already above threshold {salary_threshold}"
                )

        # Evaluate the bonus condition
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

        # Generate a new record only if modifications occurred
        if (
            new_salary != latest["base_salary"]
            or new_bonus != latest["bonus_target_pct"]
        ):
            new_comp = {
                "compensation_id": compensation_id,
                "employee_id": employee_id,
                "base_salary": new_salary,
                "currency": latest["currency"],
                "bonus_target_pct": new_bonus,
                "equity_grant": latest["equity_grant"],
                "effective_date": effective_date,
            }

            # Delete the previous record with the same ID if it exists and insert the new one
            comp = [c for c in comp.values() if c["compensation_id"] != compensation_id]
            data["compensation_records"][new_comp["compensation_record_id"]] = new_comp
            data["compensation_records"] = comp
            payload = {
                    "success": f"Compensation updated for {employee_id}",
                    "changes": changes_made,
                    "new_compensation": new_comp,
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = {
                    "success": f"No compensation changes needed for {employee_id}",
                    "analysis": changes_made,
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
        changes_made = []

        #Begin with the existing values
        new_salary = latest["base_salary"]
        new_bonus = latest["bonus_target_pct"]

        #Evaluate the salary condition
        if salary_threshold is not None and target_salary is not None:
            if latest["base_salary"] < salary_threshold:
                new_salary = target_salary
                changes_made.append(
                    f"salary increased from {latest['base_salary']} to {target_salary}"
                )
            else:
                changes_made.append(
                    f"salary {latest['base_salary']} already above threshold {salary_threshold}"
                )

        #Evaluate the bonus condition
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

        #Generate a new record only if modifications occurred
        if (
            new_salary != latest["base_salary"]
            or new_bonus != latest["bonus_target_pct"]
        ):
            new_comp = {
                "compensation_id": compensation_id,
                "employee_id": employee_id,
                "base_salary": new_salary,
                "currency": latest["currency"],
                "bonus_target_pct": new_bonus,
                "equity_grant": latest["equity_grant"],
                "effective_date": effective_date,
            }

            #Delete the previous record with the same ID if it exists and insert the new one
            comp = [c for c in comp.values() if c["compensation_id"] != compensation_id]
            data["compensation_records"][new_comp["compensation_record_id"]] = new_comp
            data["compensation_records"] = comp
            payload = {
                    "success": f"Compensation updated for {employee_id}",
                    "changes": changes_made,
                    "new_compensation": new_comp,
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = {
                    "success": f"No compensation changes needed for {employee_id}",
                    "analysis": changes_made,
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
                "name": "ConditionalCompensationCheckAndUpdate",
                "description": "Check employee compensation against thresholds and update only if below thresholds.",
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
                    },
                    "required": ["employee_id", "compensation_id", "effective_date"],
                    "additionalProperties": False,
                },
            },
        }
