# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetBudgetChanges(Tool):
    """Retrieves all budget change IDs."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        changes = data.get("budget_changes", [])
        ids_ = []
        for i in changes:
            ids_ += [i.get("change_id")]
        return json.dumps({"budget_change_ids": ids_})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_budget_changes",
                "description": "Retrieves all budget change IDs.",
                "parameters": {},
            },
        }
