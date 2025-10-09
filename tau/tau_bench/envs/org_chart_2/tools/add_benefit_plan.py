from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class add_benefit_plan(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], benefit_plan: dict[str, Any]) -> str:
        if not benefit_plan:
            payload = {"error": "benefit_plan record required"}
            out = json.dumps(payload, indent=2)
            return out
        bp = data.get("benefit_plans", {}).values()
        data["benefit_plans"][benefit_plan["benefit_plan_id"]] = benefit_plan
        data["benefit_plans"] = bp
        payload = {"success": f'benefit_plan {benefit_plan["benefit_plan_id"]} added'}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddBenefitPlan",
                "description": "Create a new benefit plan definition.",
                "parameters": {
                    "type": "object",
                    "properties": {"benefit_plan": {"type": "object"}},
                    "required": ["benefit_plan"],
                    "additionalProperties": False,
                },
            },
        }
