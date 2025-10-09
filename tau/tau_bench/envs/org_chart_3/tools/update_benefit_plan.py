from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class update_benefit_plan(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], benefit_plan_id: str, updates: dict[str, Any]
    ) -> str:
        bp = data.get("benefit_plans", [])

        for p in bp:
            if p["benefit_plan_id"] == benefit_plan_id:
                p.update(updates)
                data["benefit_plans"] = bp
                payload = {"success": f"benefit_plan {benefit_plan_id} updated"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"benefit_plan_id {benefit_plan_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
        pass
        bp = data.get("benefit_plans", [])

        for p in bp:
            if p["benefit_plan_id"] == benefit_plan_id:
                p.update(updates)
                data["benefit_plans"] = bp
                payload = {"success": f"benefit_plan {benefit_plan_id} updated"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"benefit_plan_id {benefit_plan_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateBenefitPlan",
                "description": "Patch fields of an existing benefit plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "benefit_plan_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["benefit_plan_id", "updates"],
                    "additionalProperties": False,
                },
            },
        }
