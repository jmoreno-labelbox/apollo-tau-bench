import json
from datetime import datetime, timezone
from typing import Any

from tau_bench.envs.tool import Tool

NOW: datetime = datetime(2025, 8, 9, 10, 00, 00, tzinfo=timezone.utc)




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


class GetCurrentTime(Tool):
    """Provides a static current date and time formatted as "YYYY-MM-DD HH:MM:SS+00:00". For example, "2025-08-09 10:00:00+00:00"""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        # Format the date and time in the format "YYYY-MM-DD HH:MM:SS+00:00"
        formatted_time = NOW.isoformat(timespec="seconds").replace("T", " ")
        payload = {"current_time": formatted_time}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCurrentTime",
                "description": "Returns the current date and time as YYYY-MM-DD HH:MM:SS+00:00",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class CreateUser(Tool):
    """Generates a new user in the user.json file with proper formatting and default settings."""

    @staticmethod
    def invoke(data: dict[str, Any], username: str = None, email: str = None, department: str = None, status: str = "ACTIVE",
    actor_id: Any = None,
    ) -> str:
        try:
            users = data.get("users", {}).values()
        except (KeyError, json.JSONDecodeError):
            users = []
        existing_ids = [
            int(item["user_id"].replace("U-", ""))
            for item in users.values() if item["user_id"].startswith("U-")
        ]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        user_id = f"U-{next_id_num:03d}"

        new_user = {
            "user_id": user_id,
            "username": username,
            "email": email,
            "department": department,
            "status": status,
            "mfa_enabled": False,
        }
        data["users"][user_id] = new_user
        data["users.json"] = json.dumps(users)
        payload = new_user
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateUser",
                "description": "Creates a new user entry in the database.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {
                            "type": "string",
                            "description": "The username of the new user.",
                        },
                        "email": {
                            "type": "string",
                            "description": "The email address of the new user.",
                        },
                        "department": {
                            "type": "string",
                            "description": "The department where the new user belongs.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The status of the new user (e.g., ACTIVE, INACTIVE).",
                        },
                    },
                    "required": ["username", "email", "department", "status"],
                },
            },
        }


class GetUserDetailsById(Tool):
    """Fetches complete details of a user by their unique user_id."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, actor_id: Any = None) -> str:
        try:
            users = data.get("users", {}).values()
        except (KeyError, json.JSONDecodeError):
            users = []

        for user in users.values():
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
                "name": "GetUserDetailsById",
                "description": "Retrieves full user details based on their unique user_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user (e.g., U-001).",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }


class GetUserDetailsByUsername(Tool):
    """Obtains a user's complete details via their username."""

    @staticmethod
    def invoke(data: dict[str, Any], username: str = None) -> str:
        try:
            users = data.get("users", {}).values()
        except (KeyError, json.JSONDecodeError):
            users = []

        for user in users.values():
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
                "name": "GetUserDetailsByUsername",
                "description": "Retrieves full user details based on their username.",
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


class GetUserDetailsByEmail(Tool):
    """Acquires a user's full details using their email address."""

    @staticmethod
    def invoke(data: dict[str, Any], email: str = None) -> str:
        try:
            users = data.get("users", {}).values()
        except (KeyError, json.JSONDecodeError):
            users = []

        for user in users.values():
            if user.get("email") == email:
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
                "name": "GetUserDetailsByEmail",
                "description": "Retrieves full user details based on their email address.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email": {
                            "type": "string",
                            "description": "The email address to search for.",
                        }
                    },
                    "required": ["email"],
                },
            },
        }


class GetRoleIdByName(Tool):
    """
    Locates one or more roles by searching for a name, giving priority to exact matches
    while also returning other roles that include the search term.
    """

    @staticmethod
    def invoke(data: dict[str, Any], role_name: str = None) -> str:
        find_role_name = role_name
        try:
            roles = data.get("roles", {}).values()
        except (KeyError, json.JSONDecodeError):
            roles = []

        exact_matches = []
        partial_matches = []

        for role in roles.values():
            current_role_name = role.get("role_name", "")

            if current_role_name == find_role_name:
                exact_matches.append(role)
            elif find_role_name in current_role_name:
                partial_matches.append(role)

        all_matches = exact_matches + partial_matches

        if not all_matches:
            payload = {"error": f"No roles found matching or containing '{find_role_name}'."}
            out = json.dumps(payload)
            return out
        payload = all_matches
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRoleIdByName",
                "description": "Retrieves a list of roles based on a name. Returns all roles that either exactly match the name or contain the name as a substring.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_name": {
                            "type": "string",
                            "description": "The name of the role to search for (e.g., 'sales-lead').",
                        }
                    },
                    "required": ["role_name"],
                },
            },
        }


class CreateAccessRequest(Tool):
    """Initiates a new access request for a user to obtain a particular role for a resource."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str = None,
        resource_id: str = None,
        role_id: str = None,
        justification: str = None,
        timestamp: str = None
    ) -> str:
        try:
            requests = data.get("access_requests", {}).values()
        except (KeyError, json.JSONDecodeError):
            requests = []

        existing_ids = [
            int(r["request_id"].replace("AR-", ""))
            for r in requests.values() if r.get("request_id", "").startswith("AR-")
        ]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        request_id = f"AR-{next_id_num:03d}"

        new_request = {
            "request_id": request_id,
            "user_id": user_id,
            "resource_id": resource_id,
            "requested_role_id": role_id,
            "justification": justification,
            "status": "PENDING",
            "submitted_at": timestamp,
            "reviewed_by": None,
            "decision_at": None,
        }

        data["access_requests"][new_request["access_request_id"]] = new_request
        data["access_requests.json"] = json.dumps(requests, indent=4)
        payload = new_request
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAccessRequest",
                "description": "Submits a request for a user to be granted a role. Requires subsequent approval.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user who will receive the role.",
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "The ID of the resource the role applies to.",
                        },
                        "role_id": {
                            "type": "string",
                            "description": "The ID of the requested role.",
                        },
                        "justification": {
                            "type": "string",
                            "description": "A brief reason for the request.",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp for when the request is submitted.",
                        },
                    },
                    "required": ["user_id", "resource_id", "role_id", "justification"],
                },
            },
        }


class AssignRoleToUser(Tool):
    """Assigning a role directly to a user."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str = None,
        role_id: str = None,
        assigned_by: str = None,
        expires_on: str = None
