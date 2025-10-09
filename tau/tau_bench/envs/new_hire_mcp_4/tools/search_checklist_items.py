from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SearchChecklistItems(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str, status: str = None, due_date_lte: str = None) -> str:
        rows = []
        for it in data.get("checklist_items", {}).values():
            if it.get("candidate_id") != candidate_id:
                continue
            if status and it.get("status") != status:
                continue
            if due_date_lte and it.get("due_date") and it["due_date"] > due_date_lte:
                continue
            rows.append(it)
        payload = {"items": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchChecklistItems",
                "description": "Search checklist items for a candidate with simple filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "status": {"type": "string"},
                        "due_date_lte": {"type": "string"},
                    },
                    "required": ["candidate_id"],
                },
            },
        }
