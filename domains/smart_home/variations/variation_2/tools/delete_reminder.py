from tau_bench.envs.tool import Tool
import json
from typing import Any

class DeleteReminder(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], reminder_id: str) -> str:
        reminders = _load("reminders", data)
        idx, rem = _find(reminders, reminder_id)
        if idx is None:
            payload = {"error": "reminder not found"}
            out = json.dumps(payload, indent=2)
            return out
        reminders.pop(idx)
        data["reminders"] = reminders
        payload = {"success": "reminder deleted", "reminder": rem}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeleteReminder",
                "description": "Delete a reminder by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder_id": {"type": "string", "description": "Reminder id"}
                    },
                    "required": ["reminder_id"],
                    "additionalProperties": False,
                },
            },
        }
