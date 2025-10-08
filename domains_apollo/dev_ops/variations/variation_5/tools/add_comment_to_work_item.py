from tau_bench.envs.tool import Tool
import json
from typing import Any

class AddCommentToWorkItem(Tool):
    """Inserts a comment into a work item."""

    @staticmethod
    def invoke(data: dict[str, Any], id: str = None, comment: str = None) -> str:
        work_item_id = id
        work_items = data.get("work_items", [])
        for item in work_items:
            if item.get("id", "") == work_item_id:
                break
        else:
            payload = {
                    "status": "error",
                    "message": f"Work item with id '{work_item_id}' not found.",
                }
            out = json.dumps(
                payload)
            return out
        comments = item.get("comments", [])
        comments += [comment]
        item["comments"] = comments
        payload = {
                "status": "success",
                "message": f"Comment '{comment}' added to work item '{work_item_id}'.",
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddCommentToWorkItem",
                "description": "Adds a comment to a work item.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "comment": {"type": "string"},
                    },
                    "required": ["id", "comment"],
                },
            },
        }
