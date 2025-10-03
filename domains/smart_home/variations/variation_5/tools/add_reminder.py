from tau_bench.envs.tool import Tool
import json
from typing import Any

class AddReminder(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], new_reminder: dict[str, Any]) -> str:
        reminders = data.get("reminders", [])
        if "reminder_id" not in new_reminder:
            payload = {"error": "New reminder must have a 'reminder_id'."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        reminders.append(new_reminder)
        payload = {"success": "Reminder added."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddReminder",
                "description": "Add a new reminder.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "new_reminder": {
                            "type": "object",
                            "description": "A dictionary representing the new reminder.",
                            "additionalProperties": True,
                        }
                    },
                    "required": ["new_reminder"],
                    "additionalProperties": False,
                },
            },
        }
