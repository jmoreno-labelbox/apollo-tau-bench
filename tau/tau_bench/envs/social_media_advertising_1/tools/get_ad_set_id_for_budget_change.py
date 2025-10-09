from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetAdSetIdForBudgetChange(Tool):
    """Fetches the ad set ID linked to a specific budget change."""

    @staticmethod
    def invoke(data: dict[str, Any], change_id: str = None) -> str:
        changes = data.get("budget_changes", [])

        for change in changes:
            if change.get("change_id") == change_id:
                payload = {"adset_id": change.get("adset_id")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Budget change with ID '{change_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAdsetIdForBudgetChange",
                "description": "Retrieves the ad set ID for a specific budget change.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "change_id": {
                            "type": "string",
                            "description": "The unique ID of the budget change.",
                        }
                    },
                    "required": ["change_id"],
                },
            },
        }
