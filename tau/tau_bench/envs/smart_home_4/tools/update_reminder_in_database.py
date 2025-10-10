# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateReminderInDatabase(Tool):
    """Update any field of a reminder."""
    @staticmethod
    def invoke(data: Dict[str, Any], reminder_id: str = "", updates: Optional[Dict[str, Any]] = None) -> str:
        if not reminder_id or not updates:
            return json.dumps({"error": "'reminder_id' and 'updates' parameters are required"}, indent=2)
        reminders = data.get('reminders', [])
        found = False
        for r in reminders:
            if r["reminder_id"] == reminder_id:
                for k, v in updates.items():
                    r[k] = v
                found = True
                break
        if not found:
            return json.dumps({"error": "Reminder not found"}, indent=2)
        return json.dumps({"success": "Reminder updated", "reminder_id": reminder_id, "updates": updates, "reminders": reminders}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_reminder_in_database",
                "description": "Update any field of a reminder by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder_id": {
                            "type": "string",
                            "description": "The id of the reminder to update."
                        },
                        "updates": {
                            "type": "object",
                            "description": "Key-value pairs of fields to update.",
                            "additionalProperties": True
                        }
                    },
                    "required": ["reminder_id", "updates"],
                    "additionalProperties": False
                }
            }
        }
