# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _find






def _load(entity: str, data: Dict[str, Any]):
    """Return a *mutable copy* of a top-level collection list."""
    return [*data.get(entity, [])]

def _find(collection: List[Dict[str, Any]], entity_id: str):
    for idx, item in enumerate(collection):
        if item.get("id") == entity_id or item.get("reminder_id") == entity_id \
           or item.get("list_id") == entity_id or item.get("member_id") == entity_id:
            return idx, item
    return None, None

class DeleteReminder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], reminder_id: str) -> str:
        reminders = _load("reminders", data)
        idx, rem = _find(reminders, reminder_id)
        if idx is None:
            return json.dumps({"error": "reminder not found"}, indent=2)
        reminders.pop(idx)
        data["reminders"] = reminders
        return json.dumps({"success": "reminder deleted", "reminder": rem}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_reminder",
                "description": "Delete a reminder by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder_id": {"type": "string", "description": "Reminder id"}
                    },
                    "required": ["reminder_id"],
                    "additionalProperties": False
                }
            }
        }