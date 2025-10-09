from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AddReminderToDatabase(Tool):
    """Introduce a new reminder."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        reminder: dict[str, Any] | None = None,
        threshold: dict[str, Any] = None,
    ) -> str:
        if not reminder:
            payload = {"error": "'reminder' parameter is required"}
            out = json.dumps(payload, indent=2)
            return out
        reminders = data.get("reminders", [])
        if any(r["reminder_id"] == reminder.get("reminder_id") for r in reminders):
            payload = {"error": "Reminder with this id already exists"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        reminders.append(reminder)
        payload = {"success": "Reminder added", "reminder": reminder, "reminders": reminders}
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddReminderToDatabase",
                "description": "Add a new reminder. All fields must be provided in the 'reminder' object.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder": {
                            "type": "object",
                            "description": "The full reminder object to add (must include reminder_id, name, target, trigger, actions, meta, status, created_at, etc.)",
                            "additionalProperties": True,
                        }
                    },
                    "required": ["reminder"],
                    "additionalProperties": False,
                },
            },
        }
