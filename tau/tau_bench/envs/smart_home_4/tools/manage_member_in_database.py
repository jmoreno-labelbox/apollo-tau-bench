# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ManageMemberInDatabase(Tool):
    """Unified CRUD for members: get, add, update, delete."""
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        action: str = "get",
        member_id: str = "",
        member: Optional[Dict[str, Any]] = None,
        updates: Optional[Dict[str, Any]] = None,
        filters: Optional[Dict[str, Any]] = None
    ) -> str:
        members = data.get('members', [])
        if action == "get":
            if member_id:
                result = [m for m in members if m.get("id") == member_id]
            elif filters:
                result = [m for m in members if all(m.get(k) == v for k, v in filters.items())]
            else:
                result = members
            return json.dumps(result, indent=2)
        elif action == "add":
            if not member:
                return json.dumps({"error": "'member' parameter is required for add"}, indent=2)
            if any(m["id"] == member.get("id") for m in members):
                return json.dumps({"error": "Member with this id already exists"}, indent=2)
            members.append(member)
            return json.dumps({"success": "Member added", "member": member, "members": members}, indent=2)
        elif action == "update":
            if not member_id or not updates:
                return json.dumps({"error": "'member_id' and 'updates' parameters are required for update"}, indent=2)
            found = False
            for m in members:
                if m["id"] == member_id:
                    for k, v in updates.items():
                        m[k] = v
                    found = True
                    break
            if not found:
                return json.dumps({"error": "Member not found"}, indent=2)
            return json.dumps({"success": "Member updated", "member_id": member_id, "updates": updates, "members": members}, indent=2)
        elif action == "delete":
            if not member_id:
                return json.dumps({"error": "'member_id' parameter is required for delete"}, indent=2)
            new_list = [m for m in members if m["id"] != member_id]
            if len(new_list) == len(members):
                return json.dumps({"error": "Member not found"}, indent=2)
            return json.dumps({"success": "Member deleted", "member_id": member_id, "members": new_list}, indent=2)
        else:
            return json.dumps({"error": f"Unknown action: {action}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "manage_member_in_database",
                "description": "Get member info, add, update, or delete a member.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "description": "Action to perform: get, add, update, delete"
                        },
                        "member_id": {
                            "type": "string",
                            "description": "Member id to operate on (required for get, update, delete)"
                        },
                        "member": {
                            "type": "object",
                            "description": "The full member object to add (required for add)",
                            "additionalProperties": True
                        },
                        "updates": {
                            "type": "object",
                            "description": "Key-value pairs of fields to update (required for update)",
                            "additionalProperties": True
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter members (optional for get)",
                            "additionalProperties": True
                        }
                    },
                    "required": ["action"],
                    "additionalProperties": False
                }
            }
        }
