import json
from datetime import datetime, timezone
from typing import Any

from tau_bench.envs.tool import Tool

NOW: datetime = datetime(2025, 8, 8, 9, 56, 15, tzinfo=timezone.utc)

DT_STR_FORMAT = "%Y-%m-%dT%H:%M:%SZ"




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db


class CreateUser(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], username: str = None, email: str = None, department: str = None, status: str = None,
    actor_id: Any = None,
    ) -> str:
        pass
        users = data.get("users", [])

        # Effectively determine the subsequent numeric identifier based on current user_ids formatted as 'U-###'
        def _extract_num(user_id: Any) -> int:
            pass
            if not isinstance(user_id, str):
                return 0
            if not user_id.startswith("U-"):
                return 0
            num_part = user_id[2:]
            return int(num_part) if num_part.isdigit() else 0

        new_id_num = max((_extract_num(u.get("user_id")) for u in users), default=0) + 1
        new_user_id = f"U-{new_id_num:03d}"
        new_user = {
            "user_id": new_user_id,
            "username": username,
            "email": email,
            "department": department,
            "status": status,
            "mfa_enabled": False,
        }
        users.append(new_user)
        data["users"] = users
        payload = new_user
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateUser",
                "description": "Creates a new user in the system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {
                            "type": "string",
                            "description": "The username for the new user.",
                        },
                        "email": {
                            "type": "string",
                            "description": "The email address for the new user.",
                        },
                        "department": {
                            "type": "string",
                            "description": "The department the user belongs to.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The initial status of the user account (e.g., ACTIVE).",
                        },
                    },
                    "required": ["username", "email", "department", "status"],
                },
            },
        }


class GetUserByUsername(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], username: str = None, actor_id: Any = None) -> str:
        for user in data.get("users", []):
            if user.get("username") == username:
                payload = user
                out = json.dumps(payload)
                return out
        payload = {"error": "User not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserByUsername",
                "description": "Retrieves user details based on their username.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {
                            "type": "string",
                            "description": "The username to search for.",
                        }
                    },
                    "required": ["username"],
                },
            },
        }


class GetUserById(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        for user in data.get("users", []):
            if user.get("user_id") == user_id:
                payload = user
                out = json.dumps(payload)
                return out
        payload = {"error": "User not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserById",
                "description": "Retrieves user details based on user ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user ID to search for.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }


class GetUserByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], first_name: str = "", last_name: str = "") -> str:
        first_name = first_name.lower()
        last_name = last_name.lower()
        username_to_find = f"{first_name[0]}{last_name}" if first_name else last_name
        for user in data.get("users", []):
            if user.get("username") == username_to_find:
                payload = user
                out = json.dumps(payload)
                return out
        payload = {"error": "User not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserByName",
                "description": "Retrieves user details based on their first and last name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {
                            "type": "string",
                            "description": "The first name of the user.",
                        },
                        "last_name": {
                            "type": "string",
                            "description": "The last name of the user.",
                        },
                    },
                    "required": ["first_name", "last_name"],
                },
            },
        }


class UpdateUserStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, status: str = None,
    updated_by: Any = None,
    ) -> str:
        for user in data.get("users", []):
            if user.get("user_id") == user_id:
                user["status"] = status
                payload = {"user_id": user_id, "status": status}
                out = json.dumps(payload)
                return out
        payload = {"error": "User not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateUserStatus",
                "description": "Updates the status of a user's account (e.g., ACTIVE, DISABLED).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user to update.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The new status for the user account.",
                        },
                    },
                    "required": ["user_id", "status"],
                },
            },
        }


class GetActiveUsersByDepartment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], department: str = None, note: Any = None) -> str:
        active_users = [
            user["user_id"]
            for user in data.get("users", [])
            if user.get("department") == department and user.get("status") == "ACTIVE"
        ]
        payload = {"users": active_users}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetActiveUsersByDepartment",
                "description": "Retrieves a list of active users for a specific department.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department": {
                            "type": "string",
                            "description": "The department to filter by.",
                        }
                    },
                    "required": ["department"],
                },
            },
        }


class GetRoleByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], role_name: str = None) -> str:
        for role in data.get("roles", []):
            if role.get("role_name") == role_name:
                payload = role
                out = json.dumps(payload)
                return out
        payload = {"error": "Role not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRoleByName",
                "description": "Retrieves role details based on the role name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_name": {
                            "type": "string",
                            "description": "The name of the role to search for.",
                        }
                    },
                    "required": ["role_name"],
                },
            },
        }


class GrantRole(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        user_id: str = None, 
        role_id: str = None, 
        assigned_by: str = None, 
        expires_on: str = None
    ) -> str:
        user_roles = data.get("user_roles", [])

        new_id_num = (
            max([int(ur["user_role_id"][3:]) for ur in user_roles], default=0) + 1
        )
        new_user_role_id = f"UR-{new_id_num:03d}"
        new_assignment = {
            "user_role_id": new_user_role_id,
            "user_id": user_id,
            "role_id": role_id,
            "assigned_by": assigned_by,
            "expires_on": expires_on,
        }
        user_roles.append(new_assignment)
        data["user_roles"] = user_roles
        payload = new_assignment
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GrantRole",
                "description": "Assigns a role to a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "role_id": {"type": "string"},
                        "assigned_by": {"type": "string"},
                        "expires_on": {"type": "string", "format": "date-time"},
                    },
                    "required": ["user_id", "role_id", "assigned_by"],
                },
            },
        }


