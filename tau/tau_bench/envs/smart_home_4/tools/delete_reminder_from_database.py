from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class DeleteReminderFromDatabase(Tool):
    """Delete a reminder using its id."""

    @staticmethod
    def invoke(data: dict[str, Any], reminder_id: str = "") -> str:
        if not reminder_id:
            payload = {"error": "'reminder_id' parameter is required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        reminders = data.get("reminders", {}).values()
        new_list = [r for r in reminders.values() if r["reminder_id"] != reminder_id]
        if len(new_list) == len(reminders):
            payload = {"error": "Reminder not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {
                "success": "Reminder deleted",
                "reminder_id": reminder_id,
                "reminders": new_list,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteReminderFromDatabase",
                "description": "Remove a reminder by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder_id": {
                            "type": "string",
                            "description": "The id of the reminder to delete.",
                        }
                    },
                    "required": ["reminder_id"],
                    "additionalProperties": False,
                },
            },
        }
