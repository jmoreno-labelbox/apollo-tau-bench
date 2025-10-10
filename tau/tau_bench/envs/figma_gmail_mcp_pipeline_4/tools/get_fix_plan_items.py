# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetFixPlanItems(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves fix items for one or more fix plans with filtering options.
        """
        plan_ids = kwargs.get('plan_ids', [])
        status_filter = kwargs.get('status')
        severity_filter = kwargs.get('severity')
        include_resolved = kwargs.get('include_resolved', False)
        limit = kwargs.get('limit', 50)

        if not plan_ids and 'plan_id' in kwargs:
            plan_ids = [kwargs['plan_id']]

        if not plan_ids:
            return json.dumps({"error": "At least one plan_id is required"})

        fix_plans = data.get('fix_plans', [])
        fix_items = data.get('fix_items', [])

        result = []
        for plan_id in plan_ids:
            plan = next((p for p in fix_plans if p.get('plan_id') == plan_id), None)
            if not plan:
                continue

            plan_items = [
                item for item in fix_items
                if item.get('plan_id') == plan_id and
                   (include_resolved or item.get('status') != 'RESOLVED')
            ]

            if status_filter:
                plan_items = [item for item in plan_items if item.get('status') == status_filter]
            if severity_filter:
                plan_items = [item for item in plan_items if item.get('severity') == severity_filter]

            if plan_items:
                result.append({
                    'plan_id': plan_id,
                    'plan_name': plan.get('name', ''),
                    'status': plan.get('status', ''),
                    'items': plan_items[:limit]
                })

        return json.dumps({
            'total_plans': len(result),
            'total_items': sum(len(plan['items']) for plan in result),
            'plans': result
        }, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_fix_plan_items",
                "description": "Retrieves fix items for one or more fix plans with filtering options.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of fix plan IDs to retrieve items for"
                        },
                        "plan_id": {
                            "type": "string",
                            "description": "Single fix plan ID (alternative to plan_ids)"
                        },
                        "status": {
                            "type": "string",
                            "description": "Filter items by status (e.g., 'OPEN', 'IN_PROGRESS', 'RESOLVED')"
                        },
                        "severity": {
                            "type": "string",
                            "description": "Filter items by severity (e.g., 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL')"
                        },
                        "include_resolved": {
                            "type": "boolean",
                            "default": False,
                            "description": "Include resolved items in results"
                        },
                        "limit": {
                            "type": "integer",
                            "default": 50,
                            "description": "Maximum number of items to return per plan"
                        }
                    },
                    "anyOf": [
                        {"required": ["plan_ids"]},
                        {"required": ["plan_id"]}
                    ]
                }
            }
        }
