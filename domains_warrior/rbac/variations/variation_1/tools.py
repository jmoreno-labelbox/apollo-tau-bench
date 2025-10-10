import json
from datetime import date, datetime, time, timedelta, UTC
from typing import Any, Dict, List

from domains.dto import Tool

NOW: datetime = datetime(2025, 8, 8, 9, 56, 15, tzinfo=UTC)

DT_STR_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


class CreateUser(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        users = data.get('users', [])
        new_id_num = max((int(u['user_id'][2:]) for u in users), default=0) + 1
        new_user_id = f"U-{new_id_num:03d}"
        new_user = {
                "user_id": new_user_id,
                "username": kwargs.get("username"),
                "email": kwargs.get("email"),
                "department": kwargs.get("department"),
                "status": kwargs.get("status"),
                "mfa_enabled": False
        }
        users.append(new_user)
        data['users'] = users
        return json.dumps(new_user)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "create_user",
                        "description": "Creates a new user in the system.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "username": {
                                                "type": "string",
                                                "description": "The username for the new user."
                                        },
                                        "email": {
                                                "type": "string",
                                                "description": "The email address for the new user."
                                        },
                                        "department": {
                                                "type": "string",
                                                "description": "The department the user belongs to."
                                        },
                                        "status": {
                                                "type": "string",
                                                "description": "The initial status of the user account (e.g., ACTIVE)."
                                        }
                                },
                                "required": ["username", "email", "department", "status"]
                        }
                }
        }


class GetUserByUsername(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        username = kwargs.get("username")
        for user in data.get('users', []):
            if user.get('username') == username:
                return json.dumps(user)
        return json.dumps({"error": "User not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_user_by_username",
                        "description": "Retrieves user details based on their username.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "username": {
                                                "type": "string",
                                                "description": "The username to search for."
                                        }
                                },
                                "required": ["username"]
                        }
                }
        }

class GetUserById(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        for user in data.get('users', []):
            if user.get('user_id') == user_id:
                return json.dumps(user)
        return json.dumps({"error": "User not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_user_by_id",
                        "description": "Retrieves user details based on user ID.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "user_id": {
                                                "type": "string",
                                                "description": "The user ID to search for."
                                        }
                                },
                                "required": ["user_id"]
                        }
                }
        }

class GetUserByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        first_name = kwargs.get("first_name", "").lower()
        last_name = kwargs.get("last_name", "").lower()
        username_to_find = f"{first_name[0]}{last_name}" if first_name else last_name
        for user in data.get('users', []):
            if user.get('username') == username_to_find:
                return json.dumps(user)
        return json.dumps({"error": "User not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_user_by_name",
                        "description": "Retrieves user details based on their first and last name.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "first_name": {
                                                "type": "string",
                                                "description": "The first name of the user."
                                        },
                                        "last_name": {
                                                "type": "string",
                                                "description": "The last name of the user."
                                        }
                                },
                                "required": ["first_name", "last_name"]
                        }
                }
        }


class UpdateUserStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        new_status = kwargs.get("status")
        for user in data.get('users', []):
            if user.get('user_id') == user_id:
                user['status'] = new_status
                return json.dumps({"user_id": user_id, "status": new_status})
        return json.dumps({"error": "User not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "update_user_status",
                        "description": "Updates the status of a user's account (e.g., ACTIVE, DISABLED).",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "user_id": {
                                                "type": "string",
                                                "description": "The ID of the user to update."
                                        },
                                        "status": {
                                                "type": "string",
                                                "description": "The new status for the user account."
                                        }
                                },
                                "required": ["user_id", "status"]
                        }
                }
        }


class GetActiveUsersByDepartment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        department = kwargs.get("department")
        active_users = [
                user['user_id'] for user in data.get('users', [])
                if user.get('department') == department and user.get('status') == 'ACTIVE'
        ]
        return json.dumps({"users": active_users})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_active_users_by_department",
                        "description": "Retrieves a list of active users for a specific department.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "department": {
                                                "type": "string",
                                                "description": "The department to filter by."
                                        }
                                },
                                "required": ["department"]
                        }
                }
        }


class GetRoleByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role_name = kwargs.get("role_name")
        for role in data.get('roles', []):
            if role.get('role_name') == role_name:
                return json.dumps(role)
        return json.dumps({"error": "Role not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_role_by_name",
                        "description": "Retrieves role details based on the role name.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "role_name": {
                                                "type": "string",
                                                "description": "The name of the role to search for."
                                        }
                                },
                                "required": ["role_name"]
                        }
                }
        }


class GrantRole(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_roles = data.get('user_roles', [])

        new_id_num = max([int(ur["user_role_id"][3:]) for ur in user_roles], default=0) + 1
        new_user_role_id = f"UR-{new_id_num:03d}"
        new_assignment = {
                "user_role_id": new_user_role_id,
                "user_id": kwargs.get("user_id"),
                "role_id": kwargs.get("role_id"),
                "assigned_by": kwargs.get("assigned_by"),
                "expires_on": kwargs.get("expires_on")
        }
        user_roles.append(new_assignment)
        data['user_roles'] = user_roles
        return json.dumps(new_assignment)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "grant_role",
                        "description": "Assigns a role to a user.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "user_id": {"type": "string"},
                                        "role_id": {"type": "string"},
                                        "assigned_by": {"type": "string"},
                                        "expires_on": {"type": "string", "format": "date-time"}
                                },
                                "required": ["user_id", "role_id", "assigned_by"]
                        }
                }
        }


