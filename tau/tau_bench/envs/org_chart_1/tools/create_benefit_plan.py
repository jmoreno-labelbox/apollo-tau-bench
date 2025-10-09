from tau_bench.envs.tool import Tool
import json
from typing import Any

class create_benefit_plan(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], benefit_plan: dict[str, Any]) -> str:
        if not benefit_plan:
            payload = {"error": "benefit_plan record required"}
            out = json.dumps(payload, indent=2)
            return out
        bp = data.get("benefits_plan", [])
        bp.append(benefit_plan)
        data["benefits_plan"] = bp
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
                "name": "CreateBenefitPlan",
                "description": "Create a new benefit plan definition.",
                "parameters": {
                    "type": "object",
                    "properties": {"benefit_plan": {"type": "object"}},
                    "required": ["benefit_plan"],
                    "additionalProperties": False,
                },
            },
        }
