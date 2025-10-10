# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateWorkItem(Tool):
    """Creates a new work item like a bug, task, or incident."""
    @staticmethod
    def invoke(data: Dict[str, Any], assignee_id, project_id, title, type, description = '', points = 0, priority = 'high', state = "open") -> str:
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
            "created_at": "2025-01-28T00:00:00Z", # Temporary timestamp
            "closed_at": None,
            "priority": priority,
            "points": points,
            "metadata": {"description": description}
        }
        work_items.append(new_item)
        return json.dumps(new_item)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_work_item",
                "description": "Creates a new work item (bug, task, story, incident).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"},
                        "type": {"type": "string", "enum": ["bug", "task", "story", "epic", "incident"]},
                        "title": {"type": "string"},
                        "description": {"type": "string"},
                        "assignee_id": {"type": "string"},
                        "priority": {"type": "string", "enum": ["low", "medium", "high", "critical"]},
                        "state": {"type": "string"},
                        "points": {"type": "integer"}
                    },
                    "required": ["project_id", "type", "title"],
                },
            },
        }
