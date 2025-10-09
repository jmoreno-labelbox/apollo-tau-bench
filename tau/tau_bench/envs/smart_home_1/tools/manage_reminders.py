from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ManageReminders(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        action: str,
        reminder_id: str | None = None,
        reminder: dict[str, Any] | None = None,
        updates: dict[str, Any] | None = None
    ) -> str:
        reminders = data.get("reminders", {}).values()
        if action == "list_all_names_ids":
            payload = {
                "reminders": [
                    {"name": r["name"], "reminder_id": r["reminder_id"]}
                    for r in reminders.values()
                ]
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        if action == "get":
            r = next((r for r in reminders.values() if r["reminder_id"] == reminder_id), None)
            payload = {"reminder": r} if r else {"error": "not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        if action == "delete":
            new_doc = [r for r in reminders.values() if r["reminder_id"] != reminder_id]
            if len(new_doc) == len(reminders):
                payload = {"error": "not found"}
                out = json.dumps(payload, indent=2)
                return out
            data["reminders"] = new_doc
            payload = {"success": True}
            out = json.dumps(payload, indent=2)
            return out
        if action == "create":
            if not reminder or "reminder_id" not in reminder:
                payload = {"error": "reminder object with reminder_id required"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
            if any(r["reminder_id"] == reminder["reminder_id"] for r in reminders.values()):
                payload = {"error": "Duplicate id"}
                out = json.dumps(payload, indent=2)
                return out
            data["reminders"][reminder_id] = reminder
            data["reminders"] = reminders
            payload = {"success": True}
            out = json.dumps(payload, indent=2)
            return out
        if action == "update":
            modified = False
            for r in reminders.values():
                if r["reminder_id"] == reminder_id:
                    r.update(updates)
                    modified = True
                    break
            if not modified:
                payload = {"error": "not found"}
                out = json.dumps(payload, indent=2)
                return out
            data["reminders"] = reminders
            payload = {"success": True}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": "Unknown action"}
        out = json.dumps(payload, indent=2)
        return out
        pass
        reminders = data.get("reminders", {}).values()
        if action == "list_all_names_ids":
            payload = {
                    "reminders": [
                        {"name": r["name"], "reminder_id": r["reminder_id"]}
                        for r in reminders.values()
                    ]
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        if action == "get":
            r = next((r for r in reminders.values() if r["reminder_id"] == reminder_id), None)
            payload = {"reminder": r} if r else {"error": "not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        if action == "delete":
            new_doc = [r for r in reminders.values() if r["reminder_id"] != reminder_id]
            if len(new_doc) == len(reminders):
                payload = {"error": "not found"}
                out = json.dumps(payload, indent=2)
                return out
            data["reminders"] = new_doc
            payload = {"success": True}
            out = json.dumps(payload, indent=2)
            return out
        if action == "create":
            if not reminder or "reminder_id" not in reminder:
                payload = {"error": "reminder object with reminder_id required"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
            if any(r["reminder_id"] == reminder["reminder_id"] for r in reminders.values()):
                payload = {"error": "Duplicate id"}
                out = json.dumps(payload, indent=2)
                return out
            data["reminders"][reminder_id] = reminder
            data["reminders"] = reminders
            payload = {"success": True}
            out = json.dumps(payload, indent=2)
            return out
        if action == "update":
            modified = False
            for r in reminders.values():
                if r["reminder_id"] == reminder_id:
                    r.update(updates)
                    modified = True
                    break
            if not modified:
                payload = {"error": "not found"}
                out = json.dumps(payload, indent=2)
                return out
            data["reminders"] = reminders
            payload = {"success": True}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": "Unknown action"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ManageReminders",
                "description": "Create, list, get, update, or delete reminders.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "enum": [
                                "list_all_names_ids",
                                "get (requires reminder_id)",
                                "create (requires reminder_id, reminder)",
                                "update (requires reminder_id, updates)",
                                "delete (requires reminder_id)",
                            ],
                        },
                        "reminder_id": {
                            "type": "string",
                            "description": "Reminder identifier.",
                        },
                        "reminder": {
                            "type": "object",
                            "description": "Key/value pairs of reminder.",
                        },
                        "updates": {
                            "type": "object",
                            "description": "Key/value pairs of updates.",
                        },
                    },
                    "required": ["action"],
                    "additionalProperties": False,
                },
            },
        }