class GetRolesByPermission(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        permission_id = kwargs.get("permission_id")

        if not permission_id:
            return json.dumps({"error": "permission_id must be provided."})

        role_permissions = data.get('role_permissions', [])
        roles = data.get('roles', [])

        matching_role_ids = {
                rp['role_id'] for rp in role_permissions
                if rp.get('permission_id') == permission_id
        }

        matching_roles = [
                role for role in roles
                if role.get('role_id') in matching_role_ids
        ]

        return json.dumps({"roles": matching_roles})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_roles_by_permission",
                        "description": "Retrieves a list of roles that have a specific permission assigned.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "permission_id": {
                                                "type": "string",
                                                "description": "The ID of the permission to look up."
                                        }
                                },
                                "required": ["permission_id"]
                        }
                }
        }

class GetUserRoles(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        assigned_role_ids = [
                ur['role_id'] for ur in data.get('user_roles', [])
                if ur.get('user_id') == user_id
        ]
        role_names = [
                role['role_name'] for role in data.get('roles', [])
                if role['role_id'] in assigned_role_ids
        ]
        return json.dumps({"user_id": user_id, "roles": role_names})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_user_roles",
                        "description": "Retrieves all roles assigned to a specific user.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "user_id": {"type": "string"}
                                },
                                "required": ["user_id"]
                        }
                }
        }


class GetUserRole(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        role_name = kwargs.get("role_name")
        role_id = None
        for role in data.get('roles', []):
            if role.get('role_name') == role_name:
                role_id = role.get('role_id')
                break
        if not role_id:
            return json.dumps({"error": "Role not found"})

        for ur in data.get('user_roles', []):
            if ur.get('user_id') == user_id and ur.get('role_id') == role_id:
                return json.dumps(ur)
        return json.dumps({"error": "User role assignment not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_user_role",
                        "description": "Retrieves a specific role assignment for a user.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "user_id": {"type": "string"},
                                        "role_name": {"type": "string"}
                                },
                                "required": ["user_id", "role_name"]
                        }
                }
        }


class RevokeRole(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        role_id = kwargs.get("role_id")
        data['user_roles'] = [
                ur for ur in data.get('user_roles', [])
                if not (ur.get('user_id') == user_id and ur.get('role_id') == role_id)
        ]
        return json.dumps({"user_id": user_id, "role_id": role_id, "status": "revoked"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "revoke_role",
                        "description": "Removes a role from a user.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "user_id": {"type": "string"},
                                        "role_id": {"type": "string"}
                                },
                                "required": ["user_id", "role_id"]
                        }
                }
        }


class CreateRole(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        roles = data.get('roles', [])
        new_id_num = max((int(r['role_id'][4:]) for r in roles), default=0) + 1
        new_role_id = f"ROL-{new_id_num:03d}"
        new_role = {
                "role_id": new_role_id,
                "role_name": kwargs.get("role_name"),
                "description": kwargs.get("description"),
                "is_temporary": kwargs.get("is_temporary", False),
        }
        roles.append(new_role)
        data['roles'] = roles
        return json.dumps(new_role)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "create_role",
                        "description": "Creates a new role.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "role_name": {"type": "string"},
                                        "description": {"type": "string"},
                                        "temporary": {"type": "bool"}
                                },
                                "required": ["role_name", "description"]
                        }
                }
        }


class AssignPermissionToRole(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role_permissions = data.get('role_permissions', [])
        assignment = {
                "role_id": kwargs.get("role_id"),
                "permission_id": kwargs.get("permission_id")
        }
        role_permissions.append(assignment)
        data['role_permissions'] = role_permissions
        return json.dumps(assignment)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "assign_permission_to_role",
                        "description": "Assigns a permission to a role.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "role_id": {"type": "string"},
                                        "permission_id": {"type": "string"}
                                },
                                "required": ["role_id", "permission_id"]
                        }
                }
        }

class GetPermissionsByResource(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        resource_id = kwargs.get("resource_id")
        for res in data.get('resources', []):
            if res.get('resource_id') == resource_id:
                resource_id = res.get('resource_id')
                break
        if not resource_id:
            return json.dumps({"error": "Resource not found"})

        perms = []
        for perm in data.get('permissions', []):
            if perm.get('resource_id') == resource_id:
                perms.append(perm)
        return json.dumps(perms)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_permissions_by_resource",
                        "description": "Retrieves all permissions referencing a given resource.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "resource_id": {"type": "string"}
                                },
                                "required": ["resource_id"]
                        }
                }
        }

class GetPermissionByActionAndResource(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        action = kwargs.get("action")
        resource_name = kwargs.get("resource_name")
        resource_id = None
        for res in data.get('resources', []):
            if res.get('name') == resource_name:
                resource_id = res.get('resource_id')
                break
        if not resource_id:
            return json.dumps({"error": "Resource not found"})

        for perm in data.get('permissions', []):
            if perm.get('action') == action and perm.get('resource_id') == resource_id:
                return json.dumps(perm)
        return json.dumps({"error": "Permission not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_permission_by_action_and_resource",
                        "description": "Retrieves a permission based on its action and resource.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "action": {"type": "string"},
                                        "resource_name": {"type": "string"}
                                },
                                "required": ["action", "resource_name"]
                        }
                }
        }


