from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class GetFixPlanById(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], plan_id: str = None, include_items: bool = True) -> str:
        """
        Obtains a specific fix plan using its ID along with detailed information.
        """
        if not plan_id:
            payload = {"error": "plan_id is required"}
            out = json.dumps(payload)
            return out

        fix_plans = data.get("fix_plans", [])
        fix_items = data.get("fix_items", [])

        # Locate the requested fix plan
        plan = next((p for p in fix_plans if p.get("plan_id") == plan_id), None)
        if not plan:
            payload = {"error": f"Fix plan with ID '{plan_id}' not found"}
            out = json.dumps(payload)
            return out

        result = dict(plan)  # Generate a duplicate of the plan

        # Add related items if requested
        if include_items:
            result["items"] = [
                item for item in fix_items if item.get("plan_id") == plan_id
            ]

        # Include extra metadata
        result["item_count"] = len(result.get("items", []))
        result["open_item_count"] = len(
            [i for i in result.get("items", []) if i.get("status") != "RESOLVED"]
        )
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getFixPlanById",
                "description": "Retrieves a specific fix plan by its ID with detailed information.",
                "parameters": {
                    "type": "object",
                    "required": ["plan_id"],
                    "properties": {
                        "plan_id": {
                            "type": "string",
                            "description": "The ID of the fix plan to retrieve",
                        },
                        "include_items": {
                            "type": "boolean",
                            "default": True,
                            "description": "Whether to include the fix items in the response",
                        },
                    },
                },
            },
        }
