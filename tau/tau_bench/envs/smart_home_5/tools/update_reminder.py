# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateReminder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], reminder_id: str, update_fields: Dict[str, Any]) -> str:
        reminders = data.get('reminders', [])
        reminder_found = False
        for reminder in reminders:
            if reminder.get('reminder_id') == reminder_id:
                reminder_found = True
                reminder.update(update_fields)
                break

        if not reminder_found:
            return json.dumps({"error": f"Reminder with ID '{reminder_id}' not found."}, indent=2)

        return json.dumps({"success": f"Reminder '{reminder_id}' updated."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_reminder",
                "description": "Update an existing reminder.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder_id": {
                            "type": "string",
                            "description": "The ID of the reminder to update."
                        },
                        "update_fields": {
                            "type": "object",
                            "description": "Fields to update in the reminder.",
                            "additionalProperties": True
                        }
                    },
                    "required": ["reminder_id", "update_fields"],
                    "additionalProperties": False
                }
            }
        }