class GetRolesByPermission(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], permission_id: str = None) -> str:
        if not permission_id:
            payload = {"error": "permission_id must be provided."}
            out = json.dumps(payload)
            return out

        role_permissions = data.get("role_permissions", [])
        roles = data.get("roles", [])

        matching_role_ids = {
            rp["role_id"]
            for rp in role_permissions
            if rp.get("permission_id") == permission_id
        }

        matching_roles = [
            role for role in roles if role.get("role_id") in matching_role_ids
        ]
        payload = {"roles": matching_roles}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRolesByPermission",
                "description": "Retrieves a list of roles that have a specific permission assigned.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "permission_id": {
                            "type": "string",
                            "description": "The ID of the permission to look up.",
                        }
                    },
                    "required": ["permission_id"],
                },
            },
        }


class GetUserRoles(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, role_name: str = None) -> str:
        assigned_role_ids = [
            ur["role_id"]
            for ur in data.get("user_roles", [])
            if ur.get("user_id") == user_id
        ]
        role_names = [
            role["role_name"]
            for role in data.get("roles", [])
            if role["role_id"] in assigned_role_ids
        ]
        payload = {"user_id": user_id, "roles": role_names}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserRoles",
                "description": "Retrieves all roles assigned to a specific user.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class GetUserRole(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, role_name: str = None) -> str:
        role_id = None
        for role in data.get("roles", []):
            if role.get("role_name") == role_name:
                role_id = role.get("role_id")
                break
        if not role_id:
            payload = {"error": "Role not found"}
            out = json.dumps(payload)
            return out

        for ur in data.get("user_roles", []):
            if ur.get("user_id") == user_id and ur.get("role_id") == role_id:
                payload = ur
                out = json.dumps(payload)
                return out
        payload = {"error": "User role assignment not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserRoles",
                "description": "Retrieves a specific role assignment for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "role_name": {"type": "string"},
                    },
                    "required": ["user_id", "role_name"],
                },
            },
        }


class RevokeRole(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, role_id: str = None) -> str:
        data["user_roles"] = [
            ur
            for ur in data.get("user_roles", [])
            if not (ur.get("user_id") == user_id and ur.get("role_id") == role_id)
        ]
        payload = {"user_id": user_id, "role_id": role_id, "status": "revoked"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RevokeRole",
                "description": "Removes a role from a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "role_id": {"type": "string"},
                    },
                    "required": ["user_id", "role_id"],
                },
            },
        }


class CreateRole(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], role_name: str = None, description: str = None, is_temporary: bool = False) -> str:
        roles = data.get("roles", [])
        new_id_num = max((int(r["role_id"][4:]) for r in roles), default=0) + 1
        new_role_id = f"ROL-{new_id_num:03d}"
        new_role = {
            "role_id": new_role_id,
            "role_name": role_name,
            "description": description,
            "is_temporary": is_temporary,
        }
        roles.append(new_role)
        data["roles"] = roles
        payload = new_role
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateRole",
                "description": "Creates a new role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_name": {"type": "string"},
                        "description": {"type": "string"},
                        "temporary": {"type": "boolean"},
                    },
                    "required": ["role_name", "description"],
                },
            },
        }


class AssignPermissionToRole(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None, permission_id: str = None) -> str:
        role_permissions = data.get("role_permissions", [])
        assignment = {
            "role_id": role_id,
            "permission_id": permission_id,
        }
        role_permissions.append(assignment)
        data["role_permissions"] = role_permissions
        payload = assignment
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignPermissionToRole",
                "description": "Assigns a permission to a role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {"type": "string"},
                        "permission_id": {"type": "string"},
                    },
                    "required": ["role_id", "permission_id"],
                },
            },
        }


class GetPermissionsByResource(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], resource_id: str = None) -> str:
        for res in data.get("resources", []):
            if res.get("resource_id") == resource_id:
                resource_id = res.get("resource_id")
                break
        if not resource_id:
            payload = {"error": "Resource not found"}
            out = json.dumps(payload)
            return out

        perms = []
        for perm in data.get("permissions", []):
            if perm.get("resource_id") == resource_id:
                perms.append(perm)
        payload = perms
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPermissionsByResource",
                "description": "Retrieves all permissions referencing a given resource.",
                "parameters": {
                    "type": "object",
                    "properties": {"resource_id": {"type": "string"}},
                    "required": ["resource_id"],
                },
            },
        }


class GetPermissionByActionAndResource(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], action: str = None, resource_name: str = None) -> str:
        resource_id = None
        for res in data.get("resources", []):
            if res.get("name") == resource_name:
                resource_id = res.get("resource_id")
                break
        if not resource_id:
            payload = {"error": "Resource not found"}
            out = json.dumps(payload)
            return out

        for perm in data.get("permissions", []):
            if perm.get("action") == action and perm.get("resource_id") == resource_id:
                payload = perm
                out = json.dumps(payload)
                return out
        payload = {"error": "Permission not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getPermissionByActionAndResource",
                "description": "Retrieves a permission based on its action and resource.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string"},
                        "resource_name": {"type": "string"},
                    },
                    "required": ["action", "resource_name"],
                },
            },
        }


class GetRolePermissions(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None) -> str:
        permission_ids = [
            rp["permission_id"]
            for rp in data.get("role_permissions", [])
            if rp.get("role_id") == role_id
        ]
        payload = {"role_id": role_id, "permissions": permission_ids}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRolePermissions",
                "description": "Retrieves all permissions associated with a role.",
                "parameters": {
                    "type": "object",
                    "properties": {"role_id": {"type": "string"}},
                    "required": ["role_id"],
                },
            },
        }