,
    assigned_on: Any = None,
    ) -> str:
        try:
            user_roles = data.get("user_roles", {}).values()
        except (KeyError, json.JSONDecodeError):
            user_roles = []
        existing_ids = [
            int(ur["user_role_id"].replace("UR-", ""))
            for ur in user_roles.values() if ur.get("user_role_id", "").startswith("UR-")
        ]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        user_role_id = f"UR-{next_id_num:03d}"

        new_assignment = {
            "user_role_id": user_role_id,
            "user_id": user_id,
            "role_id": role_id,
            "assigned_by": assigned_by,
            "expires_on": expires_on,
        }

        user_data["roles"][role_id] = new_assignment
        data["user_roles.json"] = json.dumps(user_roles, indent=4)
        payload = new_assignment
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignRoleToUser",
                "description": "Directly assigns a specific role to a user. This is a privileged action for processes like onboarding.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user to whom the role will be assigned.",
                        },
                        "role_id": {
                            "type": "string",
                            "description": "The unique ID of the role to be assigned.",
                        },
                        "assigned_by": {
                            "type": "string",
                            "description": "The user ID of the administrator or manager performing the assignment.",
                        },
                        "expires_on": {
                            "type": "string",
                            "description": "Optional: The timestamp when the role assignment expires. Use null for permanent roles.",
                        },
                    },
                    "required": ["user_id", "role_id", "assigned_by"],
                },
            },
        }


class LogAuditEvent(Tool):
    """Logging actions or events in the system's audit log for security, compliance, and traceability purposes."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        actor_id: str = None,
        action_type: str = None,
        target_id: str = None,
        timestamp: str = None,
        details: str = None
    ) -> str:
        try:
            audit_logs = data.get("audit_logs", {}).values()
        except (KeyError, json.JSONDecodeError):
            audit_logs = []
        existing_ids = [
            int(log["log_id"].replace("L-", ""))
            for log in audit_logs.values() if log.get("log_id", "").startswith("L-")
        ]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        log_id = f"L-{next_id_num:03d}"

        new_log = {
            "log_id": log_id,
            "actor_id": actor_id,
            "action_type": action_type,
            "target_id": target_id,
            "timestamp": timestamp,
            "details": details,
        }

        data["audit_logs"][new_log["audit_log_id"]] = new_log
        data["audit_logs.json"] = json.dumps(audit_logs, indent=4)
        payload = {"message": "Audit event logged successfully.", "log_details": new_log}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogAuditEvent",
                "description": "Records an action in the system's audit log for compliance and tracking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "actor_id": {
                            "type": "string",
                            "description": "The user ID of the user who performed the action.",
                        },
                        "action_type": {
                            "type": "string",
                            "description": "The type of action being logged (e.g., USER_CREATED, ROLE_ASSIGNED, ACCESS_GRANTED).",
                        },
                        "target_id": {
                            "type": "string",
                            "description": "The ID of the entity that was the target of the action (e.g., a user_id, role_id, or request_id).",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The timestamp of the event, in ISO 8601 format.",
                        },
                        "details": {
                            "type": "string",
                            "description": "A human-readable summary of the event.",
                        },
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


class SendEmail(Tool):
    """A utility for sending an email by generating a record in the database."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        sender: str = None,
        receiver: str = None,
        subject: str = None,
        text_content: str = None,
        timestamp: str = None
    ) -> str:
        try:
            emails = data.get("emails", {}).values()
        except (KeyError, json.JSONDecodeError):
            emails = []
        existing_ids = [
            int(email["email_id"].replace("EM-", ""))
            for email in emails.values() if email.get("email_id", "").startswith("EM-")
        ]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        email_id = f"EM-{next_id_num:03d}"

        new_email = {
            "email_id": email_id,
            "sender": sender,
            "receiver": receiver,
            "subject": subject,
            "text_content": text_content,
            "timestamp": timestamp,
        }

        data["emails"][email_id] = new_email
        data["emails.json"] = json.dumps(emails, indent=4)
        payload = new_email
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendEmail",
                "description": "Sends a standard onboarding email by creating a record of it in the database.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sender": {
                            "type": "string",
                            "description": "The email address of the sender (e.g., onboarding@taucorp.com).",
                        },
                        "receiver": {
                            "type": "string",
                            "description": "The email address of the recipient.",
                        },
                        "subject": {
                            "type": "string",
                            "description": "The subject line of the email.",
                        },
                        "text_content": {
                            "type": "string",
                            "description": "The plain text body of the email.",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The timestamp of when the email is sent, in ISO 8601 format.",
                        },
                    },
                    "required": [
                        "sender",
                        "receiver",
                        "subject",
                        "text_content",
                        "timestamp",
                    ],
                },
            },
        }


class UpdateUserStatus(Tool):
    """Modifying the 'status' field for a particular user in the database."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, new_status: str = None,
    updated_by: Any = None,
    ) -> str:
        user_id_to_update = user_id
        new_status = new_status

        try:
            users = data.get("users", {}).values()
        except:
            users = []

        user_to_update = None
        for user in users.values():
            if user.get("user_id") == user_id_to_update:
                user["status"] = new_status
                user_to_update = user
                break

        if not user_to_update:
            payload = {"error": f"User with ID '{user_id_to_update}' not found."}
            out = json.dumps(payload)
            return out

        data["users"] = users
        payload = user_to_update
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateUserStatus",
                "description": "Updates the status of a user account (e.g., to ACTIVE, DISABLED, SUSPENDED).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user whose status needs to be updated.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status to set for the user. Must be one of: ACTIVE, INACTIVE, SUSPENDED, DISABLED.",
                        },
                    },
                    "required": ["user_id", "new_status"],
                },
            },
        }


class GetUserRolesByUserId(Tool):
    """Fetches all role assignments associated with a specific user ID."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        try:
            user_roles = data.get("user_roles", {}).values()
        except:
            user_roles = []

        assigned_roles = [role for role in user_roles.values() if role.get("user_id") == user_id]
        payload = assigned_roles
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserRolesByUserId",
                "description": "Lists all roles currently assigned to a specific user ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user whose roles are to be listed.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }


class RevokeRoleFromUser(Tool):
    """Removes a specific role from a user by eliminating the user-role record from the database."""

    @staticmethod
    def invoke(data: dict[str, Any], user_role_id: str = None) -> str:
        try:
            user_roles = data.get("user_roles", {}).values()
        except:
            user_roles = []

        index = -1
        for i, assignment in enumerate(user_roles.values()):
            if assignment.get("user_role_id") == user_role_id:
                index = i
                break

        if index != -1:
            revoked_assignment = user_roles.pop(index)
        else:
            payload = {"error": f"User-role with ID '{user_role_id}' not found."}
            out = json.dumps(payload)
            return out

        data["user_roles"] = user_roles
        payload = {
            "message": "User-role assignment revoked successfully.",
            "revoked_details": revoked_assignment,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RevokeRoleFromUser",
                "description": "Revokes a specific role from a user by deleting the assignment record. Requires the user_role_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_role_id": {
                            "type": "string",
                            "description": "The unique ID of the user-role assignment to be revoked (e.g., 'UR-003').",
                        }
                    },
                    "required": ["user_role_id"],
                },
            },
        }


