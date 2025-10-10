# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class MemberManager(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        members = list(data.get('members', {}).values())
        action = kwargs.get('action', 'get')
        member_id = kwargs.get('member_id')
        relation = kwargs.get('relation')
        lives_in_house = kwargs.get('lives_in_house')
        member_data = kwargs.get('member_data', {})
        field_updates = kwargs.get('field_updates', {})

        if action == 'get':
            result = [m for m in members if (not member_id or m['id'] == member_id) and
                     (not relation or relation.lower() in m['relation'].lower()) and
                     (lives_in_house is None or m['residence']['lives_in_house'] == lives_in_house)]
            return json.dumps(result, indent=2)
        elif action == 'update':
            if not member_id or not field_updates:
                return json.dumps({"error": "member_id and field_updates required"}, indent=2)
            for member in members:
                if member['id'] == member_id:
                    for field, value in field_updates.items():
                        if '.' in field:  # hierarchical field such as 'contact.phone'
                            parts = field.split('.')
                            obj = member
                            for part in parts[:-1]:
                                obj = obj[part]
                            obj[parts[-1]] = value
                        else:
                            member[field] = value
                    return json.dumps({"success": f"Updated member {member_id}"}, indent=2)
        elif action == 'create':
            if not member_data:
                return json.dumps({"error": "member_data required"}, indent=2)
            members.append(member_data)
            return json.dumps({"success": f"Created member {member_data.get('id')}"}, indent=2)
        elif action == 'delete':
            if not member_id:
                return json.dumps({"error": "member_id required"}, indent=2)
            members[:] = [m for m in members if m['id'] != member_id]
            return json.dumps({"success": f"Deleted member {member_id}"}, indent=2)

        return json.dumps({"error": "Invalid action"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "member_manager",
                "description": "Manage household members and visitors",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": ["get", "update", "create", "delete"]},
                        "member_id": {"type": "string", "description": "Member ID (first_name.last_name)"},
                        "relation": {"type": "string", "description": "Filter by relation"},
                        "lives_in_house": {"type": "boolean", "description": "Filter by residence status"},
                        "member_data": {"type": "object", "description": "Full member data for creation"},
                        "field_updates": {"type": "object", "description": "Fields to update (supports nested with dots)"}
                    },
                    "required": ["action"],
                    "additionalProperties": False
                }
            }
        }
