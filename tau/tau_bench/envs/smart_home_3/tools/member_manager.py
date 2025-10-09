from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class MemberManager(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        action: str = "get",
        member_id: str = None,
        relation: str = None,
        lives_in_house: bool = None,
        member_data: dict[str, Any] = {},
        field_updates: dict[str, Any] = {}
    ) -> str:
        members = data.get("members", [])

        if action == "get":
            result = [
                m
                for m in members
                if (not member_id or m["id"] == member_id)
                and (not relation or relation.lower() in m["relation"].lower())
                and (
                    lives_in_house is None
                    or m["residence"]["lives_in_house"] == lives_in_house
                )
            ]
            payload = result
            out = json.dumps(payload, indent=2)
            return out
        elif action == "update":
            if not member_id or not field_updates:
                payload = {"error": "member_id and field_updates required"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
            for member in members:
                if member["id"] == member_id:
                    for field, value in field_updates.items():
                        if "." in field:  # a nested field such as 'contact.phone'
                            parts = field.split(".")
                            obj = member
                            for part in parts[:-1]:
                                obj = obj[part]
                            obj[parts[-1]] = value
                        else:
                            member[field] = value
                    payload = {"success": f"Updated member {member_id}"}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
        elif action == "create":
            if not member_data:
                payload = {"error": "member_data required"}
                out = json.dumps(payload, indent=2)
                return out
            members.append(member_data)
            payload = {"success": f"Created member {member_data.get('id')}"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        elif action == "delete":
            if not member_id:
                payload = {"error": "member_id required"}
                out = json.dumps(payload, indent=2)
                return out
            members[:] = [m for m in members if m["id"] != member_id]
            payload = {"success": f"Deleted member {member_id}"}
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
                "name": "MemberManager",
                "description": "Manage household members and visitors",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "enum": ["get", "update", "create", "delete"],
                        },
                        "member_id": {
                            "type": "string",
                            "description": "Member ID (first_name.last_name)",
                        },
                        "relation": {
                            "type": "string",
                            "description": "Filter by relation",
                        },
                        "lives_in_house": {
                            "type": "boolean",
                            "description": "Filter by residence status",
                        },
                        "member_data": {
                            "type": "object",
                            "description": "Full member data for creation",
                        },
                        "field_updates": {
                            "type": "object",
                            "description": "Fields to update (supports nested with dots)",
                        },
                    },
                    "required": ["action"],
                    "additionalProperties": False,
                },
            },
        }
