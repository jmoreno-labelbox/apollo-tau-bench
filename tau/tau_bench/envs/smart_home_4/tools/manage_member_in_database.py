from tau_bench.envs.tool import Tool
import json
from typing import Any

class ManageMemberInDatabase(Tool):
    """Consolidated CRUD for members: retrieve, add, modify, and delete."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        action: str = "get",
        member_id: str = "",
        member: dict[str, Any] | None = None,
        updates: dict[str, Any] | None = None,
        filters: dict[str, Any] | None = None
    ) -> str:
        members = data.get("members", [])
        if action == "get":
            if member_id:
                result = [m for m in members if m.get("id") == member_id]
            elif filters:
                result = [
                    m for m in members if all(m.get(k) == v for k, v in filters.items())
                ]
            else:
                result = members
            payload = result
            out = json.dumps(payload, indent=2)
            return out
        elif action == "add":
            if not member:
                payload = {"error": "'member' parameter is required for add"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
            if any(m["id"] == member.get("id") for m in members):
                payload = {"error": "Member with this id already exists"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
            members.append(member)
            payload = {"success": "Member added", "member": member, "members": members}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        elif action == "update":
            if not member_id or not updates:
                payload = {
                        "error": "'member_id' and 'updates' parameters are required for update"
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
            found = False
            for m in members:
                if m["id"] == member_id:
                    for k, v in updates.items():
                        m[k] = v
                    found = True
                    break
            if not found:
                payload = {"error": "Member not found"}
                out = json.dumps(payload, indent=2)
                return out
            payload = {
                    "success": "Member updated",
                    "member_id": member_id,
                    "updates": updates,
                    "members": members,
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        elif action == "delete":
            if not member_id:
                payload = {"error": "'member_id' parameter is required for delete"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
            new_list = [m for m in members if m["id"] != member_id]
            if len(new_list) == len(members):
                payload = {"error": "Member not found"}
                out = json.dumps(payload, indent=2)
                return out
            payload = {
                    "success": "Member deleted",
                    "member_id": member_id,
                    "members": new_list,
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = {"error": f"Unknown action: {action}"}
            out = json.dumps(payload, indent=2)
            return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ManageMemberInDatabase",
                "description": "Get member info, add, update, or delete a member.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "description": "Action to perform: get, add, update, delete",
                        },
                        "member_id": {
                            "type": "string",
                            "description": "Member id to operate on (required for get, update, delete)",
                        },
                        "member": {
                            "type": "object",
                            "description": "The full member object to add (required for add)",
                            "additionalProperties": True,
                        },
                        "updates": {
                            "type": "object",
                            "description": "Key-value pairs of fields to update (required for update)",
                            "additionalProperties": True,
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter members (optional for get)",
                            "additionalProperties": True,
                        },
                    },
                    "required": ["action"],
                    "additionalProperties": False,
                },
            },
        }
