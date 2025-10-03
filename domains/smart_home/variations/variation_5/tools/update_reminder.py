from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateReminder(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], reminder_id: str, update_fields: dict[str, Any]
    ) -> str:
        reminders = data.get("reminders", [])
        reminder_found = False
        for reminder in reminders:
            if reminder.get("reminder_id") == reminder_id:
                reminder_found = True
                reminder.update(update_fields)
                break

        if not reminder_found:
            payload = {"error": f"Reminder with ID '{reminder_id}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"success": f"Reminder '{reminder_id}' updated."}
        out = json.dumps(payload, indent=2)
        return out
    

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateReminder",
                "description": "Update an existing reminder.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder_id": {
                            "type": "string",
                            "description": "The ID of the reminder to update.",
                        },
                        "update_fields": {
                            "type": "object",
                            "description": "Fields to update in the reminder.",
                            "additionalProperties": True,
                        },
                    },
                    "required": ["reminder_id", "update_fields"],
                    "additionalProperties": False,
                },
            },
        }
