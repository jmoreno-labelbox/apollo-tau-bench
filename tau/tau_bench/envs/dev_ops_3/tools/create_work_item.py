# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class create_work_item(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], project_id: str, item_type: str, title: str, description: str) -> str:
        work_items = data.get("work_items", [])
        existing_ids = [item['id'] for item in work_items]
        new_id = _get_next_id("work", existing_ids)
        new_item = {"id": new_id, "project_id": project_id, "type": item_type, "title": title, "state": "open", "assignee_id": None, "created_at": FIXED_TIMESTAMP, "closed_at": None, "priority": "medium", "points": 5, "metadata": {"description": description}}
        work_items.append(new_item)
        data["work_items"] = work_items
        return json.dumps({"success": f"Created {item_type} ticket '{new_id}'", "work_item_id": new_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return { "type": "function", "function": { "name": "create_work_item", "description": "Creates a new work item (e.g., bug, task, story).", "parameters": { "type": "object", "properties": { "project_id": { "type": "string" }, "item_type": { "type": "string", "enum": ["bug", "task", "story"] }, "title": { "type": "string" }, "description": { "type": "string" } }, "required": ["project_id", "item_type", "title", "description"] } } }
