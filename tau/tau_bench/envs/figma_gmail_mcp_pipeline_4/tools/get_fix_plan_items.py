from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetFixPlanItems(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        plan_ids: list[str] = None,
        status: str = None,
        severity: str = None,
        include_resolved: bool = False,
        limit: int = 50,
        plan_id: str = None
    ) -> str:
        """
        Obtains fix items for one or more fix plans with available filtering options.
        """
        if plan_ids is None:
            plan_ids = []

        if not plan_ids and plan_id:
            plan_ids = [plan_id]

        if not plan_ids:
            payload = {"error": "At least one plan_id is required"}
            out = json.dumps(payload)
            return out

        fix_plans = data.get("fix_plans", [])
        fix_items = data.get("fix_items", [])

        result = []
        for plan_id in plan_ids:
            plan = next((p for p in fix_plans if p.get("plan_id") == plan_id), None)
            if not plan:
                continue

            plan_items = [
                item
                for item in fix_items
                if item.get("plan_id") == plan_id
                and (include_resolved or item.get("status") != "RESOLVED")
            ]

            if status:
                plan_items = [
                    item for item in plan_items if item.get("status") == status
                ]
            if severity:
                plan_items = [
                    item
                    for item in plan_items
                    if item.get("severity") == severity
                ]

            if plan_items:
                result.append(
                    {
                        "plan_id": plan_id,
                        "plan_name": plan.get("name", ""),
                        "status": plan.get("status", ""),
                        "items": plan_items[:limit],
                    }
                )
        payload = {
                "total_plans": len(result),
                "total_items": sum(len(plan["items"]) for plan in result),
                "plans": result,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetFixPlanItems",
                "description": "Retrieves fix items for one or more fix plans with filtering options.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of fix plan IDs to retrieve items for",
                        },
                        "plan_id": {
                            "type": "string",
                            "description": "Single fix plan ID (alternative to plan_ids)",
                        },
                        "status": {
                            "type": "string",
                            "description": "Filter items by status (e.g., 'OPEN', 'IN_PROGRESS', 'RESOLVED')",
                        },
                        "severity": {
                            "type": "string",
                            "description": "Filter items by severity (e.g., 'LOW', 'MEDIUM', 'HIGH', 'CRITICAL')",
                        },
                        "include_resolved": {
                            "type": "boolean",
                            "default": False,
                            "description": "Include resolved items in results",
                        },
                        "limit": {
                            "type": "integer",
                            "default": 50,
                            "description": "Maximum number of items to return per plan",
                        },
                    },
},
            },
        }
