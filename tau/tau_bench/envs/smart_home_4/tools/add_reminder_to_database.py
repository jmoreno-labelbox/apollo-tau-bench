# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddReminderToDatabase(Tool):
    """Add a new reminder."""
    @staticmethod
    def invoke(data: Dict[str, Any], reminder: Optional[Dict[str, Any]] = None, threshold: Dict[str, Any] = None) -> str:
        if not reminder:
            return json.dumps({"error": "'reminder' parameter is required"}, indent=2)
        reminders = data.get('reminders', [])
        if any(r["reminder_id"] == reminder.get("reminder_id") for r in reminders):
            return json.dumps({"error": "Reminder with this id already exists"}, indent=2)
        reminders.append(reminder)
        return json.dumps({"success": "Reminder added", "reminder": reminder, "reminders": reminders}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_reminder_to_database",
                "description": "Add a new reminder. All fields must be provided in the 'reminder' object.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder": {
                            "type": "object",
                            "description": "The full reminder object to add (must include reminder_id, name, target, trigger, actions, meta, status, created_at, etc.)",
                            "additionalProperties": True
                        }
                    },
                    "required": ["reminder"],
                    "additionalProperties": False
                }
            }
        }