class CreateHubspotTicket(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], subject: str = None, description: str = None, requester_id: int = None, category: str = None, assignee_id: int = None) -> str:
        tickets = data.get("hubspot_tickets", [])
        new_id_num = max((int(t["ticket_id"][3:]) for t in tickets), default=0) + 1
        new_ticket_id = f"TI-{new_id_num:03d}"
        new_ticket = {
            "ticket_id": new_ticket_id,
            "subject": subject,
            "description": description,
            "requester_id": requester_id,
            "category": category,
            "assignee_id": assignee_id,
            "status": "OPEN",
        }
        tickets.append(new_ticket)
        data["hubspot_tickets"] = tickets
        payload = new_ticket
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateHubspotTicket",
                "description": "Creates a new ticket in HubSpot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject": {"type": "string"},
                        "description": {"type": "string"},
                        "requester_id": {"type": "string"},
                        "category": {"type": "string"},
                        "assignee_id": {"type": "string"},
                    },
                    "required": ["subject", "description", "requester_id", "category"],
                },
            },
        }


class SendEmail(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        sender: str = None,
        receiver: str = None,
        subject: str = None,
        text_content: str = None,
        timestamp: str = None
    ) -> str:
        emails = data.get("emails", [])
        new_id_num = max((int(e["email_id"][3:]) for e in emails), default=0) + 1
        new_email_id = f"EM-{new_id_num:03d}"
        new_email = {
            "email_id": new_email_id,
            "sender": sender,
            "receiver": receiver,
            "subject": subject,
            "text_content": text_content,
            "timestamp": timestamp,
        }
        emails.append(new_email)
        data["emails"] = emails
        payload = new_email
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendEmail",
                "description": "Sends an email to a specified recipient.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "receiver": {"type": "string"},
                        "sender": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "subject": {"type": "string"},
                        "text_content": {"type": "string"},
                    },
                    "required": [
                        "receiver",
                        "sender",
                        "timestamp",
                        "subject",
                        "text_content",
                    ],
                },
            },
        }


class SendSlackMessage(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], username: str = None, channel: str = None, message: str = None,
    thread_id: Any = None,
    ) -> str:
        messages = data.get("slack_messages", [])
        new_id_num = max((int(m["message_id"][3:]) for m in messages), default=0) + 1
        new_message_id = f"SL-{new_id_num:03d}"
        new_message = {
            "message_id": new_message_id,
            "username": username,
            "channel": channel,
            "message": message,
            "timestamp": NOW.strftime(DT_STR_FORMAT),
        }
        messages.append(new_message)
        data["slack_messages"] = messages
        payload = new_message
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendSlackMessage",
                "description": "Sends a message to a Slack user or channel.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {"type": "string"},
                        "channel": {"type": "string"},
                        "message": {"type": "string"},
                    },
                    "required": ["username", "channel", "message"],
                },
            },
        }


class WriteAuditLog(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], actor_id: str = None, action_type: str = None, target_id: str = None, timestamp: str = None, details: str = None, thread_id: Any = None) -> str:
        logs = data.get("audit_logs", [])
        new_id_num = max((int(l["log_id"][2:]) for l in logs), default=0) + 1
        new_log_id = f"L-{new_id_num:03d}"
        new_log = {
            "log_id": new_log_id,
            "actor_id": actor_id,
            "action_type": action_type,
            "target_id": target_id,
            "timestamp": timestamp,
            "details": details,
        }
        logs.append(new_log)
        data["audit_logs"] = logs
        payload = new_log
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "WriteAuditLog",
                "description": "Writes an entry to the audit log.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "actor_id": {"type": "string"},
                        "action_type": {"type": "string"},
                        "target_id": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "details": {"type": "string"},
                    },
                    "required": [
                        "actor_id",
                        "action_type",
                        "target_id",
                        "timestamp",
                        "details",
                    ],
                },
            },
        }


class GetUserSessions(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        user_sessions = [
            s for s in data.get("sessions", []) if s.get("user_id") == user_id
        ]
        user_sessions.sort(key=lambda x: x["start_time"], reverse=True)
        payload = {"sessions": user_sessions}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserSessions",
                "description": "Retrieves recent session information for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }


class GetResourceByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        for res in data.get("resources", []):
            if res.get("name") == name:
                payload = res
                out = json.dumps(payload)
                return out
        payload = {"error": "Resource not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetResourceByName",
                "description": "Retrieves a resource by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }


class CreateAccessRequest(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, resource_id: str = None, requested_role_id: str = None, justification: str = None) -> str:
        requests = data.get("access_requests", [])
        new_id_num = max((int(r["request_id"][3:]) for r in requests), default=0) + 1
        new_request_id = f"AR-{new_id_num:03d}"
        new_request = {
            "request_id": new_request_id,
            "user_id": user_id,
            "resource_id": resource_id,
            "requested_role_id": requested_role_id,
            "justification": justification,
            "status": "PENDING",
            "submitted_at": NOW.strftime(DT_STR_FORMAT),
        }
        requests.append(new_request)
        data["access_requests"] = requests
        payload = new_request
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAccessRequest",
                "description": "Creates a new access request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "resource_id": {"type": "string"},
                        "requested_role_id": {"type": "string"},
                        "justification": {"type": "string"},
                    },
                    "required": ["user_id", "requested_role_id", "justification"],
                },
            },
        }


class GetAccessRequestDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], request_id: str = None) -> str:
        for req in data.get("access_requests", []):
            if req.get("request_id") == request_id:
                payload = req
                out = json.dumps(payload)
                return out
        payload = {"error": "Access request not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAccessRequestDetails",
                "description": "Retrieves details for a specific access request.",
                "parameters": {
                    "type": "object",
                    "properties": {"request_id": {"type": "string"}},
                    "required": ["request_id"],
                },
            },
        }


