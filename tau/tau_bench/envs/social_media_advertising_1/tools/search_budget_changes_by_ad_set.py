# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchBudgetChangesByAdSet(Tool):
    """Searches for budget changes for a specific ad set."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        changes = list(data.get("budget_changes", {}).values())
        matching_changes = []
        
        for change in changes:
            if change.get("adset_id") == adset_id:
                matching_changes.append(change.get("change_id"))
        
        return json.dumps({"budget_change_ids": matching_changes})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_budget_changes_by_adset",
                "description": "Searches for budget changes for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The ad set ID to search for.",
                        }
                    },
                    "required": ["adset_id"],
                },
            },
        }