class GetRolePermissions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role_id = kwargs.get("role_id")
        permission_ids = [
                rp['permission_id'] for rp in data.get('role_permissions', [])
                if rp.get('role_id') == role_id
        ]
        return json.dumps({"role_id": role_id, "permissions": permission_ids})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_role_permissions",
                        "description": "Retrieves all permissions associated with a role.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "role_id": {"type": "string"}
                                },
                                "required": ["role_id"]
                        }
                }
        }


class CreateHubspotTicket(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        tickets = data.get('hubspot_tickets', [])
        new_id_num = max((int(t['ticket_id'][3:]) for t in tickets), default=0) + 1
        new_ticket_id = f"TI-{new_id_num:03d}"
        new_ticket = {
                "ticket_id": new_ticket_id,
                "subject": kwargs.get("subject"),
                "description": kwargs.get("description"),
                "requester_id": kwargs.get("requester_id"),
                "category": kwargs.get("category"),
                "assignee_id": kwargs.get("assignee_id"),
                "status": "OPEN"
        }
        tickets.append(new_ticket)
        data['hubspot_tickets'] = tickets
        return json.dumps(new_ticket)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "create_hubspot_ticket",
                        "description": "Creates a new ticket in HubSpot.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "subject": {"type": "string"},
                                        "description": {"type": "string"},
                                        "requester_id": {"type": "string"},
                                        "category": {"type": "string"},
                                        "assignee_id": {"type": "string"}
                                },
                                "required": ["subject", "description", "requester_id", "category"]
                        }
                }
        }


class SendEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        emails = data.get('emails', [])
        new_id_num = max((int(e['email_id'][3:]) for e in emails), default=0) + 1
        new_email_id = f"EM-{new_id_num:03d}"
        new_email = {
                "email_id": new_email_id,
                "sender": kwargs.get("sender"),
                "receiver": kwargs.get("receiver"),
                "subject": kwargs.get("subject"),
                "text_content": kwargs.get("text_content"),
                "timestamp": kwargs.get("timestamp"),
        }
        emails.append(new_email)
        data['emails'] = emails
        return json.dumps(new_email)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "send_email",
                        "description": "Sends an email to a specified recipient.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "receiver": {"type": "string"},
                                        "sender": {"type": "string"},
                                        "timestamp": {"type": "string"},
                                        "subject": {"type": "string"},
                                        "text_content": {"type": "string"}
                                },
                                "required": ["receiver", "sender", "timestamp", "subject", "text_content"]
                        }
                }
        }


class SendSlackMessage(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        messages = data.get('slack_messages', [])
        new_id_num = max((int(m['message_id'][3:]) for m in messages), default=0) + 1
        new_message_id = f"SL-{new_id_num:03d}"
        new_message = {
                "message_id": new_message_id,
                "username": kwargs.get("username"),
                "channel": kwargs.get("channel"),
                "message": kwargs.get("message"),
                "timestamp": NOW.strftime(DT_STR_FORMAT)
        }
        messages.append(new_message)
        data['slack_messages'] = messages
        return json.dumps(new_message)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "send_slack_message",
                        "description": "Sends a message to a Slack user or channel.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "username": {"type": "string"},
                                        "channel": {"type": "string"},
                                        "message": {"type": "string"}
                                },
                                "required": ["username", "channel", "message"]
                        }
                }
        }


class WriteAuditLog(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        logs = data.get('audit_logs', [])
        new_id_num = max((int(l['log_id'][2:]) for l in logs), default=0) + 1
        new_log_id = f"L-{new_id_num:03d}"
        new_log = {
                "log_id": new_log_id,
                "actor_id": kwargs.get("actor_id"),
                "action_type": kwargs.get("action_type"),
                "target_id": kwargs.get("target_id"),
                "timestamp": kwargs.get("timestamp"),
                "details": kwargs.get("details"),
        }
        logs.append(new_log)
        data['audit_logs'] = logs
        return json.dumps(new_log)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "write_audit_log",
                        "description": "Writes an entry to the audit log.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "actor_id": {"type": "string"},
                                        "action_type": {"type": "string"},
                                        "target_id": {"type": "string"},
                                        "timestamp": {"type": "string"},
                                        "details": {"type": "string"}
                                },
                                "required": ["actor_id", "action_type", "target_id", "timestamp", "details"]
                        }
                }
        }


class GetUserSessions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        user_sessions = [
                s for s in data.get('sessions', []) if s.get('user_id') == user_id
        ]
        user_sessions.sort(key=lambda x: x['start_time'], reverse=True)
        return json.dumps({"sessions": user_sessions})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_user_sessions",
                        "description": "Retrieves recent session information for a user.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "user_id": {"type": "string"}
                                },
                                "required": ["user_id"]
                        }
                }
        }


class GetResourceByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get("name")
        for res in data.get('resources', []):
            if res.get('name') == name:
                return json.dumps(res)
        return json.dumps({"error": "Resource not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_resource_by_name",
                        "description": "Retrieves a resource by its name.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "name": {"type": "string"}
                                },
                                "required": ["name"]
                        }
                }
        }


class CreateAccessRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        requests = data.get('access_requests', [])
        new_id_num = max((int(r['request_id'][3:]) for r in requests), default=0) + 1
        new_request_id = f"AR-{new_id_num:03d}"
        new_request = {
                "request_id": new_request_id,
                "user_id": kwargs.get("user_id"),
                "resource_id": kwargs.get("resource_id"),
                "requested_role_id": kwargs.get("requested_role_id"),
                "justification": kwargs.get("justification"),
                "status": "PENDING",
                "submitted_at": NOW.strftime(DT_STR_FORMAT)
        }
        requests.append(new_request)
        data['access_requests'] = requests
        return json.dumps(new_request)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "create_access_request",
                        "description": "Creates a new access request.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "user_id": {"type": "string"},
                                        "resource_id": {"type": "string"},
                                        "requested_role_id": {"type": "string"},
                                        "justification": {"type": "string"}
                                },
                                "required": ["user_id", "requested_role_id", "justification"]
                        }
                }
        }


class GetAccessRequestDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        request_id = kwargs.get("request_id")
        for req in data.get('access_requests', []):
            if req.get('request_id') == request_id:
                return json.dumps(req)
        return json.dumps({"error": "Access request not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_access_request_details",
                        "description": "Retrieves details for a specific access request.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "request_id": {"type": "string"}
                                },
                                "required": ["request_id"]
                        }
                }
        }


class CreateCertification(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        certifications = data.get('certifications', [])
        new_id_num = max((int(c['certification_id'][2:]) for c in certifications), default=0) + 1
        new_cert_id = f"C-{new_id_num:03d}"
        new_cert = {
                "certification_id": new_cert_id,
                "reviewer_id": kwargs.get("reviewer_id"),
                "resource_id": kwargs.get("resource_id"),
                "status": "PENDING",
                "due_date": kwargs.get("due_date")
        }
        certifications.append(new_cert)
        data['certifications'] = certifications
        return json.dumps(new_cert)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "create_certification",
                        "description": "Creates a new access certification request.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "reviewer_id": {"type": "string"},
                                        "resource_id": {"type": "string"},
                                        "due_date": {"type": "string", "format": "date-time"}
                                },
                                "required": ["reviewer_id", "resource_id", "due_date"]
                        }
                }
        }


class GetCertificationDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cert_id = kwargs.get("certification_id")
        for cert in data.get('certifications', []):
            if cert.get('certification_id') == cert_id:
                return json.dumps(cert)
        return json.dumps({"error": "Certification not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_certification_details",
                        "description": "Retrieves details for a specific certification.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "certification_id": {"type": "string"}
                                },
                                "required": ["certification_id"]
                        }
                }
        }


class CreatePolicyException(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        exceptions = data.get('policy_exceptions', [])
        new_id_num = max((int(e['exception_id'][3:]) for e in exceptions), default=0) + 1
        new_exception_id = f"PE-{new_id_num:03d}"
        new_exception = {
                "exception_id": new_exception_id,
                "user_id": kwargs.get("user_id"),
                "permission_id": kwargs.get("permission_id"),
                "reviewed_by": kwargs.get("reviewed_by"),
                "reason": kwargs.get("reason"),
                "expires_on": kwargs.get("expires_on"),
                "status": "PENDING_REVIEW"
        }
        exceptions.append(new_exception)
        data['policy_exceptions'] = exceptions
        return json.dumps(new_exception)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "create_policy_exception",
                        "description": "Creates a policy exception for a user and permission.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "user_id": {"type": "string"},
                                        "permission_id": {"type": "string"},
                                        "reviewed_by": {"type": "string"},
                                        "reason": {"type": "string"},
                                        "expires_on": {"type": "string", "format": "date-time"}
                                },
                                "required": ["user_id", "permission_id", "reason"]
                        }
                }
        }

class GetPolicyExceptionDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        exception_id = kwargs.get("exception_id")
        for ex in data.get('policy_exceptions', []):
            if ex.get('exception_id') == exception_id:
                return json.dumps(ex)
        return json.dumps({"error": "Policy exception not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_policy_exception_details",
                        "description": "Retrieves details for a specific policy exception.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "exception_id": {"type": "string"}
                                },
                                "required": ["exception_id"]
                        }
                }
        }


class GetCurrentTime(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"current_time": NOW.strftime(DT_STR_FORMAT)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_current_time",
                        "description": "Returns the current date and time.",
                        "parameters": {
                                "type": "object",
                                "properties": {},
                                "required": []
                        }
                }
        }

class GetUsersByRole(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role_id = kwargs.get("role_id")
        role_name = kwargs.get("role_name")

        if not role_id and not role_name:
            return json.dumps({"error": "Either role_id or role_name must be provided"})

        if role_name and not role_id:
            for role in data.get('roles', []):
                if role.get('role_name') == role_name:
                    role_id = role.get('role_id')
                    break
            if not role_id:
                return json.dumps({"error": f"Role '{role_name}' not found"})

        user_ids = [
                ur['user_id'] for ur in data.get('user_roles', [])
                if ur.get('role_id') == role_id
        ]
        return json.dumps({"users": user_ids})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_users_by_role",
                        "description": "Retrieves all users assigned a specific role, searching by either role_id or role_name.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "role_id": {
                                                "type": "string",
                                                "description": "The ID of the role to search for."
                                        },
                                        "role_name": {
                                                "type": "string",
                                                "description": "The name of the role to search for (e.g., 'operations-lead')."
                                        }
                                }
                        }
                }
        }


