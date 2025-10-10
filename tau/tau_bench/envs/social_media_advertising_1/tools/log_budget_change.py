# © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogBudgetChange(Tool):
    """Adds a new entry to the budget_changes table."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        old_budget = kwargs.get("old_budget")
        new_budget = kwargs.get("new_budget")
        changed_at = kwargs.get("changed_at")
        reason = kwargs.get("reason")
        
        if not adset_id:
            return json.dumps({"error": "adset_id is a required parameter."})
        if not old_budget:
            return json.dumps({"error": "old_budget is a required parameter."})
        if not new_budget:
            return json.dumps({"error": "new_budget is a required parameter."})
        if not changed_at:
            return json.dumps({"error": "changed_at is a required parameter."})
        if not reason:
            return json.dumps({"error": "reason is a required parameter."})

        new_budget_change = {
            "change_id": f"BC-{adset_id}",
            "adset_id": adset_id,
            "old_budget": old_budget,
            "new_budget": new_budget,
            "changed_at": changed_at,
            "reason": reason
        }
        
        if "budget_changes" not in data:
            data["budget_changes"] = []
            
        data['budget_changes'].append(new_budget_change)

        return json.dumps(
            {
                "status": "success",
                "message": f"New budget change was added: {new_budget_change}",
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_budget_change",
                "description": "Adds a new entry to the budget_changes table.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The ID of the ad set.",
                        },
                        "old_budget": {
                            "type": "number",
                            "description": "The old budget value.",
                        },
                        "new_budget": {
                            "type": "number",
                            "description": "The new budget value.",
                        },
                        "changed_at": {
                            "type": "string",
                            "description": "The timestamp of the change (ISO format).",
                        },
                        "reason": {
                            "type": "string",
                            "description": "The reason for the budget change.",
                        }
                    },
                    "required": ["change_id", "adset_id", "old_budget", "new_budget", "changed_at", "reason"],
                },
            },
        }
