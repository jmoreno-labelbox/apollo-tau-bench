from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class LogBudgetChange(Tool):
    """Inserts a new record into the budget_changes table."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, old_budget: float = None, new_budget: float = None, changed_at: str = None, reason: str = None) -> str:
        if not adset_id:
            payload = {"error": "adset_id is a required parameter."}
            out = json.dumps(payload)
            return out
        if not old_budget:
            payload = {"error": "old_budget is a required parameter."}
            out = json.dumps(payload)
            return out
        if not new_budget:
            payload = {"error": "new_budget is a required parameter."}
            out = json.dumps(payload)
            return out
        if not changed_at:
            payload = {"error": "changed_at is a required parameter."}
            out = json.dumps(payload)
            return out
        if not reason:
            payload = {"error": "reason is a required parameter."}
            out = json.dumps(payload)
            return out

        new_budget_change = {
            "change_id": f"BC-{adset_id}",
            "adset_id": adset_id,
            "old_budget": old_budget,
            "new_budget": new_budget,
            "changed_at": changed_at,
            "reason": reason,
        }

        if "budget_changes" not in data:
            data["budget_changes"] = []

        data["budget_changes"].append(new_budget_change)
        payload = {
                "status": "success",
                "message": f"New budget change was added: {new_budget_change}",
            }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogBudgetChange",
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
                        },
                    },
                    "required": [
                        "change_id",
                        "adset_id",
                        "old_budget",
                        "new_budget",
                        "changed_at",
                        "reason",
                    ],
                },
            },
        }
