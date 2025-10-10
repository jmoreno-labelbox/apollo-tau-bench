# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindWorkItemByTitle(Tool):
    """Finds a work item by its title."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        title_query = kwargs.get("title")
        work_items = data.get("work_items", [])
        for item in work_items:
            if title_query in item.get("title", ""):
                return json.dumps(item)
        return json.dumps({"error": f"No work item found with title containing '{title_query}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_work_item_by_title",
                "description": "Finds a work item by its title.",
                "parameters": {
                    "type": "object",
                    "properties": {"title": {"type": "string"}},
                    "required": ["title"],
                },
            },
        }
