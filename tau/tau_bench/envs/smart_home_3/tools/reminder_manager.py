from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ReminderManager(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        action: str = "get",
        reminder_id: str = None,
        status: str = None,
        priority: str = None,
        reminder_data: dict = None
    ) -> str:
        reminders = data.get("reminders", {}).values()

        if action == "get":
            result = [
                r
                for r in reminders.values() if (not reminder_id or r["reminder_id"] == reminder_id)
                and (not status or r["status"] == status)
                and (not priority or r["meta"].get("priority") == priority)
            ]
            payload = result
            out = json.dumps(payload, indent=2)
            return out
        elif action == "create":
            if not reminder_data:
                payload = {"error": "reminder_data required"}
                out = json.dumps(payload, indent=2)
                return out
            data["reminders"][reminder_id] = reminder_data
            payload = {"success": f"Created reminder {reminder_data.get('reminder_id')}"}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        elif action == "update_status":
            if not reminder_id or not status:
                payload = {"error": "reminder_id and status required"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
            for reminder in reminders:
                if reminder["reminder_id"] == reminder_id:
                    reminder["status"] = status
                    payload = {"success": f"Updated {reminder_id} status to {status}"}
                    out = json.dumps(
                        payload, indent=2,
                    )
                    return out
        elif action == "snooze":
            if not reminder_id:
                payload = {"error": "reminder_id required"}
                out = json.dumps(payload, indent=2)
                return out
            for reminder in reminders:
                if reminder["reminder_id"] == reminder_id:
                    reminder["status"] = "snoozed"
                    payload = {"success": f"Snoozed reminder {reminder_id}"}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
        elif action == "delete":
            if not reminder_id:
                payload = {"error": "reminder_id required"}
                out = json.dumps(payload, indent=2)
                return out
            reminders[:] = [r for r in reminders.values() if r["reminder_id"] != reminder_id]
            payload = {"success": f"Deleted reminder {reminder_id}"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": "Invalid action"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReminderManager",
                "description": "Manage reminders and notifications",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "enum": [
                                "get",
                                "create",
                                "update_status",
                                "snooze",
                                "delete",
                            ],
                        },
                        "reminder_id": {"type": "string", "description": "Reminder ID"},
                        "status": {
                            "type": "string",
                            "description": "Filter by or set status",
                        },
                        "priority": {
                            "type": "string",
                            "description": "Filter by priority",
                        },
                        "reminder_data": {
                            "type": "object",
                            "description": "Full reminder data for creation",
                        },
                    },
                    "required": ["action"],
                    "additionalProperties": False,
                },
            },
        }