class GetAccessRequestById(Tool):
    """Retrieve complete details of a specific access request by its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], request_id: str = None) -> str:
        try:
            access_requests = data.get("access_requests", {}).values()
        except:
            access_requests = []

        for request in access_requests.values():
            if request.get("request_id") == request_id:
                payload = request
                out = json.dumps(payload)
                return out
        payload = {"error": f"Access request with ID '{request_id}' not found."}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAccessRequestById",
                "description": "Retrieves the full details of a specific access request using its unique ID (e.g., 'AR-007').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {
                            "type": "string",
                            "description": "The unique ID of the access request to retrieve.",
                        }
                    },
                    "required": ["request_id"],
                },
            },
        }


class GetResourceDetailsById(Tool):
    """Obtain the complete details of a specific resource by its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], resource_id: str = None) -> str:
        try:
            resources = data.get("resources", {}).values()
        except:
            resources = []

        for resource in resources.values():
            if resource.get("resource_id") == resource_id:
                payload = resource
                out = json.dumps(payload)
                return out
        payload = {"error": f"Resource with ID '{resource_id}' not found."}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetResourceDetailsById",
                "description": "Retrieves the full details of a specific resource (e.g., its criticality) using its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {
                            "type": "string",
                            "description": "The unique ID of the resource to retrieve (e.g., 'RES-025').",
                        }
                    },
                    "required": ["resource_id"],
                },
            },
        }


class ApproveAccessRequest(Tool):
    """Authorize access requests, updating their status from 'PENDING' to 'APPROVED', and establish the necessary user-role assignment to provide access."""

    @staticmethod
    def invoke(data: dict[str, Any], request_id: str = None, reviewer_id: str = None, timestamp: str = None, expires_on: str = None) -> str:
        try:
            access_requests = data.get("access_requests", {}).values()
            user_roles = data.get("user_roles", {}).values()
        except Exception as e:
            payload = {"error": f"Failed to load data lists: {e}"}
            out = json.dumps(payload)
            return out

        request = None
        for req in access_requests.values():
            if req.get("request_id") == request_id and req.get("status") == "PENDING":
                request = req
                break

        if not request:
            payload = {"error": f"Pending access request with ID '{request_id}' not found."}
            out = json.dumps(payload)
            return out

        request["status"] = "APPROVED"
        request["reviewed_by"] = reviewer_id
        request["decision_at"] = timestamp

        ur_existing_ids = [
            int(ur["user_role_id"].replace("UR-", ""))
            for ur in user_roles.values() if ur.get("user_role_id", "").startswith("UR-")
        ]
        next_ur_id = max(ur_existing_ids) + 1 if ur_existing_ids else 1

        new_role_assignment = {
            "user_role_id": f"UR-{next_ur_id:03d}",
            "user_id": request["user_id"],
            "role_id": request["requested_role_id"],
            "assigned_by": reviewer_id,
            "assigned_on": timestamp,
            "expires_on": expires_on,
        }
        user_data["roles"][role_id] = new_role_assignment

        data["access_requests"] = access_requests
        data["user_roles"] = user_roles
        payload = {
            "message": "Access request approved and role granted successfully.",
            "request_id": request_id,
            "new_assignment_id": new_role_assignment["user_role_id"],
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApproveAccessRequest",
                "description": "Approves a pending access request. This updates the request status and grants the specified role to the user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {
                            "type": "string",
                            "description": "The unique ID of the access request to approve.",
                        },
                        "reviewer_id": {
                            "type": "string",
                            "description": "The user ID of the person approving the request.",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp of the approval decision.",
                        },
                        "expires_on": {
                            "type": "string",
                            "description": "Optional: The timestamp when the role assignment expires. Use null for permanent roles.",
                        },
                    },
                    "required": ["request_id", "reviewer_id", "timestamp"],
                },
            },
        }


class GetSiemAlertById(Tool):
    """Retrieve complete details of a specific SIEM alert by its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], alert_id: str = None) -> str:
        try:
            siem_alerts = data.get("siem_alerts", {}).values()
        except:
            siem_alerts = []

        for alert in siem_alerts.values():
            if alert.get("alert_id") == alert_id:
                payload = alert
                out = json.dumps(payload)
                return out
        payload = {"error": f"SIEM alert with ID '{alert_id}' not found."}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSiemAlertById",
                "description": "Retrieves the full details of a specific SIEM alert using its unique ID (e.g., 'ALRT-012').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "alert_id": {
                            "type": "string",
                            "description": "The unique ID of the SIEM alert to retrieve.",
                        }
                    },
                    "required": ["alert_id"],
                },
            },
        }


class GetCertificationDetailsById(Tool):
    """Obtain the complete details of a specific access certification campaign by its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], certification_id: str = None,
    user_id: Any = None,
    ) -> str:
        try:
            certifications = data.get("certifications", {}).values()
        except:
            certifications = []

        for cert in certifications.values():
            if cert.get("certification_id") == certification_id:
                payload = cert
                out = json.dumps(payload)
                return out
        payload = {"error": f"Certification with ID '{certification_id}' not found."}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCertificationDetailsById",
                "description": "Retrieves the full details of a specific access certification campaign using its unique ID (e.g., 'C-005').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {
                            "type": "string",
                            "description": "The unique ID of the certification campaign to retrieve.",
                        }
                    },
                    "required": ["certification_id"],
                },
            },
        }


class FindUsersWithRole(Tool):
    """Identify all users currently assigned to a specific role."""

    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None) -> str:
        try:
            all_user_roles = data.get("user_roles", {}).values()
        except:
            all_user_roles = []

        users_with_role = [
            assignment["user_id"]
            for assignment in all_user_roles.values() if assignment.get("role_id") == role_id
        ]
        unique_user_ids = list(set(users_with_role))
        payload = unique_user_ids
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindUsersWithRole",
                "description": "Finds and returns a list of all user IDs that are currently assigned a specific role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "string",
                            "description": "The unique ID of the role to search for (e.g., 'ROL-013').",
                        }
                    },
                    "required": ["role_id"],
                },
            },
        }


class UpdateCertificationStatus(Tool):
    """Modify the status of an access certification campaign."""

    @staticmethod
    def invoke(data: dict[str, Any], certification_id: str = None, new_status: str = None, timestamp: str = None) -> str:
        certification_id_to_update = certification_id
        new_status = new_status
        timestamp = timestamp
        try:
            certifications = data.get("certifications", {}).values()
        except:
            certifications = []

        certification_found = False
        updated_certification = None
        for cert in certifications.values():
            if cert.get("certification_id") == certification_id_to_update:
                cert["status"] = new_status
                if new_status == "COMPLETED":
                    cert["completed_on"] = timestamp

                certification_found = True
                updated_certification = cert
                break

        if not certification_found:
            payload = {
                "error": f"Certification with ID '{certification_id_to_update}' not found."
            }
            out = json.dumps(payload)
            return out

        data["certifications"] = certifications
        payload = {
            "message": "Certification campaign status updated successfully.",
            "certification_details": updated_certification,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCertificationStatus",
                "description": "Updates the status of an access certification campaign (e.g., to 'COMPLETED').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {
                            "type": "string",
                            "description": "The unique ID of the certification campaign to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status to set for the campaign (e.g., 'COMPLETED').",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp to record as the completion time.",
                        },
                    },
                    "required": ["certification_id", "new_status", "timestamp"],
                },
            },
        }


class CreatePolicyException(Tool):
    """Establish a new policy exception to provide emergency access based on a particular permission."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        timestamp: str = None,
        user_id: str = None,
        permission_id: str = None,
        approved_by: str = None,
        expires_at: str = None,
        justification: str = None
    ) -> str:
        try:
            policy_exceptions = data.get("policy_exceptions", {}).values()
        except:
            policy_exceptions = []

        existing_ids = [
            int(item["exception_id"].replace("PE-", ""))
            for item in policy_exceptions.values() if item.get("exception_id", "").startswith("PE-")
        ]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        exception_id = f"PE-{next_id_num:03d}"

        new_exception = {
            "exception_id": exception_id,
            "user_id": user_id,
            "permission_id": permission_id,
            "reviewed_by": approved_by,
            "requested_on": timestamp,
            "reviewed_on": timestamp,
            "expires_on": expires_at,
            "reason": justification,
            "status": "ACTIVE",
        }

        data["policy_exceptions"][new_exception["policy_exception_id"]] = new_exception
        data["policy_exceptions"] = policy_exceptions
        payload = {
            "message": "Policy exception created successfully.",
            "exception_details": new_exception,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreatePolicyException",
                "description": "Creates a policy exception to grant temporary, emergency access for a specific permission.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user receiving the exception.",
                        },
                        "permission_id": {
                            "type": "string",
                            "description": "The ID of the specific permission being granted.",
                        },
                        "justification": {
                            "type": "string",
                            "description": "The business reason for the emergency exception.",
                        },
                        "approved_by": {
                            "type": "string",
                            "description": "The ID of the manager approving the exception.",
                        },
                        "expires_at": {
                            "type": "string",
                            "description": "The timestamp when this exception will automatically expire.",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp for the creation and review record.",
                        },
                    },
                    "required": [
                        "user_id",
                        "permission_id",
                        "justification",
                        "approved_by",
                        "expires_at",
                        "timestamp",
                    ],
                },
            },
        }


class CreateHubspotTicket(Tool):
    """Generate a new ticket in the HubSpot system for monitoring purposes."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        timestamp: str = None,
        subject: str = None,
        description: str = None,
        priority: str = None,
        assignee_id: str = None,
        requester_id: str = None,
        category: str = None
    ) -> str:
        try:
            hubspot_tickets = data.get("hubspot_tickets", {}).values()
        except:
            hubspot_tickets = []

        existing_ids = [
            int(item["ticket_id"].replace("TI-", ""))
            for item in hubspot_tickets.values() if item.get("ticket_id", "").startswith("TI-")
        ]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        ticket_id = f"TI-{next_id_num:03d}"

        new_ticket = {
            "ticket_id": ticket_id,
            "created_at": timestamp,
            "updated_at": timestamp,
            "subject": subject,
            "description": description,
            "status": "OPEN",
            "priority": priority,
            "assignee_id": assignee_id,
            "requester_id": requester_id,
            "category": category,
            "closed_at": None,
        }

        hubspot_data["tickets"][ticket_id] = new_ticket
        data["hubspot_tickets"] = hubspot_tickets
        payload = {
            "message": "HubSpot ticket created successfully.",
            "ticket_details": new_ticket,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateHubspotTicket",
                "description": "Creates a new ticket in the HubSpot system to track an incident or request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject": {
                            "type": "string",
                            "description": "The title or subject line of the ticket.",
                        },
                        "description": {
                            "type": "string",
                            "description": "A detailed description of the issue or event.",
                        },
                        "priority": {
                            "type": "string",
                            "description": "The priority level of the ticket (e.g., HIGH, MEDIUM, LOW).",
                        },
                        "assignee_id": {
                            "type": "string",
                            "description": "The user ID of the person the ticket is assigned to.",
                        },
                        "requester_id": {
                            "type": "string",
                            "description": "The user ID of the person who initiated the event or request.",
                        },
                        "category": {
                            "type": "string",
                            "description": "The category of the ticket (e.g., SECURITY_INCIDENT, ACCESS_REQUEST).",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp for the creation record.",
                        },
                    },
                    "required": [
                        "subject",
                        "description",
                        "priority",
                        "assignee_id",
                        "requester_id",
                        "category",
                        "timestamp",
                    ],
                },
            },
        }


class GetPermissionByName(Tool):
    """
    Locate a specific permission by its action name, with the option to filter by a resource ID.
    If resource_id is not provided, it will return the first permission that matches the name.
    """

    @staticmethod
    def invoke(data: dict[str, Any], permission_name: str = None, resource_id: str = None) -> str:
        try:
            permissions = data.get("permissions", {}).values()
        except (KeyError, json.JSONDecodeError):
            permissions = []

        for perm in permissions.values():
            if perm.get("action") == permission_name:
                if resource_id and perm.get("resource_id") != resource_id:
                    continue
                payload = perm
                out = json.dumps(payload)
                return out

        error_message = f"Permission '{permission_name}' not found."
        if resource_id:
            error_message += f" on resource '{resource_id}'"
        payload = {"error": error_message}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPermissionByName",
                "description": "Retrieves the details of a specific permission by its action name (e.g., 'admin-db-cluster'). Can be optionally filtered by the resource it applies to.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "permission_name": {
                            "type": "string",
                            "description": "The name of the action the permission allows (e.g., 'read-repo', 'admin-db-cluster').",
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "Optional. The ID of the resource to filter by (e.g., 'RES-025').",
                        },
                    },
                    "required": ["permission_name"],
                },
            },
        }


class ListUserSessions(Tool):
    """Identify all recent login sessions associated with a specific user."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        user_id_to_find = user_id
        try:
            all_sessions = data.get("sessions", {}).values()
        except:
            all_sessions = []

        user_sessions = [
            session
            for session in all_sessions.values() if session.get("user_id") == user_id_to_find
        ]
        payload = user_sessions
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListUserSessions",
                "description": "Retrieves a list of all recent login sessions for a specific user by their user ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user whose sessions are to be retrieved.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }


class RejectAccessRequest(Tool):
    """Deny an access request and document the reason."""

    @staticmethod
    def invoke(data: dict[str, Any], request_id: str = None, reviewer_id: str = None, timestamp: str = None, rejection_reason: str = None,
    reason: Any = None,
    ) -> str:
        request_id_to_find = request_id

        try:
            access_requests = data.get("access_requests", {}).values()
        except:
            access_requests = []

        request_found = False
        for request in access_requests.values():
            if request.get("request_id") == request_id_to_find:
                request["status"] = "REJECTED"
                request["reviewed_by"] = reviewer_id
                request["decision_at"] = timestamp
                request["rejection_reason"] = rejection_reason
                request_found = True
                break

        if not request_found:
            payload = {"error": f"Access request with ID '{request_id_to_find}' not found."}
            out = json.dumps(payload)
            return out

        data["access_requests"] = access_requests
        payload = {
            "message": "Access request rejected successfully.",
            "request_id": request_id_to_find,
            "new_status": "REJECTED",
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RejectAccessRequest",
                "description": "Rejects a pending access request and records the reason for the rejection.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {
                            "type": "string",
                            "description": "The unique ID of the access request to be rejected.",
                        },
                        "reviewer_id": {
                            "type": "string",
                            "description": "The user ID of the manager who is rejecting the request.",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp for the decision record.",
                        },
                        "rejection_reason": {
                            "type": "string",
                            "description": "A brief, clear reason for why the request is being rejected.",
                        },
                    },
                    "required": [
                        "request_id",
                        "reviewer_id",
                        "timestamp",
                        "rejection_reason",
                    ],
                },
            },
        }


class GetResourceByName(Tool):
    """Locate a resource by its user-friendly name."""

    @staticmethod
    def invoke(data: dict[str, Any], resource_name: str = None) -> str:
        resource_name_to_find = resource_name
        try:
            all_resources = data.get("resources", {}).values()
        except:
            all_resources = []

        for resource in all_resources.values():
            if resource.get("name") == resource_name_to_find:
                payload = resource
                out = json.dumps(payload)
                return out
        payload = {"error": f"Resource with name '{resource_name_to_find}' not found."}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetResourceByName",
                "description": "Retrieves the full details of a resource by searching for its exact name (e.g., 'Sales Reporting Dashboard').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_name": {
                            "type": "string",
                            "description": "The unique, human-readable name of the resource.",
                        }
                    },
                    "required": ["resource_name"],
                },
            },
        }


class CreateSiemAlert(Tool):
    """Create a new SIEM alert manually based on an investigation."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        timestamp: str = None,
        user_id: str = None,
        resource_id: str = None,
        alert_type: str = None,
        severity: str = None
    ) -> str:
        try:
            siem_alerts = data.get("siem_alerts", {}).values()
        except:
            siem_alerts = []

        existing_ids = [
            int(item["alert_id"].replace("ALRT-", ""))
            for item in siem_alerts.values() if item.get("alert_id", "").startswith("ALRT-")
        ]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        alert_id = f"ALRT-{next_id_num:03d}"

        new_alert = {
            "alert_id": alert_id,
            "timestamp": timestamp,
            "user_id": user_id,
            "resource_id": resource_id,
            "alert_type": alert_type,
            "severity": severity,
        }

        data["siem_alerts"][new_alert["siem_alert_id"]] = new_alert
        data["siem_alerts"] = siem_alerts
        payload = {"message": "SIEM alert created successfully.", "alert_details": new_alert}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateSiemAlert",
                "description": "Manually creates a new SIEM (Security Information and Event Management) alert to formally track a discovered security incident.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user associated with the security event.",
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "The ID of the resource that was targeted.",
                        },
                        "alert_type": {
                            "type": "string",
                            "description": "The type of alert (e.g., 'POTENTIAL_DATA_EXFILTRATION', 'UNAUTHORIZED_ACCESS_ATTEMPT').",
                        },
                        "severity": {
                            "type": "string",
                            "description": "The severity of the alert (e.g., 'CRITICAL', 'HIGH', 'MEDIUM', 'LOW').",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp to record as the alert creation time.",
                        },
                    },
                    "required": [
                        "user_id",
                        "resource_id",
                        "alert_type",
                        "severity",
                        "timestamp",
                    ],
                },
            },
        }


class GetSlackMessageById(Tool):
    """Fetch the details of a specific Slack message by its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], message_id: str = None) -> str:
        message_id_to_find = message_id
        try:
            slack_messages = data.get("slack_messages", {}).values()
        except:
            slack_messages = []

        for message in slack_messages.values():
            if message.get("message_id") == message_id_to_find:
                payload = message
                out = json.dumps(payload)
                return out
        payload = {"error": f"Slack message with ID '{message_id_to_find}' not found."}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSlackMessageById",
                "description": "Retrieves the full details of a Slack message, including its content and channel, by its unique ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message_id": {
                            "type": "string",
                            "description": "The unique ID of the Slack message (e.g., 'SL-007').",
                        }
                    },
                    "required": ["message_id"],
                },
            },
        }


class FindAccessRequestByDetails(Tool):
    """Locate an access request by examining its content details."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, role_id: str = None, resource_id: str = None) -> str:
        try:
            access_requests = data.get("access_requests", {}).values()
        except:
            access_requests = []

        for request in access_requests.values():
            if (
                request.get("user_id") == user_id
                and request.get("requested_role_id") == role_id
                and request.get("resource_id") == resource_id
            ):
                payload = request
                out = json.dumps(payload)
                return out
        payload = {"error": "No matching access request found for the provided details."}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindAccessRequestByDetails",
                "description": "Finds a specific access request by searching for a combination of the user who requested it, the role they requested, and the resource they requested it for.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user ID of the requester.",
                        },
                        "role_id": {
                            "type": "string",
                            "description": "The role ID that was requested.",
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "The resource ID that was requested.",
                        },
                    },
                    "required": ["user_id", "role_id", "resource_id"],
                },
            },
        }


class SendSlackMessage(Tool):
    """Dispatch a message to a Slack channel."""

    @staticmethod
    def invoke(data: dict[str, Any], timestamp: str = None, message: str = None, channel: str = None, reply_to_message_id: str = None,
    thread_id: Any = None,
    ) -> str:
        try:
            slack_messages = data.get("slack_messages", {}).values()
        except:
            slack_messages = []

        existing_ids = [
            int(item["message_id"].replace("SL-", ""))
            for item in slack_messages.values() if item.get("message_id", "").startswith("SL-")
        ]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        message_id = f"SL-{next_id_num:03d}"

        new_message = {
            "message_id": message_id,
            "timestamp": timestamp,
            "username": "RBAC_BOT",
            "message": message,
            "channel": channel,
            "reply_to_message_id": reply_to_message_id,
        }

        data["slack_messages"][new_message["slack_message_id"]] = new_message
        data["slack_messages"] = slack_messages
        payload = {
            "message": "Slack message sent successfully.",
            "message_details": new_message,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendSlackMessage",
                "description": "Sends a message to a specified Slack channel. Can be used to post new messages or reply to existing ones.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel": {
                            "type": "string",
                            "description": "The channel to post the message in (e.g., '#access-requests').",
                        },
                        "message": {
                            "type": "string",
                            "description": "The content of the message to be sent.",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp for the message record.",
                        },
                        "reply_to_message_id": {
                            "type": "string",
                            "description": "Optional. The ID of the message to reply to, creating a thread.",
                        },
                    },
                    "required": ["channel", "message", "timestamp"],
                },
            },
        }


class GetRoleDetailsById(Tool):
    """Locate a specific role by its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None) -> str:
        try:
            roles = data.get("roles", {}).values()
        except:
            roles = []

        for role in roles.values():
            if role.get("role_id") == role_id:
                payload = role
                out = json.dumps(payload)
                return out
        payload = {"error": f"Role with ID '{role_id}' not found."}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRoleDetailsById",
                "description": "Retrieves the full details of a specific role by providing its unique role_id (e.g., 'ROL-013').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "string",
                            "description": "The unique identifier of the role to retrieve (e.g., 'ROL-011').",
                        }
                    },
                    "required": ["role_id"],
                },
            },
        }


class FindResources(Tool):
    """Identify resources using search criteria such as name keywords, criticality, or owner ID."""

    @staticmethod
    def invoke(data: dict[str, Any], name_keyword: str = None, criticality: str = None, owner_id: str = None) -> str:
        try:
            resources = data.get("resources", {}).values()
        except:
            resources = []

        matching_resources = []
        for resource in resources.values():
            if (
                name_keyword
                and name_keyword.lower() not in resource.get("name", "").lower()
            ):
                continue
            if (
                criticality
                and criticality.upper() != resource.get("criticality", "").upper()
            ):
                continue
            if owner_id and owner_id != resource.get("owner_id"):
                continue
            matching_data["resources"][resource_id] = resource
        payload = matching_resources
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindResources",
                "description": "Searches for resources based on a combination of criteria. Returns a list of matching resources.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_keyword": {
                            "type": "string",
                            "description": "A keyword to search for within the resource name.",
                        },
                        "criticality": {
                            "type": "string",
                            "description": "The criticality level to filter by.",
                        },
                        "owner_id": {
                            "type": "string",
                            "description": "The user ID of the resource owner to filter by.",
                        },
                    },
                    "required": [],
                },
            },
        }


class UpdateUserDepartment(Tool):
    """Modifies the 'department' field for a specific user in the database."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, new_department: str = None) -> str:
        user_id_to_update = user_id
        new_department = new_department

        try:
            users = data.get("users", {}).values()
        except (KeyError, json.JSONDecodeError):
            users = []

        user_to_update = None
        for user in users.values():
            if user.get("user_id") == user_id_to_update:
                user["department"] = new_department
                user_to_update = user
                break

        if not user_to_update:
            payload = {"error": f"User with ID '{user_id_to_update}' not found."}
            out = json.dumps(payload)
            return out

        data["users"] = users
        payload = user_to_update
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
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user whose department needs to be updated.",
                        },
                        "new_department": {
                            "type": "string",
                            "description": "The new department to assign to the user.",
                        },
                    },
                    "required": ["user_id", "new_department"],
                },
            },
        }


class GetHubspotTicketById(Tool):
    """Retrieve complete details of a specific HubSpot ticket by its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], ticket_id: str = None) -> str:
        try:
            hubspot_tickets = data.get("hubspot_tickets", {}).values()
        except:
            hubspot_tickets = []

        for ticket in hubspot_tickets.values():
            if ticket.get("ticket_id") == ticket_id:
                payload = ticket
                out = json.dumps(payload)
                return out
        payload = {"error": f"HubSpot ticket with ID '{ticket_id}' not found."}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetHubspotTicketById",
                "description": "Retrieves the full details of a specific HubSpot ticket using its unique ID (e.g., 'TI-053').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {
                            "type": "string",
                            "description": "The unique ID of the HubSpot ticket to retrieve.",
                        }
                    },
                    "required": ["ticket_id"],
                },
            },
        }


class UpdateHubspotTicket(Tool):
    """Modifies an existing HubSpot ticket."""

    @staticmethod
    def invoke(data: dict[str, Any], ticket_id: str = None, timestamp: str = None, status: str = None, priority: str = None,
        closed_at: Any = None,
        description: Any = None,
    ) -> str:
        try:
            hubspot_tickets = data.get("hubspot_tickets", {}).values()
        except:
            hubspot_tickets = []

        ticket_to_update = None
        for ticket in hubspot_tickets.values():
            if ticket.get("ticket_id") == ticket_id:
                if status is not None:
                    ticket["status"] = status
                if priority is not None:
                    ticket["priority"] = priority
                ticket["updated_at"] = timestamp
                ticket_to_update = ticket
                break

        if not ticket_to_update:
            payload = {"error": f"HubSpot ticket with ID '{ticket_id}' not found."}
            out = json.dumps(payload)
            return out

        data["hubspot_tickets"] = hubspot_tickets
        payload = {
            "message": "HubSpot ticket updated successfully.",
            "ticket_details": ticket_to_update,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateHubspotTicket",
                "description": "Updates an existing HubSpot ticket's status, description, or other fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {
                            "type": "string",
                            "description": "The ID of the ticket to update.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The new status for the ticket (e.g., 'CLOSED').",
                        },
                        "description": {
                            "type": "string",
                            "description": "The updated, detailed description of the issue or event.",
                        },
                        "closed_at": {
                            "type": "string",
                            "description": "The timestamp when the ticket was closed.",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp for the update record.",
                        },
                    },
                    "required": ["ticket_id", "timestamp"],
                },
            },
        }


class RevokePolicyException(Tool):
    """Cancels an active policy exception, changing its status to 'REVOKED'."""

    @staticmethod
    def invoke(data: dict[str, Any], exception_id: str = None) -> str:
        try:
            policy_exceptions = data.get("policy_exceptions", {}).values()
        except:
            policy_exceptions = []

        exception_found = False
        for exc in policy_exceptions.values():
            if exc.get("exception_id") == exception_id:
                exc["status"] = "REVOKED"
                exception_found = True
                break

        if not exception_found:
            payload = {"error": f"Policy exception with ID '{exception_id}' not found."}
            out = json.dumps(payload)
            return out

        data["policy_exceptions"] = policy_exceptions
        payload = {
            "message": "Policy exception revoked successfully.",
            "exception_id": exception_id,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RevokePolicyException",
                "description": "Revokes an active policy exception as a remediation action.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {
                            "type": "string",
                            "description": "The ID of the policy exception to revoke.",
                        }
                    },
                    "required": ["exception_id"],
                },
            },
        }


class GetPolicyExceptionById(Tool):
    """Retrieve complete details of a specific policy exception by its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], exception_id: str = None) -> str:
        try:
            policy_exceptions = data.get("policy_exceptions", {}).values()
        except:
            policy_exceptions = []

        for exc in policy_exceptions.values():
            if exc.get("exception_id") == exception_id:
                payload = exc
                out = json.dumps(payload)
                return out
        payload = {"error": f"Policy exception with ID '{exception_id}' not found."}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPolicyExceptionById",
                "description": "Retrieves the full details of a specific policy exception using its unique ID (e.g., 'PE-010').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {
                            "type": "string",
                            "description": "The unique ID of the policy exception to retrieve.",
                        }
                    },
                    "required": ["exception_id"],
                },
            },
        }


