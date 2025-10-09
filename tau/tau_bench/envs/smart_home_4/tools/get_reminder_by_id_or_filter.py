from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetReminderByIdOrFilter(Tool):
    """Fetch reminder(s) using id or filters."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        reminder_id: str = "",
        filters: dict[str, Any] | None = None
    ) -> str:
        reminders = data.get("reminders", [])
        if reminder_id:
            result = [r for r in reminders if r.get("reminder_id") == reminder_id]
        elif filters:
            result = [
                r for r in reminders if all(r.get(k) == v for k, v in filters.items())
            ]
        else:
            payload = {"error": "Either 'reminder_id' or 'filters' must be provided"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getReminderByIdOrFilter",
                "description": "Retrieve reminder(s) by id or filter. If 'reminder_id' is provided, returns the reminder with that id. If 'filters' is provided, returns all reminders matching the filter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder_id": {
                            "type": "string",
                            "description": "Reminder id to retrieve (optional if using filters)",
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter reminders (optional if using reminder_id)",
                            "additionalProperties": True,
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
