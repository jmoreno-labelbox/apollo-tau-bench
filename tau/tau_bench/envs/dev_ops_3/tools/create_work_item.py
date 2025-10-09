from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class create_work_item(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str,
        item_type: str,
        title: str,
        description: str,
    ) -> str:
        pass
        work_items = data.get("work_items", {}).values()
        existing_ids = [item["id"] for item in work_items.values()]
        new_id = _get_next_id("work", existing_ids)
        new_item = {
            "id": new_id,
            "project_id": project_id,
            "type": item_type,
            "title": title,
            "state": "open",
            "assignee_id": None,
            "created_at": FIXED_TIMESTAMP,
            "closed_at": None,
            "priority": "medium",
            "points": 5,
            "metadata": {"description": description},
        }
        data["work_items"][new_item["work_item_id"]] = new_item
        data["work_items"] = work_items
        payload = {
                "success": f"Created {item_type} ticket '{new_id}'",
                "work_item_id": new_id,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateWorkItem",
                "description": "Creates a new work item (e.g., bug, task, story).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"},
                        "item_type": {
                            "type": "string",
                            "enum": ["bug", "task", "story"],
                        },
                        "title": {"type": "string"},
                        "description": {"type": "string"},
                    },
                    "required": ["project_id", "item_type", "title", "description"],
                },
            },
        }