class CreateCertification(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], reviewer_id: str = None, resource_id: str = None, due_date: str = None) -> str:
        certifications = data.get("certifications", [])
        new_id_num = (
            max((int(c["certification_id"][2:]) for c in certifications), default=0) + 1
        )
        new_cert_id = f"C-{new_id_num:03d}"
        new_cert = {
            "certification_id": new_cert_id,
            "reviewer_id": reviewer_id,
            "resource_id": resource_id,
            "status": "PENDING",
            "due_date": due_date,
        }
        certifications.append(new_cert)
        data["certifications"] = certifications
        payload = new_cert
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCertification",
                "description": "Creates a new access certification request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "reviewer_id": {"type": "string"},
                        "resource_id": {"type": "string"},
                        "due_date": {"type": "string", "format": "date-time"},
                    },
                    "required": ["reviewer_id", "resource_id", "due_date"],
                },
            },
        }


class GetCertificationDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], certification_id: str = None,
    user_id: Any = None,
    ) -> str:
        cert_id = certification_id
        for cert in data.get("certifications", []):
            if cert.get("certification_id") == cert_id:
                payload = cert
                out = json.dumps(payload)
                return out
        payload = {"error": "Certification not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCertificationDetails",
                "description": "Retrieves details for a specific certification.",
                "parameters": {
                    "type": "object",
                    "properties": {"certification_id": {"type": "string"}},
                    "required": ["certification_id"],
                },
            },
        }


class CreatePolicyException(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str = None,
        permission_id: str = None,
        reviewed_by: str = None,
        reason: str = None,
        expires_on: str = None
    ) -> str:
        exceptions = data.get("policy_exceptions", [])
        new_id_num = (
            max((int(e["exception_id"][3:]) for e in exceptions), default=0) + 1
        )
        new_exception_id = f"PE-{new_id_num:03d}"
        new_exception = {
            "exception_id": new_exception_id,
            "user_id": user_id,
            "permission_id": permission_id,
            "reviewed_by": reviewed_by,
            "reason": reason,
            "expires_on": expires_on,
            "status": "PENDING_REVIEW",
        }
        exceptions.append(new_exception)
        data["policy_exceptions"] = exceptions
        payload = new_exception
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreatePolicyException",
                "description": "Creates a policy exception for a user and permission.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "permission_id": {"type": "string"},
                        "reviewed_by": {"type": "string"},
                        "reason": {"type": "string"},
                        "expires_on": {"type": "string", "format": "date-time"},
                    },
                    "required": ["user_id", "permission_id", "reason"],
                },
            },
        }


class GetPolicyExceptionDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], exception_id: str = None) -> str:
        for ex in data.get("policy_exceptions", []):
            if ex.get("exception_id") == exception_id:
                payload = ex
                out = json.dumps(payload)
                return out
        payload = {"error": "Policy exception not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPolicyExceptionDetails",
                "description": "Retrieves details for a specific policy exception.",
                "parameters": {
                    "type": "object",
                    "properties": {"exception_id": {"type": "string"}},
                    "required": ["exception_id"],
                },
            },
        }


class GetCurrentTime(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        payload = {"current_time": NOW.strftime(DT_STR_FORMAT)}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCurrentTime",
                "description": "Returns the current date and time.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class GetUsersByRole(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None, role_name: str = None) -> str:
        if not role_id and not role_name:
            payload = {"error": "Either role_id or role_name must be provided"}
            out = json.dumps(payload)
            return out

        if role_name and not role_id:
            for role in data.get("roles", []):
                if role.get("role_name") == role_name:
                    role_id = role.get("role_id")
                    break
            if not role_id:
                payload = {"error": f"Role '{role_name}' not found"}
                out = json.dumps(payload)
                return out

        user_ids = [
            ur["user_id"]
            for ur in data.get("user_roles", [])
            if ur.get("role_id") == role_id
        ]
        payload = {"users": user_ids}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUsersByRole",
                "description": "Retrieves all users assigned a specific role, searching by either role_id or role_name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "string",
                            "description": "The ID of the role to search for.",
                        },
                        "role_name": {
                            "type": "string",
                            "description": "The name of the role to search for (e.g., 'operations-lead').",
                        },
                    },
                },
            },
        }


class CreatePermission(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], action: str = None, resource_id: str = None, description: str = None) -> str:
        permissions = data.get("permissions", [])
        new_id_num = (
            max((int(p["permission_id"][2:]) for p in permissions), default=0) + 1
        )
        new_permission_id = f"P-{new_id_num:03d}"
        new_permission = {
            "permission_id": new_permission_id,
            "action": action,
            "resource_id": resource_id,
            "description": description,
        }
        permissions.append(new_permission)
        data["permissions"] = permissions
        payload = new_permission
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreatePermission",
                "description": "Creates a new permission.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "description": "The action the permission grants (e.g., read, write).",
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "The ID of the resource this permission applies to.",
                        },
                        "description": {
                            "type": "string",
                            "description": "A description of the permission.",
                        },
                    },
                    "required": ["action", "resource_id"],
                },
            },
        }


class CreateResource(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: str = None, owner_id: str = None, criticality: str = None, compliance_scope: str = None) -> str:
        resources = data.get("resources", [])
        new_id_num = max((int(r["resource_id"][4:]) for r in resources), default=0) + 1
        new_resource_id = f"RES-{new_id_num:03d}"
        new_resource = {
            "resource_id": new_resource_id,
            "name": name,
            "owner_id": owner_id,
            "criticality": criticality,
            "compliance_scope": compliance_scope,
        }
        resources.append(new_resource)
        data["resources"] = resources
        payload = new_resource
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateResource",
                "description": "Creates a new resource.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "owner_id": {"type": "string"},
                        "criticality": {"type": "string"},
                        "compliance_scope": {"type": "string"},
                    },
                    "required": ["name", "owner_id", "criticality"],
                },
            },
        }


class UpdateAccessRequestStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], request_id: str = None, status: str = None, reviewed_by: str = None) -> str:
        for req in data.get("access_requests", []):
            if req.get("request_id") == request_id:
                req["status"] = status
                req["reviewed_by"] = reviewed_by
                req["decision_at"] = NOW.strftime(DT_STR_FORMAT)
                payload = req
                out = json.dumps(payload)
                return out
        payload = {"error": "Access request not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAccessRequestStatus",
                "description": "Updates the status of an access request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "status": {"type": "string"},
                        "reviewed_by": {"type": "string"},
                    },
                    "required": ["request_id", "status", "reviewed_by"],
                },
            },
        }


class CreateSiemAlert(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, resource_id: str = None, alert_type: str = None, severity: str = None) -> str:
        alerts = data.get("siem_alerts", [])
        new_id_num = max((int(a["alert_id"][5:]) for a in alerts), default=0) + 1
        new_alert_id = f"ALRT-{new_id_num:03d}"
        new_alert = {
            "alert_id": new_alert_id,
            "user_id": user_id,
            "resource_id": resource_id,
            "alert_type": alert_type,
            "severity": severity,
            "timestamp": NOW.strftime(DT_STR_FORMAT),
        }
        alerts.append(new_alert)
        data["siem_alerts"] = alerts
        payload = new_alert
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createSiemAlert",
                "description": "Creates a new SIEM alert.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "resource_id": {"type": "string"},
                        "alert_type": {"type": "string"},
                        "severity": {"type": "string"},
                    },
                    "required": ["user_id", "resource_id", "alert_type", "severity"],
                },
            },
        }


class UpdatePolicyExceptionStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], exception_id: str = None, status: str = None) -> str:
        for ex in data.get("policy_exceptions", []):
            if ex.get("exception_id") == exception_id:
                ex["status"] = status
                payload = ex
                out = json.dumps(payload)
                return out
        payload = {"error": "Policy exception not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdatePolicyExceptionStatus",
                "description": "Updates the status of a policy exception (e.g., ACTIVE, EXPIRED).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["exception_id", "status"],
                },
            },
        }


class UpdateUserDepartment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, department: str = None) -> str:
        for user in data.get("users", []):
            if user.get("user_id") == user_id:
                user["department"] = department
                payload = user
                out = json.dumps(payload)
                return out
        payload = {"error": "User not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateUserDepartment",
                "description": "Updates the department for a specific user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "department": {"type": "string"},
                    },
                    "required": ["user_id", "department"],
                },
            },
        }


class UpdateUserMfaStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, mfa_enabled: bool = None) -> str:
        for user in data.get("users", []):
            if user.get("user_id") == user_id:
                user["mfa_enabled"] = mfa_enabled
                payload = user
                out = json.dumps(payload)
                return out
        payload = {"error": "User not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateUserMfaStatus",
                "description": "Enables or disables multi-factor authentication for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "mfa_enabled": {"type": "boolean"},
                    },
                    "required": ["user_id", "mfa_enabled"],
                },
            },
        }


class ApprovePolicyException(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], exception_id: str = None, reviewed_by: str = None) -> str:
        for ex in data.get("policy_exceptions", []):
            if ex.get("exception_id") == exception_id:
                ex["status"] = "ACTIVE"
                ex["reviewed_by"] = reviewed_by
                ex["reviewed_on"] = NOW.strftime(DT_STR_FORMAT)
                payload = ex
                out = json.dumps(payload)
                return out
        payload = {"error": "Policy exception not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApprovePolicyException",
                "description": "Approves a pending policy exception.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {"type": "string"},
                        "reviewed_by": {"type": "string"},
                    },
                    "required": ["exception_id", "reviewed_by"],
                },
            },
        }


class UpdateResourceOwner(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], resource_id: str = None, new_owner_id: str = None) -> str:
        for res in data.get("resources", []):
            if res.get("resource_id") == resource_id:
                res["owner_id"] = new_owner_id
                payload = res
                out = json.dumps(payload)
                return out
        payload = {"error": "Resource not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateResourceOwner",
                "description": "Updates the owner of a resource.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {"type": "string"},
                        "new_owner_id": {"type": "string"},
                    },
                    "required": ["resource_id", "new_owner_id"],
                },
            },
        }


class CreateRoleWithPermission(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        permission_name: str,
        resource_id: str,
        permission_description: str = None,
        role_name: str = None,
        role_description: str = None
    ) -> str:
        permissions = data.get("permissions", [])
        roles = data.get("roles", [])
        role_permissions = data.get("role_permissions", [])

        new_perm_id_num = (
            max((int(p["permission_id"][2:]) for p in permissions), default=0) + 1
        )
        new_perm_id = f"P-{new_perm_id_num:03d}"
        new_permission = {
            "permission_id": new_perm_id,
            "action": permission_name,
            "resource_id": resource_id,
            "description": permission_description or f"Permission for the '{role_name}' role.",
        }
        permissions.append(new_permission)
        data["permissions"] = permissions

        new_role_id_num = max((int(r["role_id"][4:]) for r in roles), default=0) + 1
        new_role_id = f"ROL-{new_role_id_num:03d}"
        new_role = {
            "role_id": new_role_id,
            "role_name": role_name,
            "description": role_description or f"Role with permission '{permission_name}'.",
            "is_temporary": False,
        }
        roles.append(new_role)
        data["roles"] = roles

        new_assignment = {"role_id": new_role_id, "permission_id": new_perm_id}
        role_permissions.append(new_assignment)
        data["role_permissions"] = role_permissions
        payload = {"permission_id": new_perm_id, "role_id": new_role_id, "status": "success"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateRoleWithPermission",
                "description": "Creates a new permission and a new role, then assigns the permission to the role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_name": {
                            "type": "string",
                            "description": "The name for the new role (e.g., 'special-report-viewer').",
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "The ID of the resource the permission applies to.",
                        },
                        "permission_name": {
                            "type": "string",
                            "description": "The name of the action for the new permission (e.g., 'read-special-report').",
                        },
                        "permission_description": {
                            "type": "string",
                            "description": "An optional description for the new permission.",
                        },
                        "role_description": {
                            "type": "string",
                            "description": "An optional description for the new role.",
                        },
                    },
                    "required": ["permission_name", "role_name", "resource_id"],
                },
            },
        }


