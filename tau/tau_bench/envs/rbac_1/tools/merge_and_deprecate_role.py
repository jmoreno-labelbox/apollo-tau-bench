# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class MergeAndDeprecateRole(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        source_role_id = kwargs.get("source_role_id")
        target_role_id = kwargs.get("target_role_id")
        actor_id = kwargs.get("actor_id")

        source_perms = {rp['permission_id'] for rp in data.get('role_permissions', []) if rp['role_id'] == source_role_id}
        target_perms = {rp['permission_id'] for rp in data.get('role_permissions', []) if rp['role_id'] == target_role_id}

        perms_to_add = source_perms - target_perms
        for perm_id in perms_to_add:
            data['role_permissions'].append({"role_id": target_role_id, "permission_id": perm_id})

        users_to_migrate = [ur['user_id'] for ur in data.get('user_roles', []) if ur['role_id'] == source_role_id]

        migrated_users = []
        for user_id in users_to_migrate:
            has_target_role = any(ur['user_id'] == user_id and ur['role_id'] == target_role_id for ur in data.get('user_roles', []))
            if not has_target_role:
                new_id_num = max((int(ur['user_role_id'][3:]) for ur in data['user_roles']), default=0) + 1
                new_user_role_id = f"UR-{new_id_num:03d}"
                data['user_roles'].append({
                        "user_role_id": new_user_role_id,
                        "user_id": user_id,
                        "role_id": target_role_id,
                        "assigned_by": actor_id,
                        "assigned_on": NOW.strftime(DT_STR_FORMAT),
                        "expires_on": None
                })
                migrated_users.append(user_id)

        data['user_roles'] = [ur for ur in data.get('user_roles', []) if ur.get('role_id') != source_role_id]

        for role in list(data.get('roles', {}).values()):
            if role.get('role_id') == source_role_id:
                role['role_name'] = f"DEPRECATED-{role['role_name']}"
                role['description'] = f"[DEPRECATED] Merged into {target_role_id}."
                break

        return json.dumps({
                "source_role_id": source_role_id,
                "target_role_id": target_role_id,
                "permissions_migrated": len(perms_to_add),
                "users_reassigned": len(migrated_users)
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "merge_and_deprecate_role",
                        "description": "Merges permissions and users from a source role into a target role, then deprecates the source role.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "source_role_id": {"type": "string"},
                                        "target_role_id": {"type": "string"},
                                        "actor_id": {"type": "string"}
                                },
                                "required": ["source_role_id", "target_role_id", "actor_id"]
                        }
                }
        }
