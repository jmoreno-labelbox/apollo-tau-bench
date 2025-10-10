# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class update_benefit_plan(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], benefit_plan_id: str, updates: Dict[str, Any]) -> str:
        bp = data.get("benefit_plans", [])

        for p in bp:
            if p["benefit_plan_id"] == benefit_plan_id:
                p.update(updates)
                data["benefit_plans"] = bp
                return json.dumps({"success": f"benefit_plan {benefit_plan_id} updated"}, indent=2)

        return json.dumps({"error": f"benefit_plan_id {benefit_plan_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_benefit_plan",
                "description": "Patch fields of an existing benefit plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "benefit_plan_id": {"type": "string"},
                        "updates": {"type": "object"}
                    },
                    "required": ["benefit_plan_id", "updates"],
                    "additionalProperties": False
                }
            }
        }
