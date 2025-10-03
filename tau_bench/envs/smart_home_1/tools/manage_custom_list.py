from tau_bench.envs.tool import Tool
import json
from typing import Any

class ManageCustomList(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        action: str,
        list_id: str,
        tags: list[str],
        name: str = None
    ) -> str:
        lists_doc: list[dict[str, Any]] = data.get("custom_lists", [])
        if action == "list_all_names_ids":
            payload = {
                "lists": [
                    {"name": l["name"], "list_id": l["list_id"]} for l in lists_doc
                ]
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        if action == "get":
            lst = next((l for l in lists_doc if l["list_id"] == list_id), None)
            payload = {"list": lst} if lst else {"error": "List not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        if action == "delete":
            new_doc = [l for l in lists_doc if l["list_id"] != list_id]
            if len(new_doc) == len(lists_doc):
                payload = {"error": "List not found"}
                out = json.dumps(payload, indent=2)
                return out
            data["custom_lists"] = new_doc
            payload = {"success": True}
            out = json.dumps(payload, indent=2)
            return out
        if action == "create":
            if not all([name, list_id]):
                payload = {"error": "name and list_id required"}
                out = json.dumps(payload, indent=2)
                return out
            if any(l["list_id"] == list_id for l in lists_doc):
                payload = {"error": "Duplicate list_id"}
                out = json.dumps(payload, indent=2)
                return out
            lists_doc.append(
                {
                    "list_id": list_id,
                    "name": name,
                    "created_at": _now_iso(),
                    "updated_at": _now_iso(),
                    "tags": tags,
                    "items": [],
                }
            )
            data["custom_lists"] = lists_doc
            payload = {"success": True}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": "Unknown or missing action"}
        out = json.dumps(payload, indent=2)
        return out
        pass
        lists_doc: list[dict[str, Any]] = data.get("custom_lists", [])
        if action == "list_all_names_ids":
            payload = {
                    "lists": [
                        {"name": l["name"], "list_id": l["list_id"]} for l in lists_doc
                    ]
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        if action == "get":
            lst = next((l for l in lists_doc if l["list_id"] == list_id), None)
            payload = {"list": lst} if lst else {"error": "List not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        if action == "delete":
            new_doc = [l for l in lists_doc if l["list_id"] != list_id]
            if len(new_doc) == len(lists_doc):
                payload = {"error": "List not found"}
                out = json.dumps(payload, indent=2)
                return out
            data["custom_lists"] = new_doc
            payload = {"success": True}
            out = json.dumps(payload, indent=2)
            return out
        if action == "create":
            if not all([name, list_id]):
                payload = {"error": "name and list_id required"}
                out = json.dumps(payload, indent=2)
                return out
            if any(l["list_id"] == list_id for l in lists_doc):
                payload = {"error": "Duplicate list_id"}
                out = json.dumps(payload, indent=2)
                return out
            lists_doc.append(
                {
                    "list_id": list_id,
                    "name": name,
                    "created_at": _now_iso(),
                    "updated_at": _now_iso(),
                    "tags": tags,
                    "items": [],
                }
            )
            data["custom_lists"] = lists_doc
            payload = {"success": True}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": "Unknown or missing action"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ManageCustomList",
                "description": "Create, fetch, delete, or list custom lists.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "enum": [
                                "list_all_names_ids",
                                "get (requires list_id)",
                                "create (requires list_id, name, tags)",
                                "delete (requires list_id)",
                            ],
                        },
                        "list_id": {
                            "type": "string",
                            "description": "List identifier.",
                        },
                        "name": {"type": "string", "description": "List name."},
                        "tags": {
                            "type": "array",
                            "items": {"type": "string", "description": "List tags."},
                        },
                    },
                    "required": ["action"],
                    "additionalProperties": False,
                },
            },
        }
