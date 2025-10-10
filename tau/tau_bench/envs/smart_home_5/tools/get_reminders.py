# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetReminders(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], reminder_id: Optional[str] = None, status: Optional[str] = None) -> str:
        reminders = data.get('reminders', [])
        result = reminders
        if reminder_id:
            result = [r for r in result if r.get('reminder_id') == reminder_id]
        if status:
            result = [r for r in result if r.get('status') == status]
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_reminders",
                "description": "Get reminders, with optional filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reminder_id": {
                            "type": "string",
                            "description": "The ID of a specific reminder to retrieve."
                        },
                        "status": {
                            "type": "string",
                            "enum": ["scheduled", "active", "inactive"],
                            "description": "Filter reminders by status."
                        }
                    },
                    "additionalProperties": False
                }
            }
        }
