# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class create_benefit_plan(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], benefit_plan: Dict[str, Any]) -> str:
        if not benefit_plan:
            return json.dumps({"error": "benefit_plan record required"}, indent=2)
        bp = data.get("benefits_plan", [])
        bp.append(benefit_plan)
        data["benefits_plan"] = bp
        return json.dumps(
            {"success": f'benefit_plan {benefit_plan["benefit_plan_id"]} added'},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_benefit_plan",
                "description": "Create a new benefit plan definition.",
                "parameters": {
                    "type": "object",
                    "properties": {"benefit_plan": {"type": "object"}},
                    "required": ["benefit_plan"],
                    "additionalProperties": False,
                },
            },
        }
