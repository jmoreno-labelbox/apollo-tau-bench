# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetReminderByIdOrFilter(Tool):
    """Retrieve reminder(s) by id or filter."""
    @staticmethod
    def invoke(data: Dict[str, Any], reminder_id: str = "", filters: Optional[Dict[str, Any]] = None) -> str:
        reminders = data.get('reminders', [])
        if reminder_id:
            result = [r for r in reminders if r.get("reminder_id") == reminder_id]
        elif filters:
            result = [r for r in reminders if all(r.get(k) == v for k, v in filters.items())]
        else:
            return json.dumps({"error": "Either 'reminder_id' or 'filters' must be provided"}, indent=2)
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_reminder_by_id_or_filter",
                "description": "Retrieve reminder(s) by id or filter. If 'reminder_id' is provided, returns the reminder with that id. If 'filters' is provided, returns all reminders matching the filter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder_id": {
                            "type": "string",
                            "description": "Reminder id to retrieve (optional if using filters)"
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter reminders (optional if using reminder_id)",
                            "additionalProperties": True
                        }
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }
