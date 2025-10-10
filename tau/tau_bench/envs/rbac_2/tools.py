from domains.dto import Tool
import json
from datetime import datetime, UTC
from typing import Any, Dict, List

NOW: datetime = datetime(2025, 8, 9, 10, 00, 00, tzinfo=UTC)

class GetCurrentTime(Tool):
    """ Returns a fixed current date and time formatted as "YYYY-MM-DD HH:MM:SS+00:00". e.g. "2025-08-09 10:00:00+00:00" """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # Format the datetime as "YYYY-MM-DD HH:MM:SS+00:00"
        formatted_time = NOW.isoformat(timespec='seconds').replace("T", " ")
        return json.dumps({"current_time": formatted_time})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Returns the current date and time as YYYY-MM-DD HH:MM:SS+00:00",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        }

class CreateUser(Tool):
    """ Creates a new user in the user.json file with correct formatting and default values. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        try:
           users = data.get('users', [])
        except (KeyError, json.JSONDecodeError):
            users = []
        existing_ids = [int(item["user_id"].replace("U-", "")) for item in users if item["user_id"].startswith("U-")]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        user_id = f"U-{next_id_num:03d}"

        new_user = {
            "user_id": user_id,
            "username": kwargs.get("username"),
            "email": kwargs.get("email"),
            "department": kwargs.get("department"),
            "status": kwargs.get("status", "ACTIVE"),  # Default to ACTIVE if not specified
            "mfa_enabled": False
        }
        users.append(new_user)
        data["users.json"] = json.dumps(users)
        return json.dumps(new_user)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_user",
                "description": "Creates a new user entry in the database.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "username": {
                            "type": "string",
                            "description": "The username of the new user."
                        },
                        "email": {
                            "type": "string",
                            "description": "The email address of the new user."
                            },
                        "department": {
                            "type": "string",
                            "description": "The department where the new user belongs."
                            },
                        "status": {
                            "type": "string",
                            "description": "The status of the new user (e.g., ACTIVE, INACTIVE)."
                            }
                    },
                    "required": ["username", "email", "department", "status"]
                }
            }
        }

class GetUserDetailsById(Tool):
    """Retrieves a user's full details using their unique user_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        try:
           users = data.get('users', [])
        except (KeyError, json.JSONDecodeError):
            users = []

        for user in users:
            if user.get('user_id') == user_id:
                return json.dumps(user)

        return json.dumps({"error": "User not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_details_by_id",
                "description": "Retrieves full user details based on their unique user_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user (e.g., U-001)."
                        }
                    },
                    "required": ["user_id"]
                }
            }
        }

class GetUserDetailsByUsername(Tool):
    """Retrieves a user's full details using their username."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        username = kwargs.get("username")
        try:
           users = data.get('users', [])
        except (KeyError, json.JSONDecodeError):
            users = []

        for user in users:
            if user.get('username') == username:
                return json.dumps(user)

        return json.dumps({"error": "User not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_details_by_username",
                "description": "Retrieves full user details based on their username.",
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

class GetUserDetailsByEmail(Tool):
    """Retrieves a user's full details using their email address."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        email = kwargs.get("email")
        try:
            users = data.get('users', [])
        except (KeyError, json.JSONDecodeError):
            users = []

        for user in users:
            if user.get('email') == email:
                return json.dumps(user)

        return json.dumps({"error": "User not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_details_by_email",
                "description": "Retrieves full user details based on their email address.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "email": {
                            "type": "string",
                            "description": "The email address to search for."
                        }
                    },
                "required": ["email"]
                }
            }
        }

class GetRoleIdByName(Tool):
    """
    Finds one or more roles by searching for a name. It prioritizes an exact match
    but will also return other roles that contain the search string.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        find_role_name = kwargs.get("role_name")
        try:
            roles = data.get('roles', [])
        except (KeyError, json.JSONDecodeError):
            roles = []

        exact_matches = []
        partial_matches = []

        for role in roles:
            current_role_name = role.get("role_name", "")
            
            if current_role_name == find_role_name:
                exact_matches.append(role)
            elif find_role_name in current_role_name:
                partial_matches.append(role)
        
        all_matches = exact_matches + partial_matches

        if not all_matches:
            return json.dumps({"error": f"No roles found matching or containing '{find_role_name}'."})
        
        return json.dumps(all_matches)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_role_id_by_name",
                "description": "Retrieves a list of roles based on a name. Returns all roles that either exactly match the name or contain the name as a substring.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_name": {
                            "type": "string",
                            "description": "The name of the role to search for (e.g., 'sales-lead')."
                        }
                    },
                    "required": ["role_name"]
                }
            }
        }

class CreateAccessRequest(Tool):
    """ Creates a new access request for a user to receive a specific role for a resource. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        try:
            requests = data.get('access_requests', [])
        except (KeyError, json.JSONDecodeError):
            requests = []

        existing_ids = [int(r["request_id"].replace("AR-", "")) for r in requests if r.get("request_id", "").startswith("AR-")]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        request_id = f"AR-{next_id_num:03d}"

        new_request = {
            "request_id": request_id,
            "user_id": kwargs.get("user_id"),
            "resource_id": kwargs.get("resource_id"),
            "requested_role_id": kwargs.get("role_id"),
            "justification": kwargs.get("justification"),
            "status": "PENDING",
            "submitted_at": kwargs.get("timestamp"),
            "reviewed_by": None,
            "decision_at": None
        }

        requests.append(new_request)
        data["access_requests.json"] = json.dumps(requests, indent=4)

        return json.dumps(new_request)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_access_request",
                "description": "Submits a request for a user to be granted a role. Requires subsequent approval.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user who will receive the role."
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "The ID of the resource the role applies to."
                        },
                        "role_id": {
                            "type": "string",
                            "description": "The ID of the requested role."
                        },
                        "justification": {
                            "type": "string",
                            "description": "A brief reason for the request."
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp for when the request is submitted."
                        }
                    },
                    "required": ["user_id", "resource_id", "role_id", "justification"]
                }
            }
        }

class AssignRoleToUser(Tool):
    """ Directly assigning a role to an user. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        try:
            user_roles = data.get('user_roles', [])
        except (KeyError, json.JSONDecodeError):
            user_roles = []
        existing_ids = [int(ur["user_role_id"].replace("UR-", "")) for ur in user_roles if ur.get("user_role_id", "").startswith("UR-")]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        user_role_id = f"UR-{next_id_num:03d}"

        new_assignment = {
            "user_role_id": user_role_id,
            "user_id": kwargs.get("user_id"),
            "role_id": kwargs.get("role_id"),
            "assigned_by": kwargs.get("assigned_by"),
            "expires_on": kwargs.get("expires_on", None) # Optional: for temporary roles
        }

        user_roles.append(new_assignment)
        data["user_roles.json"] = json.dumps(user_roles, indent=4)

        return json.dumps(new_assignment)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_role_to_user",
                "description": "Directly assigns a specific role to a user. This is a privileged action for processes like onboarding.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user to whom the role will be assigned."
                        },
                        "role_id": {
                            "type": "string",
                            "description": "The unique ID of the role to be assigned."
                        },
                        "assigned_by": {
                            "type": "string",
                            "description": "The user ID of the administrator or manager performing the assignment."
                        },
                        "expires_on": {
                            "type": "string",
                            "description": "Optional: The timestamp when the role assignment expires. Use null for permanent roles."
                        }
                    },
                    "required": ["user_id", "role_id", "assigned_by"]
                }
            }
        }

class LogAuditEvent(Tool):
    """ Recording actions or events in the system's audit log used for security, compliance, and traceability."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        try:
           audit_logs = data.get('audit_logs', [])
        except (KeyError, json.JSONDecodeError):
            audit_logs = []
        existing_ids = [int(log["log_id"].replace("L-", "")) for log in audit_logs if log.get("log_id", "").startswith("L-")]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        log_id = f"L-{next_id_num:03d}"

        new_log = {
            "log_id": log_id,
            "actor_id": kwargs.get("actor_id"),
            "action_type": kwargs.get("action_type"),
            "target_id": kwargs.get("target_id"),
            "timestamp": kwargs.get("timestamp"),
            "details": kwargs.get("details")
        }

        audit_logs.append(new_log)
        data["audit_logs.json"] = json.dumps(audit_logs, indent=4)

        return json.dumps({
            "message": "Audit event logged successfully.",
            "log_details": new_log
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_audit_event",
                "description": "Records an action in the system's audit log for compliance and tracking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "actor_id": {
                            "type": "string",
                            "description": "The user ID of the user who performed the action."
                        },
                        "action_type": {
                            "type": "string",
                            "description": "The type of action being logged (e.g., USER_CREATED, ROLE_ASSIGNED, ACCESS_GRANTED)."
                        },
                        "target_id": {
                            "type": "string",
                            "description": "The ID of the entity that was the target of the action (e.g., a user_id, role_id, or request_id)."
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The timestamp of the event, in ISO 8601 format."
                        },
                        "details": {
                            "type": "string",
                            "description": "A human-readable summary of the event."
                        }
                    },
                    "required": ["actor_id", "action_type", "target_id", "timestamp", "details"]
                }
            }
        }

class SendEmail(Tool):
    """ A tool to send an email by creating a record in the database."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        try:
            emails = data.get('emails', [])
        except (KeyError, json.JSONDecodeError):
            emails = []
        existing_ids = [int(email["email_id"].replace("EM-", "")) for email in emails if email.get("email_id", "").startswith("EM-")]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        email_id = f"EM-{next_id_num:03d}"

        new_email = {
            "email_id": email_id,
            "sender": kwargs.get("sender"),
            "receiver": kwargs.get("receiver"),
            "subject": kwargs.get("subject"),
            "text_content": kwargs.get("text_content"),
            "timestamp": kwargs.get("timestamp"),
        }

        emails.append(new_email)
        data["emails.json"] = json.dumps(emails, indent=4)

        return json.dumps(new_email)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "send_email",
                "description": "Sends a standard onboarding email by creating a record of it in the database.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sender": {
                            "type": "string",
                            "description": "The email address of the sender (e.g., onboarding@taucorp.com)."
                        },
                        "receiver": {
                            "type": "string",
                            "description": "The email address of the recipient."
                        },
                        "subject": {
                            "type": "string",
                            "description": "The subject line of the email."
                        },
                        "text_content": {
                            "type": "string",
                            "description": "The plain text body of the email."
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The timestamp of when the email is sent, in ISO 8601 format."
                        },
                    },
                    "required": ["sender", "receiver", "subject", "text_content", "timestamp"]
                }
            }
        }

class UpdateUserStatus(Tool):
    """ Updating the 'status' field of a specific user in the database. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id_to_update = kwargs.get("user_id")
        new_status = kwargs.get("new_status")

        try:
            users = data.get('users', [])
        except:
            users = []

        user_to_update = None
        for user in users:
            if user.get("user_id") == user_id_to_update:
                user["status"] = new_status
                user_to_update = user
                break

        if not user_to_update:
            return json.dumps({"error": f"User with ID '{user_id_to_update}' not found."})

        data['users'] = users
        return json.dumps(user_to_update)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_user_status",
                "description": "Updates the status of a user account (e.g., to ACTIVE, DISABLED, SUSPENDED).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user whose status needs to be updated."
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status to set for the user. Must be one of: ACTIVE, INACTIVE, SUSPENDED, DISABLED."
                        }
                    },
                    "required": ["user_id", "new_status"]
                }
            }
        }

class GetUserRolesByUserId(Tool):
    """ Retrieves all role assignments for a specific user ID. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        try:
            user_roles = data.get('user_roles', [])
        except:
            user_roles = []

        assigned_roles = [
            role for role in user_roles
            if role.get("user_id") == user_id
        ]

        return json.dumps(assigned_roles)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_roles_by_user_id",
                "description": "Lists all roles currently assigned to a specific user ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user whose roles are to be listed."
                        }
                    },
                    "required": ["user_id"]
                }
            }
        }

class RevokeRoleFromUser(Tool):
    """ Revokes a specific role from a user by deleting the user-role entry from the database."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_role_id = kwargs.get("user_role_id")
        try:
            user_roles = data.get('user_roles', [])
        except:
            user_roles = []

        index = -1
        for i, assignment in enumerate(user_roles):
            if assignment.get("user_role_id") == user_role_id:
                index = i
                break

        if index != -1:
            revoked_assignment = user_roles.pop(index)
        else:
            return json.dumps({"error": f"User-role with ID '{user_role_id}' not found."})

        data['user_roles'] = user_roles

        return json.dumps({
            "message": "User-role assignment revoked successfully.",
            "revoked_details": revoked_assignment
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "revoke_role_from_user",
                "description": "Revokes a specific role from a user by deleting the assignment record. Requires the user_role_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_role_id": {
                            "type": "string",
                            "description": "The unique ID of the user-role assignment to be revoked (e.g., 'UR-003')."
                        }
                    },
                    "required": ["user_role_id"]
                }
            }
        }

class GetAccessRequestById(Tool):
    """ Get the full details of a specific access request using its ID. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        request_id = kwargs.get("request_id")
        try:
            access_requests = data.get('access_requests', [])
        except:
            access_requests = []

        for request in access_requests:
            if request.get("request_id") == request_id:
                return json.dumps(request)

        return json.dumps({"error": f"Access request with ID '{request_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_access_request_by_id",
                "description": "Retrieves the full details of a specific access request using its unique ID (e.g., 'AR-007').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {
                            "type": "string",
                            "description": "The unique ID of the access request to retrieve."
                        }
                    },
                    "required": ["request_id"]
                }
            }
        }

class GetResourceDetailsById(Tool):
    """ Get the full details of a specific resource using its ID. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        resource_id = kwargs.get("resource_id")
        try:
            resources = data.get('resources', [])
        except:
            resources = []

        for resource in resources:
            if resource.get("resource_id") == resource_id:
                return json.dumps(resource)

        return json.dumps({"error": f"Resource with ID '{resource_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_resource_details_by_id",
                "description": "Retrieves the full details of a specific resource (e.g., its criticality) using its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {
                            "type": "string",
                            "description": "The unique ID of the resource to retrieve (e.g., 'RES-025')."
                        }
                    },
                    "required": ["resource_id"]
                }
            }
        }

class ApproveAccessRequest(Tool):
    """ Approve access requests and change their status from 'PENDING' to 'APPROVED' and create the required user-role assignment to grant the access."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        request_id = kwargs.get("request_id")
        reviewer_id = kwargs.get("reviewer_id")
        timestamp = kwargs.get("timestamp")
        expires_on = kwargs.get("expires_on")

        try:
            access_requests = data.get('access_requests', [])
            user_roles = data.get('user_roles', [])
        except Exception as e:
            return json.dumps({"error": f"Failed to load data lists: {e}"})

        request = None
        for req in access_requests:
            if req.get("request_id") == request_id and req.get("status") == "PENDING":
                request = req
                break

        if not request:
            return json.dumps({"error": f"Pending access request with ID '{request_id}' not found."})

        request["status"] = "APPROVED"
        request["reviewed_by"] = reviewer_id
        request["decision_at"] = timestamp

        ur_existing_ids = [int(ur["user_role_id"].replace("UR-", "")) for ur in user_roles if ur.get("user_role_id", "").startswith("UR-")]
        next_ur_id = max(ur_existing_ids) + 1 if ur_existing_ids else 1

        new_role_assignment = {
            "user_role_id": f"UR-{next_ur_id:03d}",
            "user_id": request["user_id"],
            "role_id": request["requested_role_id"],
            "assigned_by": reviewer_id,
            "assigned_on": timestamp,
            "expires_on": expires_on
        }
        user_roles.append(new_role_assignment)

        data['access_requests'] = access_requests
        data['user_roles'] = user_roles

        return json.dumps({
            "message": "Access request approved and role granted successfully.",
            "request_id": request_id,
            "new_assignment_id": new_role_assignment["user_role_id"]
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "approve_access_request",
                "description": "Approves a pending access request. This updates the request status and grants the specified role to the user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {
                            "type": "string",
                            "description": "The unique ID of the access request to approve."
                        },
                        "reviewer_id": {
                            "type": "string",
                            "description": "The user ID of the person approving the request."
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp of the approval decision."
                        },
                        "expires_on": {
                            "type": "string",
                            "description": "Optional: The timestamp when the role assignment expires. Use null for permanent roles."
                        }
                    },
                    "required": ["request_id", "reviewer_id", "timestamp"]
                }
            }
        }

class GetSiemAlertById(Tool):
    """ Get the full details of a specific SIEM alert using its ID. """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        alert_id = kwargs.get("alert_id")
        try:
            siem_alerts = data.get('siem_alerts', [])
        except:
            siem_alerts = []

        for alert in siem_alerts:
            if alert.get("alert_id") == alert_id:
                return json.dumps(alert)

        return json.dumps({"error": f"SIEM alert with ID '{alert_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_siem_alert_by_id",
                "description": "Retrieves the full details of a specific SIEM alert using its unique ID (e.g., 'ALRT-012').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "alert_id": {
                            "type": "string",
                            "description": "The unique ID of the SIEM alert to retrieve."
                        }
                    },
                    "required": ["alert_id"]
                }
            }
        }

class GetCertificationDetailsById(Tool):
    """ Get the full details of a specific access certification campaign using its ID. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        certification_id = kwargs.get("certification_id")
        try:
            certifications = data.get('certifications', [])
        except:
            certifications = []

        for cert in certifications:
            if cert.get("certification_id") == certification_id:
                return json.dumps(cert)

        return json.dumps({"error": f"Certification with ID '{certification_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_certification_details_by_id",
                "description": "Retrieves the full details of a specific access certification campaign using its unique ID (e.g., 'C-005').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {
                            "type": "string",
                            "description": "The unique ID of the certification campaign to retrieve."
                        }
                    },
                    "required": ["certification_id"]
                }
            }
        }

class FindUsersWithRole(Tool):
    """ Find all users who are currently assigned a specific role. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role_id = kwargs.get("role_id")
        try:
            all_user_roles = data.get('user_roles', [])
        except:
            all_user_roles = []

        users_with_role = [
            assignment["user_id"] for assignment in all_user_roles
            if assignment.get("role_id") == role_id
        ]
        unique_user_ids = list(set(users_with_role))
        
        return json.dumps(unique_user_ids)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_users_with_role",
                "description": "Finds and returns a list of all user IDs that are currently assigned a specific role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "string",
                            "description": "The unique ID of the role to search for (e.g., 'ROL-013')."
                        }
                    },
                    "required": ["role_id"]
                }
            }
        }

class UpdateCertificationStatus(Tool):
    """ Update the status of an access certification campaign. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        certification_id_to_update = kwargs.get("certification_id")
        new_status = kwargs.get("new_status")
        timestamp = kwargs.get("timestamp")
        try:
            certifications = data.get('certifications', [])
        except:
            certifications = []

        certification_found = False
        updated_certification = None
        for cert in certifications:
            if cert.get("certification_id") == certification_id_to_update:
                cert["status"] = new_status
                if new_status == "COMPLETED":
                    cert["completed_on"] = timestamp

                certification_found = True
                updated_certification = cert
                break

        if not certification_found:
            return json.dumps({"error": f"Certification with ID '{certification_id_to_update}' not found."})

        data['certifications'] = certifications

        return json.dumps({
            "message": "Certification campaign status updated successfully.",
            "certification_details": updated_certification
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_certification_status",
                "description": "Updates the status of an access certification campaign (e.g., to 'COMPLETED').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "certification_id": {
                            "type": "string",
                            "description": "The unique ID of the certification campaign to update."
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status to set for the campaign (e.g., 'COMPLETED')."
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp to record as the completion time."
                        }
                    },
                    "required": ["certification_id", "new_status", "timestamp"]
                }
            }
        }

class CreatePolicyException(Tool):
    """ Create a new policy exception for granting emergency access based on a specific permission. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        try:
            policy_exceptions = data.get('policy_exceptions', [])
        except:
            policy_exceptions = []

        existing_ids = [int(item["exception_id"].replace("PE-", "")) for item in policy_exceptions if
                        item.get("exception_id", "").startswith("PE-")]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        exception_id = f"PE-{next_id_num:03d}"
        timestamp = kwargs.get("timestamp")

        new_exception = {
            "exception_id": exception_id,
            "user_id": kwargs.get("user_id"),
            "permission_id": kwargs.get("permission_id"),
            "reviewed_by": kwargs.get("approved_by"),
            "requested_on": timestamp,
            "reviewed_on": timestamp,
            "expires_on": kwargs.get("expires_on"),
            "reason": kwargs.get("justification"),
            "status": "ACTIVE"
        }

        policy_exceptions.append(new_exception)
        data['policy_exceptions'] = policy_exceptions

        return json.dumps({
            "message": "Policy exception created successfully.",
            "exception_details": new_exception
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_policy_exception",
                "description": "Creates a policy exception to grant temporary, emergency access for a specific permission.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The ID of the user receiving the exception."},
                        "permission_id": {"type": "string",
                                          "description": "The ID of the specific permission being granted."},
                        "justification": {"type": "string",
                                          "description": "The business reason for the emergency exception."},
                        "approved_by": {"type": "string",
                                        "description": "The ID of the manager approving the exception."},
                        "expires_at": {"type": "string",
                                       "description": "The timestamp when this exception will automatically expire."},
                        "timestamp": {"type": "string",
                                      "description": "The current timestamp for the creation and review record."}
                    },
                    "required": ["user_id", "permission_id", "justification", "approved_by", "expires_at", "timestamp"]
                }
            }
        }

class CreateHubspotTicket(Tool):
    """ Create a new ticket in the HubSpot system for tracking. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        try:
            hubspot_tickets = data.get('hubspot_tickets', [])
        except:
            hubspot_tickets = []

        existing_ids = [int(item["ticket_id"].replace("TI-", "")) for item in hubspot_tickets if
                        item.get("ticket_id", "").startswith("TI-")]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        ticket_id = f"TI-{next_id_num:03d}"
        timestamp = kwargs.get("timestamp")

        new_ticket = {
            "ticket_id": ticket_id,
            "created_at": timestamp,
            "updated_at": timestamp, 
            "subject": kwargs.get("subject"),
            "description": kwargs.get("description"),
            "status": "OPEN",
            "priority": kwargs.get("priority"),
            "assignee_id": kwargs.get("assignee_id"),
            "requester_id": kwargs.get("requester_id"),
            "category": kwargs.get("category"),
            "closed_at": None
        }

        hubspot_tickets.append(new_ticket)
        data['hubspot_tickets'] = hubspot_tickets

        return json.dumps({
            "message": "HubSpot ticket created successfully.",
            "ticket_details": new_ticket
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_hubspot_ticket",
                "description": "Creates a new ticket in the HubSpot system to track an incident or request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject": {"type": "string", "description": "The title or subject line of the ticket."},
                        "description": {"type": "string",
                                        "description": "A detailed description of the issue or event."},
                        "priority": {"type": "string",
                                     "description": "The priority level of the ticket (e.g., HIGH, MEDIUM, LOW)."},
                        "assignee_id": {"type": "string",
                                        "description": "The user ID of the person the ticket is assigned to."},
                        "requester_id": {"type": "string",
                                         "description": "The user ID of the person who initiated the event or request."},
                        "category": {"type": "string",
                                     "description": "The category of the ticket (e.g., SECURITY_INCIDENT, ACCESS_REQUEST)."},
                        "timestamp": {"type": "string", "description": "The current timestamp for the creation record."}
                    },
                    "required": ["subject", "description", "priority", "assignee_id", "requester_id", "category",
                                 "timestamp"]
                }
            }
        }

class GetPermissionByName(Tool):
    """
    Find a specific permission using its action name. Can be filtered by a resource ID.
    If resource_id is omitted, it will return the first permission matching the name.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        permission_name = kwargs.get("permission_name")
        resource_id = kwargs.get("resource_id") 
        try:
            permissions = data.get('permissions', [])
        except (KeyError, json.JSONDecodeError):
            permissions = []

        for perm in permissions:
            if perm.get("action") == permission_name:
                if resource_id and perm.get("resource_id") != resource_id:
                    continue
                return json.dumps(perm)

        error_message = f"Permission '{permission_name}' not found."
        if resource_id:
            error_message += f" on resource '{resource_id}'"
            
        return json.dumps({"error": error_message})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_permission_by_name",
                "description": "Retrieves the details of a specific permission by its action name (e.g., 'admin-db-cluster'). Can be optionally filtered by the resource it applies to.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "permission_name": {
                            "type": "string",
                            "description": "The name of the action the permission allows (e.g., 'read-repo', 'admin-db-cluster')."
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "Optional. The ID of the resource to filter by (e.g., 'RES-025')." 
                        }
                    },
                    "required": ["permission_name"] 
                }
            }
        }

class ListUserSessions(Tool):
    """ Find all recent login sessions for a specific user. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id_to_find = kwargs.get("user_id")
        try:
            all_sessions = data.get('sessions', [])
        except:
            all_sessions = []

        user_sessions = [
            session for session in all_sessions
            if session.get("user_id") == user_id_to_find
        ]

        return json.dumps(user_sessions)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_user_sessions",
                "description": "Retrieves a list of all recent login sessions for a specific user by their user ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user whose sessions are to be retrieved."
                        }
                    },
                    "required": ["user_id"]
                }
            }
        }

class RejectAccessRequest(Tool):
    """ Reject an access request and record the reason. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        request_id_to_find = kwargs.get("request_id")
        reviewer_id = kwargs.get("reviewer_id")
        timestamp = kwargs.get("timestamp")
        rejection_reason = kwargs.get("rejection_reason")

        try:
            access_requests = data.get('access_requests', [])
        except:
            access_requests = []

        request_found = False
        for request in access_requests:
            if request.get("request_id") == request_id_to_find:
                request["status"] = "REJECTED"
                request["reviewed_by"] = reviewer_id
                request["decision_at"] = timestamp
                request["rejection_reason"] = rejection_reason
                request_found = True
                break

        if not request_found:
            return json.dumps({"error": f"Access request with ID '{request_id_to_find}' not found."})

        data['access_requests'] = access_requests

        return json.dumps({
            "message": "Access request rejected successfully.",
            "request_id": request_id_to_find,
            "new_status": "REJECTED"
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "reject_access_request",
                "description": "Rejects a pending access request and records the reason for the rejection.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {
                            "type": "string",
                            "description": "The unique ID of the access request to be rejected."
                        },
                        "reviewer_id": {
                            "type": "string",
                            "description": "The user ID of the manager who is rejecting the request."
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp for the decision record."
                        },
                        "rejection_reason": {
                            "type": "string",
                            "description": "A brief, clear reason for why the request is being rejected."
                        }
                    },
                    "required": ["request_id", "reviewer_id", "timestamp", "rejection_reason"]
                }
            }
        }

class GetResourceByName(Tool):
    """ Find a resource using its human-readable name. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        resource_name_to_find = kwargs.get("resource_name")
        try:
            all_resources = data.get('resources', [])
        except:
            all_resources = []

        for resource in all_resources:
            if resource.get("name") == resource_name_to_find:
                # 3. If a match is found, return the entire resource object.
                return json.dumps(resource)

        return json.dumps({"error": f"Resource with name '{resource_name_to_find}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_resource_by_name",
                "description": "Retrieves the full details of a resource by searching for its exact name (e.g., 'Sales Reporting Dashboard').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_name": {
                            "type": "string",
                            "description": "The unique, human-readable name of the resource."
                        }
                    },
                    "required": ["resource_name"]
                }
            }
        }

class CreateSiemAlert(Tool):
    """ Manually create a new SIEM alert based on an investigation. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        try:
            siem_alerts = data.get('siem_alerts', [])
        except:
            siem_alerts = []

        existing_ids = [int(item["alert_id"].replace("ALRT-", "")) for item in siem_alerts if item.get("alert_id", "").startswith("ALRT-")]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        alert_id = f"ALRT-{next_id_num:03d}"

        new_alert = {
            "alert_id": alert_id,
            "timestamp": kwargs.get("timestamp"),
            "user_id": kwargs.get("user_id"),
            "resource_id": kwargs.get("resource_id"),
            "alert_type": kwargs.get("alert_type"),
            "severity": kwargs.get("severity")
        }

        siem_alerts.append(new_alert)
        data['siem_alerts'] = siem_alerts

        return json.dumps({
            "message": "SIEM alert created successfully.",
            "alert_details": new_alert
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_siem_alert",
                "description": "Manually creates a new SIEM (Security Information and Event Management) alert to formally track a discovered security incident.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user associated with the security event."
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "The ID of the resource that was targeted."
                        },
                        "alert_type": {
                            "type": "string",
                            "description": "The type of alert (e.g., 'POTENTIAL_DATA_EXFILTRATION', 'UNAUTHORIZED_ACCESS_ATTEMPT')."
                        },
                        "severity": {
                            "type": "string",
                            "description": "The severity of the alert (e.g., 'CRITICAL', 'HIGH', 'MEDIUM', 'LOW')."
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp to record as the alert creation time."
                        }
                    },
                    "required": ["user_id", "resource_id", "alert_type", "severity", "timestamp"]
                }
            }
        }

class GetSlackMessageById(Tool):
    """ Retrieve the details of a specific Slack message using its ID. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        message_id_to_find = kwargs.get("message_id")
        try:
            slack_messages = data.get('slack_messages', [])
        except:
            slack_messages = []

        for message in slack_messages:
            if message.get("message_id") == message_id_to_find:
                return json.dumps(message)

        return json.dumps({"error": f"Slack message with ID '{message_id_to_find}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_slack_message_by_id",
                "description": "Retrieves the full details of a Slack message, including its content and channel, by its unique ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message_id": {
                            "type": "string",
                            "description": "The unique ID of the Slack message (e.g., 'SL-007')."
                        }
                    },
                    "required": ["message_id"]
                }
            }
        }

class FindAccessRequestByDetails(Tool):
    """ Find an access request based on its content details. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        role_id = kwargs.get("role_id")
        resource_id = kwargs.get("resource_id")

        try:
            access_requests = data.get('access_requests', [])
        except:
            access_requests = []

        for request in access_requests:
            if (request.get("user_id") == user_id and
                request.get("requested_role_id") == role_id and
                request.get("resource_id") == resource_id):
                # 3. If a match is found, return the entire request object.
                return json.dumps(request)

        return json.dumps({"error": "No matching access request found for the provided details."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_access_request_by_details",
                "description": "Finds a specific access request by searching for a combination of the user who requested it, the role they requested, and the resource they requested it for.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user ID of the requester."
                        },
                        "role_id": {
                            "type": "string",
                            "description": "The role ID that was requested."
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "The resource ID that was requested."
                        }
                    },
                    "required": ["user_id", "role_id", "resource_id"]
                }
            }
        }

class SendSlackMessage(Tool):
    """ Send a message to a Slack channel. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        try:
            slack_messages = data.get('slack_messages', [])
        except:
            slack_messages = []

        existing_ids = [int(item["message_id"].replace("SL-", "")) for item in slack_messages if item.get("message_id", "").startswith("SL-")]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        message_id = f"SL-{next_id_num:03d}"

        new_message = {
            "message_id": message_id,
            "timestamp": kwargs.get("timestamp"),
            "username": "RBAC_BOT",
            "message": kwargs.get("message"),
            "channel": kwargs.get("channel"),
            "reply_to_message_id": kwargs.get("reply_to_message_id", None) # Optional for threading
        }

        slack_messages.append(new_message)
        data['slack_messages'] = slack_messages

        return json.dumps({
            "message": "Slack message sent successfully.",
            "message_details": new_message
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "send_slack_message",
                "description": "Sends a message to a specified Slack channel. Can be used to post new messages or reply to existing ones.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel": {
                            "type": "string",
                            "description": "The channel to post the message in (e.g., '#access-requests')."
                        },
                        "message": {
                            "type": "string",
                            "description": "The content of the message to be sent."
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp for the message record."
                        },
                        "reply_to_message_id": {
                            "type": "string",
                            "description": "Optional. The ID of the message to reply to, creating a thread."
                        }
                    },
                    "required": ["channel", "message", "timestamp"]
                }
            }
        }

class GetRoleDetailsById(Tool):
    """ Find a specific role using its ID. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role_id = kwargs.get("role_id")
        try:
            roles = data.get('roles', [])
        except:
            roles = []

        for role in roles:
            if role.get("role_id") == role_id:
                return json.dumps(role)

        return json.dumps({"error": f"Role with ID '{role_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_role_details_by_id",
                "description": "Retrieves the full details of a specific role by providing its unique role_id (e.g., 'ROL-013').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {
                            "type": "string",
                            "description": "The unique identifier of the role to retrieve (e.g., 'ROL-011')."
                        }
                    },
                    "required": ["role_id"]
                }
            }
        }

class FindResources(Tool):
    """ Find resources based on search criteria like name keywords, criticality, or owner ID. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name_keyword = kwargs.get("name_keyword")
        criticality = kwargs.get("criticality")
        owner_id = kwargs.get("owner_id")  # The ESSENTIAL new parameter

        try:
            resources = data.get('resources', [])
        except:
            resources = []

        matching_resources = []
        for resource in resources:
            if name_keyword and name_keyword.lower() not in resource.get("name", "").lower():
                continue
            if criticality and criticality.upper() != resource.get("criticality", "").upper():
                continue
            # This is the new, required logic
            if owner_id and owner_id != resource.get("owner_id"):
                continue
            matching_resources.append(resource)

        return json.dumps(matching_resources)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_resources",
                "description": "Searches for resources based on a combination of criteria. Returns a list of matching resources.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name_keyword": {"type": "string", "description": "A keyword to search for within the resource name."},
                        "criticality": {"type": "string", "description": "The criticality level to filter by."},
                        "owner_id": {"type": "string", "description": "The user ID of the resource owner to filter by."} # The new parameter info
                    },
                    "required": []
                }
            }
        }

class UpdateUserDepartment(Tool):
    """ Updates the 'department' field for a specific user in the database. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id_to_update = kwargs.get("user_id")
        new_department = kwargs.get("new_department")

        try:
            users = data.get('users', [])
        except (KeyError, json.JSONDecodeError):
            users = []

        user_to_update = None
        for user in users:
            if user.get("user_id") == user_id_to_update:
                user["department"] = new_department
                user_to_update = user
                break

        if not user_to_update:
            return json.dumps({"error": f"User with ID '{user_id_to_update}' not found."})

        data['users'] = users
        return json.dumps(user_to_update)

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
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user whose department needs to be updated."
                        },
                        "new_department": {
                            "type": "string",
                            "description": "The new department to assign to the user."
                        }
                    },
                    "required": ["user_id", "new_department"]
                }
            }
        }

class GetResourceByName(Tool):
    """Find a resource using its human-readable name."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        resource_name = kwargs.get("resource_name")
        try:
            all_resources = data.get('resources', [])
        except (KeyError, json.JSONDecodeError):
            all_resources = []

        for resource in all_resources:
            if resource.get("name") == resource_name:
                return json.dumps(resource)

        # 5. If no match is found after checking all resources, return an error message.
        return json.dumps({"error": f"Resource with name '{resource_name}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_resource_by_name",
                "description": "Retrieves the full details of a resource by searching for its exact name (e.g., 'sales-reporting-dashboard').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_name": {
                            "type": "string",
                            "description": "The unique, human-readable name of the resource."
                        }
                    },
                    "required": ["resource_name"]
                }
            }
        }

class GetHubspotTicketById(Tool):
    """ Get the full details of a specific HubSpot ticket using its ID. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ticket_id = kwargs.get("ticket_id")
        try:
            hubspot_tickets = data.get('hubspot_tickets', [])
        except:
            hubspot_tickets = []

        for ticket in hubspot_tickets:
            if ticket.get("ticket_id") == ticket_id:
                return json.dumps(ticket)

        return json.dumps({"error": f"HubSpot ticket with ID '{ticket_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_hubspot_ticket_by_id",
                "description": "Retrieves the full details of a specific HubSpot ticket using its unique ID (e.g., 'TI-053').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {
                            "type": "string",
                            "description": "The unique ID of the HubSpot ticket to retrieve."
                        }
                    },
                    "required": ["ticket_id"]
                }
            }
        }

class UpdateHubspotTicket(Tool):
    """ Updates an existing HubSpot ticket. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ticket_id= kwargs.get("ticket_id")
        try:
            hubspot_tickets = data.get('hubspot_tickets', [])
        except:
            hubspot_tickets = []

        ticket_to_update = None
        for ticket in hubspot_tickets:
            if ticket.get("ticket_id") == ticket_id:
                for key, value in kwargs.items():
                    if key in ticket:
                        ticket[key] = value
                ticket["updated_at"] = kwargs.get("timestamp") # Always update the timestamp
                ticket_to_update = ticket
                break

        if not ticket_to_update:
            return json.dumps({"error": f"HubSpot ticket with ID '{ticket_id}' not found."})

        data['hubspot_tickets'] = hubspot_tickets
        return json.dumps({
            "message": "HubSpot ticket updated successfully.",
            "ticket_details": ticket_to_update
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_hubspot_ticket",
                "description": "Updates an existing HubSpot ticket's status, description, or other fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {"type": "string", "description": "The ID of the ticket to update."},
                        "status": {"type": "string", "description": "The new status for the ticket (e.g., 'CLOSED')."},
                        "description": {"type": "string", "description": "The updated, detailed description of the issue or event."},
                        "closed_at": {"type": "string", "description": "The timestamp when the ticket was closed."},
                        "timestamp": {"type": "string", "description": "The current timestamp for the update record."}
                    },
                    "required": ["ticket_id", "timestamp"]
                }
            }
        }

class RevokePolicyException(Tool):
    """ Revokes an active policy exception, setting its status to 'REVOKED'. """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        exception_id = kwargs.get("exception_id")
        try:
            policy_exceptions = data.get('policy_exceptions', [])
        except:
            policy_exceptions = []

        exception_found = False
        for exc in policy_exceptions:
            if exc.get("exception_id") == exception_id:
                exc["status"] = "REVOKED"
                exception_found = True
                break
        
        if not exception_found:
            return json.dumps({"error": f"Policy exception with ID '{exception_id}' not found."})

        data['policy_exceptions'] = policy_exceptions
        return json.dumps({"message": "Policy exception revoked successfully.", "exception_id": exception_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "revoke_policy_exception",
                "description": "Revokes an active policy exception as a remediation action.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {"type": "string", "description": "The ID of the policy exception to revoke."}
                    },
                    "required": ["exception_id"]
                }
            }
        }

class GetPolicyExceptionById(Tool):
    """ Get the full details of a specific policy exception using its ID. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        exception_id = kwargs.get("exception_id")
        try:
            policy_exceptions = data.get('policy_exceptions', [])
        except:
            policy_exceptions = []

        for exc in policy_exceptions:
            if exc.get("exception_id") == exception_id:
                return json.dumps(exc)

        return json.dumps({"error": f"Policy exception with ID '{exception_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_policy_exception_by_id",
                "description": "Retrieves the full details of a specific policy exception using its unique ID (e.g., 'PE-010').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {
                            "type": "string",
                            "description": "The unique ID of the policy exception to retrieve."
                        }
                    },
                    "required": ["exception_id"]
                }
            }
        }
    
class GetPolicyExceptionByUserId(Tool):
    """Finds all policy exceptions for a specific user, with an option to include inactive ones."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        include_inactive = kwargs.get("include_inactive", False) 
        
        terminal_statuses = {"REVOKED", "REJECTED", "EXPIRED"}
        try:
            policy_exceptions = data.get('policy_exceptions', [])
        except:
            policy_exceptions = []

        user_exceptions = []
        for exc in policy_exceptions:
            if exc.get("user_id") == user_id:
                if include_inactive:
                    user_exceptions.append(exc)
                elif exc.get("status") not in terminal_statuses:
                    user_exceptions.append(exc)
        
        return json.dumps(user_exceptions)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_policy_exception_by_user_id",
                "description": "Retrieves a list of policy exceptions for a given user ID. By default, it only returns active exceptions.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The ID of the user to find exceptions for."},
                        "include_inactive": {"type": "boolean", "description": "Set to true to include expired, revoked, or rejected exceptions. Defaults to false."}
                    },
                    "required": ["user_id"]
                }
            }
        }

class FindRolesByResourceId(Tool):
    """ Finds all roles that grant permissions to a specific resource ID. """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        resource_id = kwargs.get("resource_id")
        try:
            role_permissions = data.get('role_permissions', [])
            permissions = data.get('permissions', [])
        except:
            return json.dumps({"error": "Data files not found."})

        perm_ids_for_resource = {p["permission_id"] for p in permissions if p.get("resource_id") == resource_id}

        if not perm_ids_for_resource:
            return json.dumps([])

        role_ids_for_resource = {rp["role_id"] for rp in role_permissions if rp.get("permission_id") in perm_ids_for_resource}
        
        return json.dumps(list(role_ids_for_resource))

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_roles_by_resource_id",
                "description": "Returns a list of role IDs that are associated with a given resource ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {"type": "string", "description": "The ID of the resource to find associated roles for."}
                    },
                    "required": ["resource_id"]
                }
            }
        }

class FindHubspotTicketByDescription(Tool):
    """Finds a HubSpot ticket by searching for a keyword in its description field."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        keyword = kwargs.get("keyword")
        try:
            tickets = data.get('hubspot_tickets', [])
        except (KeyError, json.JSONDecodeError):
            tickets = []

        for ticket in tickets:
            description = ticket.get("description", "")
            if description is None:
                description = ""
            
            if keyword in description:
                return json.dumps(ticket)

        return json.dumps({"error": f"No HubSpot ticket found with keyword '{keyword}' in its description."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_hubspot_ticket_by_description",
                "description": "Finds a HubSpot ticket by searching for a specific keyword within its description text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "keyword": {
                            "type": "string",
                            "description": "The keyword or string to search for in the ticket descriptions (e.g., an alert ID like 'ALRT-001')."
                        }
                    },
                    "required": ["keyword"]
                }
            }
        }
    
class GetPermissionById(Tool):
    """ Get the full details of a specific permission using its ID. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        permission_id = kwargs.get("permission_id")
        try:
            permissions = data.get('permissions', [])
        except (KeyError, json.JSONDecodeError):
            permissions = []

        for perm in permissions:
            if perm.get("permission_id") == permission_id:
                return json.dumps(perm)

        return json.dumps({"error": f"Permission with ID '{permission_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_permission_by_id",
                "description": "Retrieves the full details of a specific permission (action, resource_id) using its unique permission_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "permission_id": {
                            "type": "string",
                            "description": "The unique ID of the permission to retrieve (e.g., 'P-021')."
                        }
                    },
                    "required": ["permission_id"]
                }
            }
        }

class FindResourcesByRoleId(Tool):
    """Finds all resource IDs that a specific role grants permissions to."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        role_id = kwargs.get("role_id")
        try:
            role_permissions = data.get('role_permissions', [])
            permissions = data.get('permissions', [])
        except:
            return json.dumps({"error": "Data files not found."})

        perm_ids_for_role = {
            rp["permission_id"] for rp in role_permissions if rp.get("role_id") == role_id
        }

        if not perm_ids_for_role:
            return json.dumps([])

        resource_ids = {
            p["resource_id"] for p in permissions if p.get("permission_id") in perm_ids_for_role
        }
        
        return json.dumps(list(resource_ids))

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_resources_by_role_id",
                "description": "Returns a list of all unique resource IDs that a specific role has permissions for.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "role_id": {"type": "string", "description": "The ID of the role to find associated resources for."}
                    },
                    "required": ["role_id"]
                }
            }
        }

class GetSessionDetailsById(Tool):
    """Get the full details of a specific session using its ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        session_id = kwargs.get("session_id")
        try:
            sessions = data.get('sessions', [])
        except (KeyError, json.JSONDecodeError):
            sessions = []

        for session in sessions:
            if session.get("session_id") == session_id:
                return json.dumps(session)

        return json.dumps({"error": f"Session with ID '{session_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_session_details_by_id",
                "description": "Retrieves the full details of a specific user session using its unique ID (e.g., 'S-028').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "session_id": {
                            "type": "string",
                            "description": "The unique ID of the session to retrieve."
                        }
                    },
                    "required": ["session_id"]
                }
            }
        }
    
class CheckUserSessionsById(Tool):
    """Finds all recent login sessions for a specific user to aid in security investigations."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id_to_find = kwargs.get("user_id")
        try:
            all_sessions = data.get('sessions', [])
        except (KeyError, json.JSONDecodeError):
            all_sessions = []

        user_sessions = [
            session for session in all_sessions
            if session.get("user_id") == user_id_to_find
        ]
        return json.dumps(user_sessions)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_user_sessions_by_id",
                "description": "Retrieves a list of all recent login sessions for a specific user ID as part of a security investigation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user whose sessions are to be checked."
                        }
                    },
                    "required": ["user_id"]
                }
            }
        }
    
class UpdateResourceOwner(Tool):
    """ Updates the 'owner_id' field for a specific resource in the database. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        resource_id_to_update = kwargs.get("resource_id")
        new_owner_id = kwargs.get("new_owner_id")

        try:
            resources = data.get('resources', [])
        except (KeyError, json.JSONDecodeError):
            resources = []

        resource_to_update = None
        for resource in resources:
            if resource.get("resource_id") == resource_id_to_update:
                resource["owner_id"] = new_owner_id
                resource_to_update = resource
                break

        if not resource_to_update:
            return json.dumps({"error": f"Resource with ID '{resource_id_to_update}' not found."})

        data['resources'] = resources
        return json.dumps({
            "message": "Resource owner updated successfully.",
            "resource_details": resource_to_update
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_resource_owner",
                "description": "Updates the owner of a specific resource.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {
                            "type": "string",
                            "description": "The unique ID of the resource whose owner needs to be updated."
                        },
                        "new_owner_id": {
                            "type": "string",
                            "description": "The user ID of the new owner for the resource."
                        }
                    },
                    "required": ["resource_id", "new_owner_id"]
                }
            }
        }

class UpdateAccessRequest(Tool):
    """Updates an existing access request, used for rerouting or corrections."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        request_id = kwargs.get("request_id")
        new_reviewer_id = kwargs.get("new_reviewer_id")
        new_status = kwargs.get("new_status")

        for req in data.get('access_requests', []):
            if req.get("request_id") == request_id:
                if new_reviewer_id:
                    req["reviewer_id"] = new_reviewer_id
                if new_status:
                    req["status"] = new_status
                req["decision_at"] = kwargs.get("timestamp") 
                return json.dumps({"status": "success", "updated_request_id": request_id})
        
        return json.dumps({"status": "error", "message": "Request not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_access_request",
                "description": "Updates an existing access request. Primarily used to reroute a request to a new approver by changing the reviewer_id and resetting the status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string", "description": "The ID of the access request to update."},
                        "new_reviewer_id": {"type": "string", "description": "The user_id of the new approver to assign the request to."},
                        "new_status": {"type": "string", "description": "The new status for the request, e.g., 'PENDING'."},
                        "timestamp": {"type": "string", "description": "The timestamp of the update action."}
                    },
                    "required": ["request_id"]
                }
            }
        }

class FindAccessRequestsByUserId(Tool):
    """Finds all access requests submitted by a specific user."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id_to_find = kwargs.get("user_id")
        try:
            all_requests = data.get('access_requests', [])
        except (KeyError, json.JSONDecodeError):
            all_requests = []

        user_requests = [
            request for request in all_requests
            if request.get("user_id") == user_id_to_find
        ]
        return json.dumps(user_requests)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_access_requests_by_user_id",
                "description": "Retrieves a list of all historical access requests submitted by a specific user, which can then be reviewed for patterns.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user whose access requests are to be retrieved."
                        }
                    },
                    "required": ["user_id"]
                }
            }
        }
    
class GetPermissionByResourceId(Tool):
    """Finds all permissions associated with a specific resource ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        resource_id_to_find = kwargs.get("resource_id")
        try:
            all_permissions = data.get('permissions', [])
        except (KeyError, json.JSONDecodeError):
            return json.dumps([])

        matching_permissions = [
            perm for perm in all_permissions
            if perm.get("resource_id") == resource_id_to_find
        ]

        return json.dumps(matching_permissions)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_permission_by_resource_id",
                "description": "Retrieves a list of all permissions that are directly associated with a specific resource ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "resource_id": {
                            "type": "string",
                            "description": "The unique ID of the resource to find permissions for (e.g., 'RES-032')."
                        }
                    },
                    "required": ["resource_id"]
                }
            }
        }
    
class GetUserRoleDetailsByUserRoleId(Tool):
    """ Retrieves the details of a specific user role assignment by its user_role_id. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_role_id = kwargs.get("user_role_id")
        try:
            user_roles = data.get("user_roles", [])
        except:
            user_roles = []

        for user_role in user_roles:
            if user_role.get("user_role_id") == user_role_id:
                return json.dumps(user_role)

        return json.dumps({"error": f"User role with ID \'{user_role_id}\' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_role_details_by_user_role_id",
                "description": "Retrieves the full details of a specific user role assignment by its user_role_id (e.g., \'UR-029\').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_role_id": {
                            "type": "string",
                            "description": "The unique identifier of the user role assignment to retrieve (e.g., \'UR-029\')."
                        }
                    },
                    "required": ["user_role_id"]
                }
            }
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