class ListRoles(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        roles = data.get("roles", [])
        payload = {"roles": roles}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListRoles",
                "description": "Lists all available roles in the system.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class UpdateHubspotTicketStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], ticket_id: str = None, status: str = None,
    note: Any = None,
    closed_at: Any = None,
    description: Any = None
    ) -> str:
        for ticket in data.get("hubspot_tickets", []):
            if ticket.get("ticket_id") == ticket_id:
                ticket["status"] = status
                ticket["closed_at"] = NOW.strftime(DT_STR_FORMAT)
                payload = ticket
                out = json.dumps(payload)
                return out
        payload = {"error": "Ticket not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateHubspotTicketStatus",
                "description": "Updates the status of a HubSpot ticket (e.g., OPEN, CLOSED).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {"type": "string"},
                        "status": {"type": "string"},
                        "note": {
                            "type": "string",
                            "description": "An optional note to add when updating the status.",
                        },
                    },
                    "required": ["ticket_id", "status"],
                },
            },
        }


class GetUsersByDepartment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], department: str = None) -> str:
        department_name = department
        users_in_dept = [
            user
            for user in data.get("users", [])
            if user.get("department") == department_name
        ]
        payload = {"users": users_in_dept}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUsersByDepartment",
                "description": "Retrieves all users for a given department by the department's name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department": {
                            "type": "string",
                            "description": "The name of the department to search for (e.g., 'Engineering').",
                        }
                    },
                    "required": ["department"],
                },
            },
        }


class MergeAndDeprecateRole(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], source_role_id: str = None, target_role_id: str = None, actor_id: str = None) -> str:
        source_perms = {
            rp["permission_id"]
            for rp in data.get("role_permissions", [])
            if rp["role_id"] == source_role_id
        }
        target_perms = {
            rp["permission_id"]
            for rp in data.get("role_permissions", [])
            if rp["role_id"] == target_role_id
        }

        perms_to_add = source_perms - target_perms
        for perm_id in perms_to_add:
            data["role_permissions"].append(
                {"role_id": target_role_id, "permission_id": perm_id}
            )

        users_to_migrate = [
            ur["user_id"]
            for ur in data.get("user_roles", [])
            if ur["role_id"] == source_role_id
        ]

        migrated_users = []
        for user_id in users_to_migrate:
            has_target_role = any(
                ur["user_id"] == user_id and ur["role_id"] == target_role_id
                for ur in data.get("user_roles", [])
            )
            if not has_target_role:
                new_id_num = (
                    max(
                        (int(ur["user_role_id"][3:]) for ur in data["user_roles"]),
                        default=0,
                    )
                    + 1
                )
                new_user_role_id = f"UR-{new_id_num:03d}"
                data["user_roles"].append(
                    {
                        "user_role_id": new_user_role_id,
                        "user_id": user_id,
                        "role_id": target_role_id,
                        "assigned_by": actor_id,
                        "assigned_on": NOW.strftime(DT_STR_FORMAT),
                        "expires_on": None,
                    }
                )
                migrated_users.append(user_id)

        data["user_roles"] = [
            ur
            for ur in data.get("user_roles", [])
            if ur.get("role_id") != source_role_id
        ]

        for role in data.get("roles", []):
            if role.get("role_id") == source_role_id:
                role["role_name"] = f"DEPRECATED-{role['role_name']}"
                role["description"] = f"[DEPRECATED] Merged into {target_role_id}."
                break
        payload = {
                "source_role_id": source_role_id,
                "target_role_id": target_role_id,
                "permissions_migrated": len(perms_to_add),
                "users_reassigned": len(migrated_users),
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "MergeAndDeprecateRole",
                "description": "Merges permissions and users from a source role into a target role, then deprecates the source role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_role_id": {"type": "string"},
                        "target_role_id": {"type": "string"},
                        "actor_id": {"type": "string"},
                    },
                    "required": ["source_role_id", "target_role_id", "actor_id"],
                },
            },
        }


class UpdateRoleDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None, new_name: str = None, new_description: str = None) -> str:
        for role in data.get("roles", []):
            if role.get("role_id") == role_id:
                if new_name:
                    role["role_name"] = new_name
                if new_description:
                    role["description"] = new_description
                payload = role
                out = json.dumps(payload)
                return out
        payload = {"error": "Role not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateRoleDetails",
                "description": "Updates the name and/or description of an existing role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {"type": "string"},
                        "new_name": {
                            "type": "string",
                            "description": "The new name for the role.",
                        },
                        "new_description": {
                            "type": "string",
                            "description": "The new description for the role.",
                        },
                    },
                    "required": ["role_id"],
                },
            },
        }


