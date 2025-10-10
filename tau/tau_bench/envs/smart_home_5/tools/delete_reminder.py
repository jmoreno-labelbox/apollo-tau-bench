# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteReminder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], reminder_id: str) -> str:
        reminders = data.get('reminders', [])
        initial_len = len(reminders)
        reminders[:] = [r for r in reminders if r.get('reminder_id') != reminder_id]

        if len(reminders) == initial_len:
            return json.dumps({"error": f"Reminder with ID '{reminder_id}' not found."}, indent=2)

        return json.dumps({"success": f"Reminder '{reminder_id}' deleted."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_reminder",
                "description": "Delete a reminder.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder_id": {
                            "type": "string",
                            "description": "The ID of the reminder to delete."
                        }
                    },
                    "required": ["reminder_id"],
                    "additionalProperties": False
                }
            }
        }
