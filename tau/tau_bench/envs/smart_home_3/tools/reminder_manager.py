# Sierra copyright.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReminderManager(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        reminders = list(data.get('reminders', {}).values())
        action = kwargs.get('action', 'get')
        reminder_id = kwargs.get('reminder_id')
        status = kwargs.get('status')
        priority = kwargs.get('priority')
        reminder_data = kwargs.get('reminder_data', {})

        if action == 'get':
            result = [r for r in reminders if (not reminder_id or r['reminder_id'] == reminder_id) and
                     (not status or r['status'] == status) and
                     (not priority or r['meta'].get('priority') == priority)]
            return json.dumps(result, indent=2)
        elif action == 'create':
            if not reminder_data:
                return json.dumps({"error": "reminder_data required"}, indent=2)
            reminders.append(reminder_data)
            return json.dumps({"success": f"Created reminder {reminder_data.get('reminder_id')}"}, indent=2)
        elif action == 'update_status':
            if not reminder_id or not status:
                return json.dumps({"error": "reminder_id and status required"}, indent=2)
            for reminder in reminders:
                if reminder['reminder_id'] == reminder_id:
                    reminder['status'] = status
                    return json.dumps({"success": f"Updated {reminder_id} status to {status}"}, indent=2)
        elif action == 'snooze':
            if not reminder_id:
                return json.dumps({"error": "reminder_id required"}, indent=2)
            for reminder in reminders:
                if reminder['reminder_id'] == reminder_id:
                    reminder['status'] = 'snoozed'
                    return json.dumps({"success": f"Snoozed reminder {reminder_id}"}, indent=2)
        elif action == 'delete':
            if not reminder_id:
                return json.dumps({"error": "reminder_id required"}, indent=2)
            reminders[:] = [r for r in reminders if r['reminder_id'] != reminder_id]
            return json.dumps({"success": f"Deleted reminder {reminder_id}"}, indent=2)

        return json.dumps({"error": "Invalid action"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "reminder_manager",
                "description": "Manage reminders and notifications",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": ["get", "create", "update_status", "snooze", "delete"]},
                        "reminder_id": {"type": "string", "description": "Reminder ID"},
                        "status": {"type": "string", "description": "Filter by or set status"},
                        "priority": {"type": "string", "description": "Filter by priority"},
                        "reminder_data": {"type": "object", "description": "Full reminder data for creation"}
                    },
                    "required": ["action"],
                    "additionalProperties": False
                }
            }
        }
