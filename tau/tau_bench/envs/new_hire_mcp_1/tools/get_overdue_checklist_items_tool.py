from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetOverdueChecklistItemsTool(Tool):
    """Searches checklist_items for overdue tasks, organized by candidate and task priority."""

    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str = None, days_overdue_threshold: int = 0) -> str:
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

        # Organize by candidate
        grouped_results = {}
        for item in overdue_items:
            cid = item.get("candidate_id")
            if cid not in grouped_results:
                grouped_results[cid] = []
            grouped_results[cid].append(item)
        payload = grouped_results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOverdueChecklistItems",
                "description": "Queries checklist_items for tasks past due date, grouped by candidate and task priority.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {
                            "type": "string",
                            "description": "Specific candidate or null for all candidates",
                        },
                        "days_overdue_threshold": {
                            "type": "integer",
                            "description": "Minimum days past due date",
                        },
                    },
                    "required": ["days_overdue_threshold"],
                },
            },
        }
