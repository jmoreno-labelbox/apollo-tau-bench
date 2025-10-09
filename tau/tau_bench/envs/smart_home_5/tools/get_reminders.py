from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetReminders(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], reminder_id: str | None = None, status: str | None = None
    ) -> str:
        reminders = data.get("reminders", [])
        result = reminders
        if reminder_id:
            result = [r for r in result if r.get("reminder_id") == reminder_id]
        if status:
            result = [r for r in result if r.get("status") == status]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReminders",
                "description": "Get reminders, with optional filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder_id": {
                            "type": "string",
                            "description": "The ID of a specific reminder to retrieve.",
                        },
                        "status": {
                            "type": "string",
                            "enum": ["scheduled", "active", "inactive"],
                            "description": "Filter reminders by status.",
                        },
                    },
                    "additionalProperties": False,
                },
            },
        }
