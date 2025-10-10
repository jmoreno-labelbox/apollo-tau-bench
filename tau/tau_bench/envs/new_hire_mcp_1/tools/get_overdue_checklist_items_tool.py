# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOverdueChecklistItemsTool(Tool):
    """Queries checklist_items for tasks past due date, grouped by candidate and task priority."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        days_overdue_threshold = _as_int(kwargs.get("days_overdue_threshold", 0))

        if days_overdue_threshold is None:
            return _err("days_overdue_threshold must be an integer.")

        checklist_items = data.get("checklist_items", [])

        overdue_items = []
        for item in checklist_items:
            due_date = item.get("due_date")
            if not due_date or item.get("status") == "Completed":
                continue

            days_overdue = _days_between(due_date, HARD_TS)

            if days_overdue >= days_overdue_threshold:
                if candidate_id is None or str(item.get("candidate_id")) == str(candidate_id):
                    item_copy = item.copy()
                    item_copy["days_overdue"] = days_overdue
                    overdue_items.append(item_copy)

        # Group by candidate
        grouped_results = {}
        for item in overdue_items:
            cid = item.get("candidate_id")
            if cid not in grouped_results:
                grouped_results[cid] = []
            grouped_results[cid].append(item)

        return json.dumps(grouped_results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_overdue_checklist_items",
                "description": "Queries checklist_items for tasks past due date, grouped by candidate and task priority.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string", "description": "Specific candidate or null for all candidates"},
                        "days_overdue_threshold": {"type": "integer", "description": "Minimum days past due date"}
                    },
                    "required": ["days_overdue_threshold"],
                },
            },
        }
