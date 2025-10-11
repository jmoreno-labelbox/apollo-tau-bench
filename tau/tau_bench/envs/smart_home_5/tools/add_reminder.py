# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddReminder(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], new_reminder: Dict[str, Any]) -> str:
        reminders = data.get('reminders', [])
        if 'reminder_id' not in new_reminder:
            return json.dumps({"error": "New reminder must have a 'reminder_id'."}, indent=2)

        reminders.append(new_reminder)
        return json.dumps({"success": "Reminder added."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_reminder",
                "description": "Add a new reminder.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "new_reminder": {
                            "type": "object",
                            "description": "A dictionary representing the new reminder.",
                            "additionalProperties": True
                        }
                    },
                    "required": ["new_reminder"],
                    "additionalProperties": False
                }
            }
        }
