from tau_bench.envs.tool import Tool
import json
from typing import Any

class DeleteReminder(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], reminder_id: str) -> str:
        reminders = data.get("reminders", [])
        initial_len = len(reminders)
        reminders[:] = [r for r in reminders if r.get("reminder_id") != reminder_id]

        if len(reminders) == initial_len:
            payload = {"error": f"Reminder with ID '{reminder_id}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"success": f"Reminder '{reminder_id}' deleted."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeleteReminder",
                "description": "Delete a reminder.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder_id": {
                            "type": "string",
                            "description": "The ID of the reminder to delete.",
                        }
                    },
                    "required": ["reminder_id"],
                    "additionalProperties": False,
                },
            },
        }
