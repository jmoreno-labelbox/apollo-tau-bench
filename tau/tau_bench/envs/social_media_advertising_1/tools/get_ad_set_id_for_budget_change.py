# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAdSetIdForBudgetChange(Tool):
    """Retrieves the ad set ID for a specific budget change."""

    @staticmethod
    def invoke(data: Dict[str, Any], change_id) -> str:
        changes = list(data.get("budget_changes", {}).values())
        
        for change in changes:
            if change.get("change_id") == change_id:
                return json.dumps({"adset_id": change.get('adset_id')})
        
        return json.dumps({"error": f"Budget change with ID '{change_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_adset_id_for_budget_change",
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
