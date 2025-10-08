from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateWorkItem(Tool):
    """Generates a new work item such as a bug, task, or incident."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str,
        type: str,
        title: str,
        state: str = "open",
        assignee_id: str = None,
        priority: str = "high",
        points: int = 0,
        description: str = ""
    ) -> str:
        pass
        work_items = data.get("work_items", [])
        new_id_num = max([int(w["id"].split("_")[1]) for w in work_items]) + 1
        new_id = f"work_{new_id_num:03d}"

        new_item = {
            "id": new_id,
            "project_id": project_id,
            "type": type,
            "title": title,
            "state": state,
            "assignee_id": assignee_id,
            "created_at": "2025-01-28T00:00:00Z",  # Temporary timestamp
            "closed_at": None,
            "priority": priority,
            "points": points,
            "metadata": {"description": description},
        }
        work_items.append(new_item)
        payload = new_item
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateWorkItem",
                "description": "Creates a new work item (bug, task, story, incident).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"},
                        "type": {
                            "type": "string",
                            "enum": ["bug", "task", "story", "epic", "incident"],
                        },
                        "title": {"type": "string"},
                        "description": {"type": "string"},
                        "assignee_id": {"type": "string"},
                        "priority": {
                            "type": "string",
                            "enum": ["low", "medium", "high", "critical"],
                        },
                        "state": {"type": "string"},
                        "points": {"type": "integer"},
                    },
                    "required": ["project_id", "type", "title"],
                },
            },
        }