class CreatePermission(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        permissions = data.get('permissions', [])
        new_id_num = max((int(p['permission_id'][2:]) for p in permissions), default=0) + 1
        new_permission_id = f"P-{new_id_num:03d}"
        new_permission = {
                "permission_id": new_permission_id,
                "action": kwargs.get("action"),
                "resource_id": kwargs.get("resource_id"),
                "description": kwargs.get("description")
        }
        permissions.append(new_permission)
        data['permissions'] = permissions
        return json.dumps(new_permission)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "create_permission",
                        "description": "Creates a new permission.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "action": {
                                                "type": "string",
                                                "description": "The action the permission grants (e.g., read, write)."
                                        },
                                        "resource_id": {
                                                "type": "string",
                                                "description": "The ID of the resource this permission applies to."
                                        },
                                        "description": {
                                                "type": "string",
                                                "description": "A description of the permission."
                                        }
                                },
                                "required": ["action", "resource_id"]
                        }
                }
        }


class CreateResource(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        resources = data.get('resources', [])
        new_id_num = max((int(r['resource_id'][4:]) for r in resources), default=0) + 1
        new_resource_id = f"RES-{new_id_num:03d}"
        new_resource = {
                "resource_id": new_resource_id,
                "name": kwargs.get("name"),
                "owner_id": kwargs.get("owner_id"),
                "criticality": kwargs.get("criticality"),
                "compliance_scope": kwargs.get("compliance_scope")
        }
        resources.append(new_resource)
        data['resources'] = resources
        return json.dumps(new_resource)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "create_resource",
                        "description": "Creates a new resource.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "name": {"type": "string"},
                                        "owner_id": {"type": "string"},
                                        "criticality": {"type": "string"},
                                        "compliance_scope": {"type": "string"}
                                },
                                "required": ["name", "owner_id", "criticality"]
                        }
                }
        }


class UpdateAccessRequestStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        request_id = kwargs.get("request_id")
        new_status = kwargs.get("status")
        reviewed_by = kwargs.get("reviewed_by")
        for req in data.get('access_requests', []):
            if req.get('request_id') == request_id:
                req['status'] = new_status
                req['reviewed_by'] = reviewed_by
                req['decision_at'] = NOW.strftime(DT_STR_FORMAT)
                return json.dumps(req)
        return json.dumps({"error": "Access request not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "update_access_request_status",
                        "description": "Updates the status of an access request.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "request_id": {"type": "string"},
                                        "status": {"type": "string"},
                                        "reviewed_by": {"type": "string"}
                                },
                                "required": ["request_id", "status", "reviewed_by"]
                        }
                }
        }


class CreateSiemAlert(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        alerts = data.get('siem_alerts', [])
        new_id_num = max((int(a['alert_id'][5:]) for a in alerts), default=0) + 1
        new_alert_id = f"ALRT-{new_id_num:03d}"
        new_alert = {
                "alert_id": new_alert_id,
                "user_id": kwargs.get("user_id"),
                "resource_id": kwargs.get("resource_id"),
                "alert_type": kwargs.get("alert_type"),
                "severity": kwargs.get("severity"),
                "timestamp": NOW.strftime(DT_STR_FORMAT)
        }
        alerts.append(new_alert)
        data['siem_alerts'] = alerts
        return json.dumps(new_alert)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "create_siem_alert",
                        "description": "Creates a new SIEM alert.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "user_id": {"type": "string"},
                                        "resource_id": {"type": "string"},
                                        "alert_type": {"type": "string"},
                                        "severity": {"type": "string"}
                                },
                                "required": ["user_id", "resource_id", "alert_type", "severity"]
                        }
                }
        }


class UpdatePolicyExceptionStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        exception_id = kwargs.get("exception_id")
        new_status = kwargs.get("status")
        for ex in data.get('policy_exceptions', []):
            if ex.get('exception_id') == exception_id:
                ex['status'] = new_status
                return json.dumps(ex)
        return json.dumps({"error": "Policy exception not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "update_policy_exception_status",
                        "description": "Updates the status of a policy exception (e.g., ACTIVE, EXPIRED).",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "exception_id": {"type": "string"},
                                        "status": {"type": "string"}
                                },
                                "required": ["exception_id", "status"]
                        }
                }
        }


class UpdateUserDepartment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        new_department = kwargs.get("department")
        for user in data.get('users', []):
            if user.get('user_id') == user_id:
                user['department'] = new_department
                return json.dumps(user)
        return json.dumps({"error": "User not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "update_user_department",
                        "description": "Updates the department for a specific user.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "user_id": {"type": "string"},
                                        "department": {"type": "string"}
                                },
                                "required": ["user_id", "department"]
                        }
                }
        }


class UpdateUserMfaStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        mfa_enabled = kwargs.get("mfa_enabled")
        for user in data.get('users', []):
            if user.get('user_id') == user_id:
                user['mfa_enabled'] = mfa_enabled
                return json.dumps(user)
        return json.dumps({"error": "User not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "update_user_mfa_status",
                        "description": "Enables or disables multi-factor authentication for a user.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "user_id": {"type": "string"},
                                        "mfa_enabled": {"type": "boolean"}
                                },
                                "required": ["user_id", "mfa_enabled"]
                        }
                }
        }


class ApprovePolicyException(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        exception_id = kwargs.get("exception_id")
        reviewed_by = kwargs.get("reviewed_by")
        for ex in data.get('policy_exceptions', []):
            if ex.get('exception_id') == exception_id:
                ex['status'] = 'ACTIVE'
                ex['reviewed_by'] = reviewed_by
                ex['reviewed_on'] = NOW.strftime(DT_STR_FORMAT)
                return json.dumps(ex)
        return json.dumps({"error": "Policy exception not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "approve_policy_exception",
                        "description": "Approves a pending policy exception.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "exception_id": {"type": "string"},
                                        "reviewed_by": {"type": "string"}
                                },
                                "required": ["exception_id", "reviewed_by"]
                        }
                }
        }


class UpdateResourceOwner(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        resource_id = kwargs.get("resource_id")
        new_owner_id = kwargs.get("new_owner_id")
        for res in data.get('resources', []):
            if res.get('resource_id') == resource_id:
                res['owner_id'] = new_owner_id
                return json.dumps(res)
        return json.dumps({"error": "Resource not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "update_resource_owner",
                        "description": "Updates the owner of a resource.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "resource_id": {"type": "string"},
                                        "new_owner_id": {"type": "string"}
                                },
                                "required": ["resource_id", "new_owner_id"]
                        }
                }
        }


class CreateRoleWithPermission(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        permissions = data.get('permissions', [])
        roles = data.get('roles', [])
        role_permissions = data.get('role_permissions', [])

        new_perm_id_num = max((int(p['permission_id'][2:]) for p in permissions), default=0) + 1
        new_perm_id = f"P-{new_perm_id_num:03d}"
        new_permission = {
                "permission_id": new_perm_id,
                "action": kwargs.get("permission_name"),
                "resource_id": kwargs.get("resource_id"),
                "description": kwargs.get("permission_description", f"Permission for the '{kwargs.get('role_name')}' role.")
        }
        permissions.append(new_permission)
        data['permissions'] = permissions

        new_role_id_num = max((int(r['role_id'][4:]) for r in roles), default=0) + 1
        new_role_id = f"ROL-{new_role_id_num:03d}"
        new_role = {
                "role_id": new_role_id,
                "role_name": kwargs.get("role_name"),
                "description": kwargs.get("role_description", f"Role with permission '{kwargs.get('permission_name')}'."),
                "is_temporary": False
        }
        roles.append(new_role)
        data['roles'] = roles

        new_assignment = {
                "role_id": new_role_id,
                "permission_id": new_perm_id
        }
        role_permissions.append(new_assignment)
        data['role_permissions'] = role_permissions

        return json.dumps({
                "permission_id": new_perm_id,
                "role_id": new_role_id,
                "status": "success"
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "create_role_with_permission",
                        "description": "Creates a new permission and a new role, then assigns the permission to the role.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "role_name": {
                                                "type": "string",
                                                "description": "The name for the new role (e.g., 'special-report-viewer')."
                                        },
                                        "resource_id": {
                                                "type": "string",
                                                "description": "The ID of the resource the permission applies to."
                                        },
                                        "permission_name": {
                                                "type": "string",
                                                "description": "The name of the action for the new permission (e.g., 'read-special-report')."
                                        },
                                        "permission_description": {
                                                "type": "string",
                                                "description": "An optional description for the new permission."
                                        },
                                        "role_description": {
                                                "type": "string",
                                                "description": "An optional description for the new role."
                                        }
                                },
                                "required": ["permission_name", "role_name", "resource_id"]
                        }
                }
        }


class ListRoles(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        roles = data.get('roles', [])
        return json.dumps({"roles": roles})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "list_roles",
                        "description": "Lists all available roles in the system.",
                        "parameters": {
                                "type": "object",
                                "properties": {},
                                "required": []
                        }
                }
        }


class UpdateHubspotTicketStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ticket_id = kwargs.get("ticket_id")
        new_status = kwargs.get("status")
        for ticket in data.get('hubspot_tickets', []):
            if ticket.get('ticket_id') == ticket_id:
                ticket['status'] = new_status
                ticket['closed_at'] = NOW.strftime(DT_STR_FORMAT)
                return json.dumps(ticket)
        return json.dumps({"error": "Ticket not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "update_hubspot_ticket_status",
                        "description": "Updates the status of a HubSpot ticket (e.g., OPEN, CLOSED).",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "ticket_id": {"type": "string"},
                                        "status": {"type": "string"},
                                        "note": {"type": "string", "description": "An optional note to add when updating the status."}
                                },
                                "required": ["ticket_id", "status"]
                        }
                }
        }


