from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FindWorkItemByTitle(Tool):
    """Locates a work item using its title."""

    @staticmethod
    def invoke(data: dict[str, Any], title: str = None) -> str:
        title_query = title
        work_items = data.get("work_items", [])
        for item in work_items:
            if title_query in item.get("title", ""):
                payload = item
                out = json.dumps(payload)
                return out
        payload = {"error": f"No work item found with title containing '{title_query}'."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindWorkItemByTitle",
                "description": "Finds a work item by its title.",
                "parameters": {
                    "type": "object",
                    "properties": {"title": {"type": "string"}},
                    "required": ["title"],
                },
            },
        }
