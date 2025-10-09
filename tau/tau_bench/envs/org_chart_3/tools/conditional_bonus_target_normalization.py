from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class conditional_bonus_target_normalization(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str,
        compensation_id: str,
        effective_date: str,
        target_bonus_pct: float
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
        current_bonus = latest.get("bonus_target_pct", 0)

        if current_bonus < target_bonus_pct:
            # Revise bonus target to align with default
            new_comp = {
                "compensation_id": compensation_id,
                "employee_id": employee_id,
                "base_salary": latest["base_salary"],
                "currency": latest["currency"],
                "bonus_target_pct": target_bonus_pct,
                "equity_grant": latest["equity_grant"],
                "effective_date": effective_date,
            }

            # Delete the previous record with the same ID if it exists and insert the new one
            comp = [c for c in comp if c["compensation_id"] != compensation_id]
            comp.append(new_comp)
            data["compensation_records"] = comp
            payload = {
                "success": f"Bonus target normalized for employee {employee_id}",
                "previous_bonus": current_bonus,
                "new_bonus": target_bonus_pct,
                "action_taken": f"Bonus increased from {current_bonus}% to {target_bonus_pct}%",
                "new_compensation": new_comp,
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = {
                "success": f"Bonus target normalization skipped for employee {employee_id}",
                "current_bonus": current_bonus,
                "target_bonus": target_bonus_pct,
                "action_taken": f"Bonus {current_bonus}% already at or above target {target_bonus_pct}%",
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
        current_bonus = latest.get("bonus_target_pct", 0)

        if current_bonus < target_bonus_pct:
            #Revise bonus target to align with default
            new_comp = {
                "compensation_id": compensation_id,
                "employee_id": employee_id,
                "base_salary": latest["base_salary"],
                "currency": latest["currency"],
                "bonus_target_pct": target_bonus_pct,
                "equity_grant": latest["equity_grant"],
                "effective_date": effective_date,
            }

            #Delete the previous record with the same ID if it exists and insert the new one
            comp = [c for c in comp if c["compensation_id"] != compensation_id]
            comp.append(new_comp)
            data["compensation_records"] = comp
            payload = {
                    "success": f"Bonus target normalized for employee {employee_id}",
                    "previous_bonus": current_bonus,
                    "new_bonus": target_bonus_pct,
                    "action_taken": f"Bonus increased from {current_bonus}% to {target_bonus_pct}%",
                    "new_compensation": new_comp,
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = {
                    "success": f"Bonus target normalization skipped for employee {employee_id}",
                    "current_bonus": current_bonus,
                    "target_bonus": target_bonus_pct,
                    "action_taken": f"Bonus {current_bonus}% already at or above target {target_bonus_pct}%",
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
                "name": "ConditionalBonusTargetNormalization",
                "description": "Normalize employee bonus target to default level only if current bonus is below target.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "compensation_id": {"type": "string"},
                        "effective_date": {
                            "type": "string",
                            "description": "Effective date (YYYY-MM-DD)",
                        },
                        "target_bonus_pct": {
                            "type": "number",
                            "description": "Target bonus percentage for normalization",
                        },
                    },
                    "required": [
                        "employee_id",
                        "compensation_id",
                        "effective_date",
                        "target_bonus_pct",
                    ],
                    "additionalProperties": False,
                },
            },
        }