class GetUsersByDepartment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        department_name = kwargs.get("department")
        users_in_dept = [
                user for user in data.get('users', [])
                if user.get('department') == department_name
        ]
        return json.dumps({"users": users_in_dept})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_users_by_department",
                        "description": "Retrieves all users for a given department by the department's name.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "department": {
                                                "type": "string",
                                                "description": "The name of the department to search for (e.g., 'Engineering')."
                                        }
                                },
                                "required": ["department"]
                        }
                }
        }


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

        for role in data.get('roles', []):
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


class UpdateRoleDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role_id = kwargs.get("role_id")
        new_name = kwargs.get("new_name")
        new_description = kwargs.get("new_description")
        for role in data.get('roles', []):
            if role.get('role_id') == role_id:
                if new_name:
                    role['role_name'] = new_name
                if new_description:
                    role['description'] = new_description
                return json.dumps(role)
        return json.dumps({"error": "Role not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "update_role_details",
                        "description": "Updates the name and/or description of an existing role.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "role_id": {"type": "string"},
                                        "new_name": {"type": "string", "description": "The new name for the role."},
                                        "new_description": {"type": "string", "description": "The new description for the role."}
                                },
                                "required": ["role_id"]
                        }
                }
        }

class ListInactiveUsers(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inactive_since_str = kwargs.get("inactive_since")
        inactive_since_dt = datetime.strptime(inactive_since_str, DT_STR_FORMAT)

        active_user_ids = {session['user_id'] for session in data.get('user_sessions', []) if datetime.strptime(session['end_time'], DT_STR_FORMAT) >= inactive_since_dt}

        all_user_ids = {user['user_id'] for user in data.get('users', [])}
        inactive_user_ids = list(all_user_ids - active_user_ids)

        return json.dumps({"inactive_users": inactive_user_ids})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "list_inactive_users",
                        "description": "Lists users who have not had a session since the specified date.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "inactive_since": {"type": "string", "description": "The date in ISO 8601 format (e.g., '2025-05-01T00:00:00Z')."}
                                },
                                "required": ["inactive_since"]
                        }
                }
        }


class TerminateUserSession(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        session_id = kwargs.get("session_id")
        sessions = data.get('user_sessions', [])
        terminated = False
        for session in sessions:
            if session.get('session_id') == session_id:
                session['end_time'] = NOW.strftime(DT_STR_FORMAT)
                session['status'] = 'TERMINATED'
                terminated = True
                break

        if terminated:
            return json.dumps(session)
        return json.dumps({"error": "Session not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "terminate_user_session",
                        "description": "Terminates a user's active session.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "session_id": {"type": "string"}
                                },
                                "required": ["session_id"]
                        }
                }
        }


class UpdateUserDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        new_username = kwargs.get("new_username")
        new_email = kwargs.get("new_email")

        for user in data.get('users', []):
            if user.get('user_id') == user_id:
                if new_username:
                    user['username'] = new_username
                if new_email:
                    user['email'] = new_email
                return json.dumps(user)
        return json.dumps({"error": "User not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "update_user_details",
                        "description": "Updates a user's username and/or email address.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "user_id": {"type": "string"},
                                        "new_username": {"type": "string"},
                                        "new_email": {"type": "string"}
                                },
                                "required": ["user_id"]
                        }
                }
        }

class UpdateHubspotTicketAssignee(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ticket_id = kwargs.get("ticket_id")
        new_assignee_id = kwargs.get("new_assignee_id")
        for ticket in data.get('hubspot_tickets', []):
            if ticket.get('ticket_id') == ticket_id:
                ticket['assignee_id'] = new_assignee_id
                ticket['updated_at'] = NOW.strftime(DT_STR_FORMAT)
                return json.dumps(ticket)
        return json.dumps({"error": "Ticket not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "update_hubspot_ticket_assignee",
                        "description": "Updates the assignee of an existing HubSpot ticket.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "ticket_id": {
                                            "type": "string",
                                            "description": "The ID of the ticket to update."
                                        },
                                        "new_assignee_id": {
                                            "type": "string",
                                            "description": "The user_id of the new assignee."
                                        }
                                },
                                "required": ["ticket_id", "new_assignee_id"]
                        }
                }
        }


class GetHubspotTicketsByRequester(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        requester_id = kwargs.get("requester_id")

        matching_tickets = [
                ticket for ticket in data.get('hubspot_tickets', [])
                if ticket.get('requester_id') == requester_id
        ]

        return json.dumps({"tickets": matching_tickets})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_hubspot_tickets_by_requester",
                        "description": "Retrieves a list of HubSpot tickets based on the requester's user ID.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "requester_id": {
                                                "type": "string",
                                                "description": "The user_id of the person who requested the tickets."
                                        }
                                },
                                "required": ["requester_id"]
                        }
                }
        }

class GetHubspotTicketsByAssignee(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        assignee_id = kwargs.get("assignee_id")

        matching_tickets = [
                ticket for ticket in data.get('hubspot_tickets', [])
                if ticket.get('assignee_id') == assignee_id
        ]

        return json.dumps({"tickets": matching_tickets})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_hubspot_tickets_by_assignee",
                        "description": "Retrieves a list of HubSpot tickets based on the assignee's user ID.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "assignee_id": {
                                                "type": "string",
                                                "description": "The user_id of the person to whom the tickets are assigned."
                                        }
                                },
                                "required": ["assignee_id"]
                        }
                }
        }


