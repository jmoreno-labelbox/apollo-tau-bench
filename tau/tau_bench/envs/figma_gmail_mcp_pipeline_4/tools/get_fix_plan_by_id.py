# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetFixPlanById(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves a specific fix plan by its ID with detailed information.
        """
        plan_id = kwargs.get('plan_id')
        include_items = kwargs.get('include_items', True)

        if not plan_id:
            return json.dumps({"error": "plan_id is required"})

        fix_plans = data.get('fix_plans', [])
        fix_items = data.get('fix_items', [])

        # Locate the proposed solution outline.
        plan = next((p for p in fix_plans if p.get('plan_id') == plan_id), None)
        if not plan:
            return json.dumps({"error": f"Fix plan with ID '{plan_id}' not found"})

        result = dict(plan)  # Duplicate the plan.

        # Add associated items upon request.
        if include_items:
            result['items'] = [
                item for item in fix_items
                if item.get('plan_id') == plan_id
            ]

        # Incorporate extra metadata.
        result['item_count'] = len(result.get('items', []))
        result['open_item_count'] = len([i for i in result.get('items', [])
                                       if i.get('status') != 'RESOLVED'])

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_fix_plan_by_id",
                "description": "Retrieves a specific fix plan by its ID with detailed information.",
                "parameters": {
                    "type": "object",
                    "required": ["plan_id"],
                    "properties": {
                        "plan_id": {
                            "type": "string",
                            "description": "The ID of the fix plan to retrieve"
                        },
                        "include_items": {
                            "type": "boolean",
                            "default": True,
                            "description": "Whether to include the fix items in the response"
                        }
                    }
                }
            }
        }
