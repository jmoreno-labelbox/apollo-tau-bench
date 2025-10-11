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

class UpsertReminder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], reminder: Dict[str, Any]) -> str:
        if not reminder:
            return json.dumps({"error": "reminder object required"}, indent=2)
        reminders = _load("reminders", data)
        idx, _ = _find(reminders, reminder["reminder_id"])
        if idx is not None:
            reminders[idx].update(reminder)
            msg = "updated"
        else:
            reminders.append(reminder)
            msg = "added"
            data["reminders"] = reminders
        return json.dumps({"success": f"reminder {msg}", "reminder": reminder}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_reminder",
                "description": "Create a new reminder or update an existing one.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder": {
                            "type": "object",
                            "description": "Full or partial reminder object.",
                            "additionalProperties": True
                        }
                    },
                    "required": ["reminder"],
                    "additionalProperties": False
                }
            }
        }