class GetResourcesByOwner(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner_id = kwargs.get("owner_id")

        owned_resources = [
                resource for resource in data.get('resources', [])
                if resource.get('owner_id') == owner_id
        ]

        return json.dumps({"resources": owned_resources})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_resources_by_owner",
                        "description": "Retrieves a list of all resources owned by a specific user.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "owner_id": {
                                                "type": "string",
                                                "description": "The user_id of the resource owner."
                                        }
                                },
                                "required": ["owner_id"]
                        }
                }
        }


class GetPermissionDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        permission_id = kwargs.get("permission_id")
        permission_name = kwargs.get("permission_name")

        if not permission_id and not permission_name:
            return json.dumps({"error": "Either permission_id or permission_name must be provided."})

        for permission in data.get('permissions', []):
            if permission_id and permission.get('permission_id') == permission_id:
                return json.dumps(permission)
            if permission_name and permission.get('action') == permission_name:
                return json.dumps(permission)

        return json.dumps({"error": "Permission not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_permission_details",
                        "description": "Retrieves the full details of a permission by its ID or name.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "permission_id": {
                                                "type": "string",
                                                "description": "The ID of the permission to retrieve."
                                        },
                                        "permission_name": {
                                                "type": "string",
                                                "description": "The name (action) of the permission to retrieve."
                                        }
                                }
                        }
                }
        }


class GetSiemAlerts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")

        matching_alerts = [
                alert for alert in data.get('siem_alerts', [])
                if alert.get('user_id') == user_id
        ]

        return json.dumps({"alerts": matching_alerts})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_siem_alerts",
                        "description": "Retrieves a list of SIEM alerts based on the user's ID.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "user_id": {
                                                "type": "string",
                                                "description": "The user_id to retrieve SIEM alerts for."
                                        }
                                },
                                "required": ["user_id"]
                        }
                }
        }


class RemovePermissionFromRole(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role_id = kwargs.get("role_id")
        permission_id = kwargs.get("permission_id")

        if not role_id or not permission_id:
            return json.dumps({"error": "Both role_id and permission_id must be provided."})

        role_permissions = data.get('role_permissions', [])

        initial_len = len(role_permissions)

        updated_permissions = [
                rp for rp in role_permissions
                if not (rp.get('role_id') == role_id and rp.get('permission_id') == permission_id)
        ]

        if len(updated_permissions) < initial_len:
            data['role_permissions'] = updated_permissions
            return json.dumps({"role_id": role_id, "permission_id": permission_id, "status": "removed"})
        else:
            return json.dumps({"error": "Permission not found on the specified role."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "remove_permission_from_role",
                        "description": "Removes a specific permission from a role.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "role_id": {
                                                "type": "string",
                                                "description": "The ID of the role to modify."
                                        },
                                        "permission_id": {
                                                "type": "string",
                                                "description": "The ID of the permission to remove."
                                        }
                                },
                                "required": ["role_id", "permission_id"]
                        }
                }
        }


class RemoveRole(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role_id_to_remove = kwargs.get("role_id")

        if not role_id_to_remove:
            return json.dumps({"error": "role_id must be provided."})

        roles = data.get('roles', [])
        initial_roles_len = len(roles)
        updated_roles = [role for role in roles if role.get('role_id') != role_id_to_remove]

        if len(updated_roles) == initial_roles_len:
            return json.dumps({"error": "Role not found."})

        data['roles'] = updated_roles

        role_permissions = data.get('role_permissions', [])
        updated_role_permissions = [rp for rp in role_permissions if rp.get('role_id') != role_id_to_remove]
        data['role_permissions'] = updated_role_permissions

        user_roles = data.get('user_roles', [])
        updated_user_roles = [ur for ur in user_roles if ur.get('role_id') != role_id_to_remove]
        data['user_roles'] = updated_user_roles

        return json.dumps({"role_id": role_id_to_remove, "status": "removed"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "remove_role",
                        "description": "Deletes a role from the system, including all associated user and permission assignments.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "role_id": {
                                                "type": "string",
                                                "description": "The ID of the role to be removed."
                                        }
                                },
                                "required": ["role_id"]
                        }
                }
        }

class RemovePermission(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        permission_id_to_remove = kwargs.get("permission_id")

        if not permission_id_to_remove:
            return json.dumps({"error": "permission_id must be provided."})

        permissions = data.get('permissions', [])
        initial_permissions_len = len(permissions)
        updated_permissions = [p for p in permissions if p.get('permission_id') != permission_id_to_remove]

        if len(updated_permissions) == initial_permissions_len:
            return json.dumps({"error": "Permission not found."})

        data['permissions'] = updated_permissions

        role_permissions = data.get('role_permissions', [])
        updated_role_permissions = [rp for rp in role_permissions if rp.get('permission_id') != permission_id_to_remove]
        data['role_permissions'] = updated_role_permissions

        return json.dumps({"permission_id": permission_id_to_remove, "status": "removed"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_permission",
                "description": "Deletes a permission from the system, including its assignments to any roles.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "permission_id": {
                            "type": "string",
                            "description": "The ID of the permission to be removed."
                        }
                    },
                    "required": ["permission_id"]
                }
            }
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
