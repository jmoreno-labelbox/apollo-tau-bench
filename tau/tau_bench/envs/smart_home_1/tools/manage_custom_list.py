# Copyright by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ManageCustomList(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], action: str, list_id: str,  tags: List[str], name: str = None) -> str:
        lists_doc: List[Dict[str, Any]] = list(data.get("custom_lists", {}).values())
        if action == "list_all_names_ids":
            return json.dumps({"lists": [{"name": l["name"], "list_id": l["list_id"]} for l in lists_doc]}, indent=2)
        if action == "get":
            lst = next((l for l in lists_doc if l["list_id"] == list_id), None)
            return json.dumps({"list": lst} if lst else {"error": "List not found"}, indent=2)
        if action == "delete":
            new_doc = [l for l in lists_doc if l["list_id"] != list_id]
            if len(new_doc) == len(lists_doc):
                return json.dumps({"error": "List not found"}, indent=2)
            data["custom_lists"] = new_doc
            return json.dumps({"success": True}, indent=2)
        if action == "create":
            if not all([name, list_id]):
                return json.dumps({"error": "name and list_id required"}, indent=2)
            if any(l["list_id"] == list_id for l in lists_doc):
                return json.dumps({"error": "Duplicate list_id"}, indent=2)
            lists_doc.append({
                "list_id": list_id,
                "name": name,
                "created_at": _now_iso(),
                "updated_at": _now_iso(),
                "tags": tags,
                "items": [],
            })
            data["custom_lists"] = lists_doc
            return json.dumps({"success": True}, indent=2)
        return json.dumps({"error": "Unknown or missing action"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "manage_custom_list",
                "description": "Create, fetch, delete, or list custom lists.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": ["list_all_names_ids", "get (requires list_id)", "create (requires list_id, name, tags)", "delete (requires list_id)"]},
                        "list_id": {"type": "string", "description": "List identifier."},
                        "name": {"type": "string", "description": "List name."},
                        "tags": {"type": "array", "items": {"type": "string", "description": "List tags."}},
                    },
                    "required": ["action"],
                    "additionalProperties": False,
                },
            },
        }
