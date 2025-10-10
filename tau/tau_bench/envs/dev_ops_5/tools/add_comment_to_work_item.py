# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddCommentToWorkItem(Tool):
    """Adds a comment to a work item."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        work_item_id = kwargs.get("id")
        work_items = data.get("work_items", [])
        for item in work_items:
            if item.get("id", '') == work_item_id:
                break
        else:
            return json.dumps({"status": "error", "message": f"Work item with id '{work_item_id}' not found."})
        comment = kwargs.get("comment")
        comments = item.get('comments', [])
        comments += [comment]
        item['comments'] = comments
        return json.dumps({"status": "success", "message": f"Comment '{comment}' added to work item '{work_item_id}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_comment_to_work_item",
                "description": "Adds a comment to a work item.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "comment": {"type": "string"}
                    },
                    "required": ["id", "comment"],
                },
            },
        }