class ListInactiveUsers(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], inactive_since: str) -> str:
        inactive_since_dt = datetime.strptime(inactive_since, DT_STR_FORMAT)

        active_user_ids = {
            session["user_id"]
            for session in data.get("user_sessions", [])
            if datetime.strptime(session["end_time"], DT_STR_FORMAT)
            >= inactive_since_dt
        }

        all_user_ids = {user["user_id"] for user in data.get("users", [])}
        inactive_user_ids = list(all_user_ids - active_user_ids)
        payload = {"inactive_users": inactive_user_ids}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListInactiveUsers",
                "description": "Lists users who have not had a session since the specified date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inactive_since": {
                            "type": "string",
                            "description": "The date in ISO 8601 format (e.g., '2025-05-01T00:00:00Z').",
                        }
                    },
                    "required": ["inactive_since"],
                },
            },
        }


class TerminateUserSession(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], session_id: str = None) -> str:
        sessions = data.get("user_sessions", [])
        terminated = False
        for session in sessions:
            if session.get("session_id") == session_id:
                session["end_time"] = NOW.strftime(DT_STR_FORMAT)
                session["status"] = "TERMINATED"
                terminated = True
                break

        if terminated:
            payload = session
            out = json.dumps(payload)
            return out
        payload = {"error": "Session not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "terminateUserSession",
                "description": "Terminates a user's active session.",
                "parameters": {
                    "type": "object",
                    "properties": {"session_id": {"type": "string"}},
                    "required": ["session_id"],
                },
            },
        }


class UpdateUserDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, new_username: str = None, new_email: str = None) -> str:
        for user in data.get("users", []):
            if user.get("user_id") == user_id:
                if new_username:
                    user["username"] = new_username
                if new_email:
                    user["email"] = new_email
                payload = user
                out = json.dumps(payload)
                return out
        payload = {"error": "User not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateUserDetails",
                "description": "Updates a user's username and/or email address.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "new_username": {"type": "string"},
                        "new_email": {"type": "string"},
                    },
                    "required": ["user_id"],
                },
            },
        }


class UpdateHubspotTicketAssignee(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], ticket_id: str = None, new_assignee_id: str = None) -> str:
        for ticket in data.get("hubspot_tickets", []):
            if ticket.get("ticket_id") == ticket_id:
                ticket["assignee_id"] = new_assignee_id
                ticket["updated_at"] = NOW.strftime(DT_STR_FORMAT)
                payload = ticket
                out = json.dumps(payload)
                return out
        payload = {"error": "Ticket not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateHubspotTicketAssignee",
                "description": "Updates the assignee of an existing HubSpot ticket.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {
                            "type": "string",
                            "description": "The ID of the ticket to update.",
                        },
                        "new_assignee_id": {
                            "type": "string",
                            "description": "The user_id of the new assignee.",
                        },
                    },
                    "required": ["ticket_id", "new_assignee_id"],
                },
            },
        }


class GetHubspotTicketsByRequester(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], requester_id: str = None) -> str:
        matching_tickets = [
            ticket
            for ticket in data.get("hubspot_tickets", [])
            if ticket.get("requester_id") == requester_id
        ]
        payload = {"tickets": matching_tickets}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetHubspotTicketsByRequester",
                "description": "Retrieves a list of HubSpot tickets based on the requester's user ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "requester_id": {
                            "type": "string",
                            "description": "The user_id of the person who requested the tickets.",
                        }
                    },
                    "required": ["requester_id"],
                },
            },
        }


class GetHubspotTicketsByAssignee(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], assignee_id: str = None) -> str:
        matching_tickets = [
            ticket
            for ticket in data.get("hubspot_tickets", [])
            if ticket.get("assignee_id") == assignee_id
        ]
        payload = {"tickets": matching_tickets}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetHubspotTicketsByAssignee",
                "description": "Retrieves a list of HubSpot tickets based on the assignee's user ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "assignee_id": {
                            "type": "string",
                            "description": "The user_id of the person to whom the tickets are assigned.",
                        }
                    },
                    "required": ["assignee_id"],
                },
            },
        }


class GetResourcesByOwner(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], owner_id: str = None) -> str:
        owned_resources = [
            resource
            for resource in data.get("resources", [])
            if resource.get("owner_id") == owner_id
        ]
        payload = {"resources": owned_resources}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetResourcesByOwner",
                "description": "Retrieves a list of all resources owned by a specific user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner_id": {
                            "type": "string",
                            "description": "The user_id of the resource owner.",
                        }
                    },
                    "required": ["owner_id"],
                },
            },
        }


class GetPermissionDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], permission_id: str = None, permission_name: str = None) -> str:
        if not permission_id and not permission_name:
            payload = {"error": "Either permission_id or permission_name must be provided."}
            out = json.dumps(payload)
            return out

        for permission in data.get("permissions", []):
            if permission_id and permission.get("permission_id") == permission_id:
                payload = permission
                out = json.dumps(payload)
                return out
            if permission_name and permission.get("action") == permission_name:
                payload = permission
                out = json.dumps(payload)
                return out
        payload = {"error": "Permission not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPermissionDetails",
                "description": "Retrieves the full details of a permission by its ID or name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "permission_id": {
                            "type": "string",
                            "description": "The ID of the permission to retrieve.",
                        },
                        "permission_name": {
                            "type": "string",
                            "description": "The name (action) of the permission to retrieve.",
                        },
                    },
                },
            },
        }


