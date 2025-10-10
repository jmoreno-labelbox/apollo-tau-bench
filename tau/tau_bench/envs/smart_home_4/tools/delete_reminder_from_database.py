# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteReminderFromDatabase(Tool):
    """Remove a reminder by id."""
    @staticmethod
    def invoke(data: Dict[str, Any], reminder_id: str = "") -> str:
        if not reminder_id:
            return json.dumps({"error": "'reminder_id' parameter is required"}, indent=2)
        reminders = data.get('reminders', [])
        new_list = [r for r in reminders if r["reminder_id"] != reminder_id]
        if len(new_list) == len(reminders):
            return json.dumps({"error": "Reminder not found"}, indent=2)
        return json.dumps({"success": "Reminder deleted", "reminder_id": reminder_id, "reminders": new_list}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_reminder_from_database",
                "description": "Remove a reminder by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder_id": {
                            "type": "string",
                            "description": "The id of the reminder to delete."
                        }
                    },
                    "required": ["reminder_id"],
                    "additionalProperties": False
                }
            }
        }
