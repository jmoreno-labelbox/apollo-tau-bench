from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateReminderInDatabase(Tool):
    """Modify any attribute of a reminder."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        reminder_id: str = "",
        updates: dict[str, Any] | None = None,
    ) -> str:
        if not reminder_id or not updates:
            payload = {"error": "'reminder_id' and 'updates' parameters are required"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        reminders = data.get("reminders", [])
        found = False
        for r in reminders:
            if r["reminder_id"] == reminder_id:
                for k, v in updates.items():
                    r[k] = v
                found = True
                break
        if not found:
            payload = {"error": "Reminder not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {
                "success": "Reminder updated",
                "reminder_id": reminder_id,
                "updates": updates,
                "reminders": reminders,
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
                "name": "updateReminderInDatabase",
                "description": "Update any field of a reminder by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder_id": {
                            "type": "string",
                            "description": "The id of the reminder to update.",
                        },
                        "updates": {
                            "type": "object",
                            "description": "Key-value pairs of fields to update.",
                            "additionalProperties": True,
                        },
                    },
                    "required": ["reminder_id", "updates"],
                    "additionalProperties": False,
                },
            },
        }