class GetSiemAlerts(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        matching_alerts = [
            alert
            for alert in data.get("siem_alerts", [])
            if alert.get("user_id") == user_id
        ]
        payload = {"alerts": matching_alerts}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSiemAlerts",
                "description": "Retrieves a list of SIEM alerts based on the user's ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user_id to retrieve SIEM alerts for.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }


class RemovePermissionFromRole(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None, permission_id: str = None) -> str:
        if not role_id or not permission_id:
            payload = {"error": "Both role_id and permission_id must be provided."}
            out = json.dumps(payload)
            return out

        role_permissions = data.get("role_permissions", [])

        initial_len = len(role_permissions)

        updated_permissions = [
            rp
            for rp in role_permissions
            if not (
                rp.get("role_id") == role_id
                and rp.get("permission_id") == permission_id
            )
        ]

        if len(updated_permissions) < initial_len:
            data["role_permissions"] = updated_permissions
            payload = {
                "role_id": role_id,
                "permission_id": permission_id,
                "status": "removed",
            }
            out = json.dumps(payload)
            return out
        else:
            payload = {"error": "Permission not found on the specified role."}
            out = json.dumps(payload)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemovePermissionFromRole",
                "description": "Removes a specific permission from a role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "string",
                            "description": "The ID of the role to modify.",
                        },
                        "permission_id": {
                            "type": "string",
                            "description": "The ID of the permission to remove.",
                        },
                    },
                    "required": ["role_id", "permission_id"],
                },
            },
        }


class RemoveRole(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None) -> str:
        role_id_to_remove = role_id

        if not role_id_to_remove:
            payload = {"error": "role_id must be provided."}
            out = json.dumps(payload)
            return out

        roles = data.get("roles", [])
        initial_roles_len = len(roles)
        updated_roles = [
            role for role in roles if role.get("role_id") != role_id_to_remove
        ]

        if len(updated_roles) == initial_roles_len:
            payload = {"error": "Role not found."}
            out = json.dumps(payload)
            return out

        data["roles"] = updated_roles

        role_permissions = data.get("role_permissions", [])
        updated_role_permissions = [
            rp for rp in role_permissions if rp.get("role_id") != role_id_to_remove
        ]
        data["role_permissions"] = updated_role_permissions

        user_roles = data.get("user_roles", [])
        updated_user_roles = [
            ur for ur in user_roles if ur.get("role_id") != role_id_to_remove
        ]
        data["user_roles"] = updated_user_roles
        payload = {"role_id": role_id_to_remove, "status": "removed"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "removeRole",
                "description": "Deletes a role from the system, including all associated user and permission assignments.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "string",
                            "description": "The ID of the role to be removed.",
                        }
                    },
                    "required": ["role_id"],
                },
            },
        }


class RemovePermission(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], permission_id: str = None) -> str:
        permission_id_to_remove = permission_id

        if not permission_id_to_remove:
            payload = {"error": "permission_id must be provided."}
            out = json.dumps(payload)
            return out

        permissions = data.get("permissions", [])
        initial_permissions_len = len(permissions)
        updated_permissions = [
            p for p in permissions if p.get("permission_id") != permission_id_to_remove
        ]

        if len(updated_permissions) == initial_permissions_len:
            payload = {"error": "Permission not found."}
            out = json.dumps(payload)
            return out

        data["permissions"] = updated_permissions

        role_permissions = data.get("role_permissions", [])
        updated_role_permissions = [
            rp
            for rp in role_permissions
            if rp.get("permission_id") != permission_id_to_remove
        ]
        data["role_permissions"] = updated_role_permissions
        payload = {"permission_id": permission_id_to_remove, "status": "removed"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "removePermission",
                "description": "Deletes a permission from the system, including its assignments to any roles.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "permission_id": {
                            "type": "string",
                            "description": "The ID of the permission to be removed.",
                        }
                    },
                    "required": ["permission_id"],
                },
            },
        }


TOOLS = [
    CreateUser(),
    GetUserByUsername(),
    GetUserById(),
    GetUserByName(),
    UpdateUserStatus(),
    GetActiveUsersByDepartment(),
    GetRoleByName(),
    GetRolesByPermission(),
    GrantRole(),
    GetUserRoles(),
    GetUserRole(),
    RevokeRole(),
    CreateRole(),
    AssignPermissionToRole(),
    GetPermissionsByResource(),
    GetPermissionByActionAndResource(),
    GetRolePermissions(),
    CreateHubspotTicket(),
    SendEmail(),
    SendSlackMessage(),
    WriteAuditLog(),
    GetUserSessions(),
    GetResourceByName(),
    CreateAccessRequest(),
    GetAccessRequestDetails(),
    CreateCertification(),
    GetCertificationDetails(),
    CreatePolicyException(),
    GetPolicyExceptionDetails(),
    GetCurrentTime(),
    GetUsersByRole(),
    CreatePermission(),
    CreateResource(),
    UpdateAccessRequestStatus(),
    CreateSiemAlert(),
    UpdatePolicyExceptionStatus(),
    UpdateUserDepartment(),
    UpdateUserMfaStatus(),
    ApprovePolicyException(),
    UpdateResourceOwner(),
    CreateRoleWithPermission(),
    ListRoles(),
    UpdateHubspotTicketStatus(),
    GetUsersByDepartment(),
    MergeAndDeprecateRole(),
    UpdateRoleDetails(),
    ListInactiveUsers(),
    TerminateUserSession(),
    UpdateUserDetails(),
    UpdateHubspotTicketAssignee(),
    GetHubspotTicketsByRequester(),
    GetHubspotTicketsByAssignee(),
    GetResourcesByOwner(),
    GetPermissionDetails(),
    GetSiemAlerts(),
    RemovePermissionFromRole(),
    RemoveRole(),
    RemovePermission(),
]
