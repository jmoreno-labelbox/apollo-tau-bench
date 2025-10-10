# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ManageReminders(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], action: str, reminder_id: Optional[str] = None, reminder: Optional[Dict[str, Any]] = None, updates: Optional[Dict[str, Any]] = None) -> str:
        reminders = list(data.get("reminders", {}).values())
        if action == "list_all_names_ids":
            return json.dumps({"reminders": [{"name": r["name"], "reminder_id": r["reminder_id"]} for r in reminders]}, indent=2)
        if action == "get":
            r = next((r for r in reminders if r["reminder_id"] == reminder_id), None)
            return json.dumps({"reminder": r} if r else {"error": "not found"}, indent=2)
        if action == "delete":
            new_doc = [r for r in reminders if r["reminder_id"] != reminder_id]
            if len(new_doc) == len(reminders):
                return json.dumps({"error": "not found"}, indent=2)
            data["reminders"] = new_doc
            return json.dumps({"success": True}, indent=2)
        if action == "create":
            if not reminder or "reminder_id" not in reminder:
                return json.dumps({"error": "reminder object with reminder_id required"}, indent=2)
            if any(r["reminder_id"] == reminder["reminder_id"] for r in reminders):
                return json.dumps({"error": "Duplicate id"}, indent=2)
            reminders.append(reminder)
            data["reminders"] = reminders
            return json.dumps({"success": True}, indent=2)
        if action == "update":
            modified = False
            for r in reminders:
                if r["reminder_id"] == reminder_id:
                    r.update(updates)
                    modified = True
                    break
            if not modified:
                return json.dumps({"error": "not found"}, indent=2)
            data["reminders"] = reminders
            return json.dumps({"success": True}, indent=2)
        return json.dumps({"error": "Unknown action"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "manage_reminders",
                "description": "Create, list, get, update, or delete reminders.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": ["list_all_names_ids", "get (requires reminder_id)", "create (requires reminder_id, reminder)", "update (requires reminder_id, updates)", "delete (requires reminder_id)"]},
                        "reminder_id": {"type": "string", "description": "Reminder identifier."},
                        "reminder": {"type": "object", "description": "Key/value pairs of reminder."},
                        "updates": {"type": "object", "description": "Key/value pairs of updates."},
                    },
                    "required": ["action"],
                    "additionalProperties": False,
                },
            },
        }
