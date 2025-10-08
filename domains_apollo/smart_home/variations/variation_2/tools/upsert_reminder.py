from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpsertReminder(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], reminder: dict[str, Any]) -> str:
        if not reminder:
            payload = {"error": "reminder object required"}
            out = json.dumps(payload, indent=2)
            return out
        reminders = _load("reminders", data)
        idx, _ = _find(reminders, reminder["reminder_id"])
        if idx is not None:
            reminders[idx].update(reminder)
            msg = "updated"
        else:
            reminders.append(reminder)
            msg = "added"
            data["reminders"] = reminders
        payload = {"success": f"reminder {msg}", "reminder": reminder}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpsertReminder",
                "description": "Create a new reminder or update an existing one.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder": {
                            "type": "object",
                            "description": "Full or partial reminder object.",
                            "additionalProperties": True,
                        }
                    },
                    "required": ["reminder"],
                    "additionalProperties": False,
                },
            },
        }