class GetPolicyExceptionByUserId(Tool):
    """Identifies all policy exceptions for a specific user, with the option to include inactive exceptions."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, include_inactive: bool = False) -> str:
        terminal_statuses = {"REVOKED", "REJECTED", "EXPIRED"}
        try:
            policy_exceptions = data.get("policy_exceptions", {}).values()
        except:
            policy_exceptions = []

        user_exceptions = []
        for exc in policy_exceptions.values():
            if exc.get("user_id") == user_id:
                if include_inactive:
                    user_exceptions.append(exc)
                elif exc.get("status") not in terminal_statuses:
                    user_exceptions.append(exc)
        payload = user_exceptions
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPolicyExceptionByUserId",
                "description": "Retrieves a list of policy exceptions for a given user ID. By default, it only returns active exceptions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user to find exceptions for.",
                        },
                        "include_inactive": {
                            "type": "boolean",
                            "description": "Set to true to include expired, revoked, or rejected exceptions. Defaults to false.",
                        },
                    },
                    "required": ["user_id"],
                },
            },
        }


class FindRolesByResourceId(Tool):
    """Locates all roles that provide permissions for a specific resource ID."""

    @staticmethod
    def invoke(data: dict[str, Any], role_permissions: list = None, permissions: list = None, resource_id: str = None) -> str:
        try:
            role_permissions = role_permissions if role_permissions is not None else data.get("role_permissions", {}).values()
            permissions = permissions if permissions is not None else data.get("permissions", {}).values()
        except:
            payload = {"error": "Data files not found."}
            out = json.dumps(payload)
            return out

        perm_ids_for_resource = {
            p["permission_id"]
            for p in permissions.values() if p.get("resource_id") == resource_id
        }

        if not perm_ids_for_resource:
            payload = []
            out = json.dumps(payload)
            return out

        role_ids_for_resource = {
            rp["role_id"]
            for rp in role_permissions.values() if rp.get("permission_id") in perm_ids_for_resource
        }
        payload = list(role_ids_for_resource)
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindRolesByResourceId",
                "description": "Returns a list of role IDs that are associated with a given resource ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {
                            "type": "string",
                            "description": "The ID of the resource to find associated roles for.",
                        }
                    },
                    "required": ["resource_id"],
                },
            },
        }


class FindHubspotTicketByDescription(Tool):
    """Identifies a HubSpot ticket by looking for a keyword in its description field."""

    @staticmethod
    def invoke(data: dict[str, Any], keyword: str = None) -> str:
        try:
            tickets = data.get("hubspot_tickets", {}).values()
        except (KeyError, json.JSONDecodeError):
            tickets = []

        for ticket in tickets.values():
            description = ticket.get("description", "")
            if description is None:
                description = ""

            if keyword in description:
                payload = ticket
                out = json.dumps(payload)
                return out
        payload = {
            "error": f"No HubSpot ticket found with keyword '{keyword}' in its description."
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindHubspotTicketByDescription",
                "description": "Finds a HubSpot ticket by searching for a specific keyword within its description text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "keyword": {
                            "type": "string",
                            "description": "The keyword or string to search for in the ticket descriptions (e.g., an alert ID like 'ALRT-001').",
                        }
                    },
                    "required": ["keyword"],
                },
            },
        }


class GetPermissionById(Tool):
    """Retrieve complete details of a specific permission by its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], permission_id: str = None) -> str:
        try:
            permissions = data.get("permissions", {}).values()
        except (KeyError, json.JSONDecodeError):
            permissions = []

        for perm in permissions.values():
            if perm.get("permission_id") == permission_id:
                payload = perm
                out = json.dumps(payload)
                return out
        payload = {"error": f"Permission with ID '{permission_id}' not found."}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPermissionById",
                "description": "Retrieves the full details of a specific permission (action, resource_id) using its unique permission_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "permission_id": {
                            "type": "string",
                            "description": "The unique ID of the permission to retrieve (e.g., 'P-021').",
                        }
                    },
                    "required": ["permission_id"],
                },
            },
        }


class FindResourcesByRoleId(Tool):
    """Identifies all resource IDs that a specific role provides permissions for."""

    @staticmethod
    def invoke(data: dict[str, Any], role_id: str = None) -> str:
        try:
            role_permissions = data.get("role_permissions", {}).values()
            permissions = data.get("permissions", {}).values()
        except:
            payload = {"error": "Data files not found."}
            out = json.dumps(payload)
            return out

        perm_ids_for_role = {
            rp["permission_id"]
            for rp in role_permissions.values() if rp.get("role_id") == role_id
        }

        if not perm_ids_for_role:
            payload = []
            out = json.dumps(payload)
            return out

        resource_ids = {
            p["resource_id"]
            for p in permissions.values() if p.get("permission_id") in perm_ids_for_role
        }
        payload = list(resource_ids)
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindResourcesByRoleId",
                "description": "Returns a list of all unique resource IDs that a specific role has permissions for.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "string",
                            "description": "The ID of the role to find associated resources for.",
                        }
                    },
                    "required": ["role_id"],
                },
            },
        }


class GetSessionDetailsById(Tool):
    """Retrieve complete details of a specific session by its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], session_id: str = None) -> str:
        try:
            sessions = data.get("sessions", {}).values()
        except (KeyError, json.JSONDecodeError):
            sessions = []

        for session in sessions.values():
            if session.get("session_id") == session_id:
                payload = session
                out = json.dumps(payload)
                return out
        payload = {"error": f"Session with ID '{session_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSessionDetailsById",
                "description": "Retrieves the full details of a specific user session using its unique ID (e.g., 'S-028').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "session_id": {
                            "type": "string",
                            "description": "The unique ID of the session to retrieve.",
                        }
                    },
                    "required": ["session_id"],
                },
            },
        }


class CheckUserSessionsById(Tool):
    """Identifies all recent login sessions for a specific user to assist in security investigations."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        user_id_to_find = user_id
        try:
            all_sessions = data.get("sessions", {}).values()
        except (KeyError, json.JSONDecodeError):
            all_sessions = []

        user_sessions = [
            session
            for session in all_sessions.values() if session.get("user_id") == user_id_to_find
        ]
        payload = user_sessions
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckUserSessionsById",
                "description": "Retrieves a list of all recent login sessions for a specific user ID as part of a security investigation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user whose sessions are to be checked.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }


class UpdateResourceOwner(Tool):
    """Modifies the 'owner_id' field for a specific resource in the database."""

    @staticmethod
    def invoke(data: dict[str, Any], resource_id: str = None, new_owner_id: str = None) -> str:
        resource_id_to_update = resource_id
        new_owner_id = new_owner_id

        try:
            resources = data.get("resources", {}).values()
        except (KeyError, json.JSONDecodeError):
            resources = []

        resource_to_update = None
        for resource in resources.values():
            if resource.get("resource_id") == resource_id_to_update:
                resource["owner_id"] = new_owner_id
                resource_to_update = resource
                break

        if not resource_to_update:
            payload = {"error": f"Resource with ID '{resource_id_to_update}' not found."}
            out = json.dumps(
                payload)
            return out

        data["resources"] = resources
        payload = {
                "message": "Resource owner updated successfully.",
                "resource_details": resource_to_update,
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateResourceOwner",
                "description": "Updates the owner of a specific resource.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {
                            "type": "string",
                            "description": "The unique ID of the resource whose owner needs to be updated.",
                        },
                        "new_owner_id": {
                            "type": "string",
                            "description": "The user ID of the new owner for the resource.",
                        },
                    },
                    "required": ["resource_id", "new_owner_id"],
                },
            },
        }


class UpdateAccessRequest(Tool):
    """Modifies an existing access request, utilized for rerouting or adjustments."""

    @staticmethod
    def invoke(data: dict[str, Any], request_id: str = None, new_reviewer_id: str = None, new_status: str = None, timestamp: str = None) -> str:
        for req in data.get("access_requests", {}).values():
            if req.get("request_id") == request_id:
                if new_reviewer_id:
                    req["reviewer_id"] = new_reviewer_id
                if new_status:
                    req["status"] = new_status
                req["decision_at"] = timestamp
                payload = {"status": "success", "updated_request_id": request_id}
                out = json.dumps(payload)
                return out
        payload = {"status": "error", "message": "Request not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAccessRequest",
                "description": "Updates an existing access request. Primarily used to reroute a request to a new approver by changing the reviewer_id and resetting the status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {
                            "type": "string",
                            "description": "The ID of the access request to update.",
                        },
                        "new_reviewer_id": {
                            "type": "string",
                            "description": "The user_id of the new approver to assign the request to.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status for the request, e.g., 'PENDING'.",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The timestamp of the update action.",
                        },
                    },
                    "required": ["request_id"],
                },
            },
        }


class FindAccessRequestsByUserId(Tool):
    """Identifies all access requests made by a specific user."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        user_id_to_find = user_id
        try:
            all_requests = data.get("access_requests", {}).values()
        except (KeyError, json.JSONDecodeError):
            all_requests = []

        user_requests = [
            request
            for request in all_requests.values() if request.get("user_id") == user_id_to_find
        ]
        payload = user_requests
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindAccessRequestsByUserId",
                "description": "Retrieves a list of all historical access requests submitted by a specific user, which can then be reviewed for patterns.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user whose access requests are to be retrieved.",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }


class GetPermissionByResourceId(Tool):
    """Locates all permissions linked to a specific resource ID."""

    @staticmethod
    def invoke(data: dict[str, Any], resource_id: str = None) -> str:
        pass
        resource_id_to_find = resource_id
        try:
            all_permissions = data.get("permissions", {}).values()
        except (KeyError, json.JSONDecodeError):
            payload = []
            out = json.dumps(payload)
            return out

        matching_permissions = [
            perm
            for perm in all_permissions.values() if perm.get("resource_id") == resource_id_to_find
        ]
        payload = matching_permissions
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getPermissionByResourceId",
                "description": "Retrieves a list of all permissions that are directly associated with a specific resource ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {
                            "type": "string",
                            "description": "The unique ID of the resource to find permissions for (e.g., 'RES-032').",
                        }
                    },
                    "required": ["resource_id"],
                },
            },
        }


class GetUserRoleDetailsByUserRoleId(Tool):
    """Fetches the details of a specific user role assignment using its user_role_id."""

    @staticmethod
    def invoke(data: dict[str, Any], user_role_id: str = None) -> str:
        try:
            user_roles = data.get("user_roles", {}).values()
        except:
            user_roles = []

        for user_role in user_roles.values():
            if user_role.get("user_role_id") == user_role_id:
                payload = user_role
                out = json.dumps(payload)
                return out
        payload = {"error": f"User role with ID '{user_role_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserRoleDetailsByUserRoleId",
                "description": "Retrieves the full details of a specific user role assignment by its user_role_id (e.g., 'UR-029').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_role_id": {
                            "type": "string",
                            "description": "The unique identifier of the user role assignment to retrieve (e.g., 'UR-029').",
                        }
                    },
                    "required": ["user_role_id"],
                },
            },
        }


TOOLS = [
    GetCurrentTime(),
    CreateUser(),
    GetUserDetailsById(),
    GetUserDetailsByUsername(),
    GetUserDetailsByEmail(),
    GetRoleIdByName(),
    CreateAccessRequest(),
    AssignRoleToUser(),
    LogAuditEvent(),
    SendEmail(),
    UpdateUserStatus(),
    GetUserRolesByUserId(),
    RevokeRoleFromUser(),
    GetAccessRequestById(),
    GetResourceDetailsById(),
    ApproveAccessRequest(),
    GetSiemAlertById(),
    GetCertificationDetailsById(),
    FindUsersWithRole(),
    UpdateCertificationStatus(),
    CreatePolicyException(),
    CreateHubspotTicket(),
    GetPermissionByName(),
    ListUserSessions(),
    RejectAccessRequest(),
    GetResourceByName(),
    CreateSiemAlert(),
    GetSlackMessageById(),
    FindAccessRequestByDetails(),
    SendSlackMessage(),
    GetRoleDetailsById(),
    FindResources(),
    UpdateUserDepartment(),
    GetResourceByName(),
    GetHubspotTicketById(),
    UpdateHubspotTicket(),
    RevokePolicyException(),
    GetPolicyExceptionById(),
    GetPolicyExceptionByUserId(),
    FindRolesByResourceId(),
    FindHubspotTicketByDescription(),
    GetPermissionById(),
    FindResourcesByRoleId(),
    GetSessionDetailsById(),
    CheckUserSessionsById(),
    UpdateResourceOwner(),
    UpdateAccessRequest(),
    FindAccessRequestsByUserId(),
    GetPermissionByResourceId(),
    GetUserRoleDetailsByUserRoleId(),
]