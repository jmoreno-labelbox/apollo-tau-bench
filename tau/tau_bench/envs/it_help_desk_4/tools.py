import json
from typing import Any

from tau_bench.envs.tool import Tool

FIXED_NOW = "2025-08-15T13:00:00Z"




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db


def _get_table(data: dict[str, Any], name: str) -> list[dict[str, Any]]:
    """Get table from data and convert from dict to list if needed."""
    table = data.get(name, [])
    return _convert_db_to_list(table)


def _get_next_id(table: list[dict[str, Any]], key: str, prefix: str) -> str:
    pass
    if not table:
        return f"{prefix}_00001"
    max_id = 0
    for item in table:
        try:
            num = int(item[key].split("_")[-1])
            if num > max_id:
                max_id = num
        except (ValueError, IndexError):
            continue
    return f"{prefix}_{max_id + 1:05d}"


class GetUserByUpnOrHrId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_lookup: str = None) -> str:
        accounts = data.get("directory_accounts", {}).values()
        for acc in accounts.values():
            if (
                acc.get("hr_id") == user_lookup
                or acc.get("upn") == user_lookup
                or acc.get("employee_id") == user_lookup
            ):
                payload = acc
                out = json.dumps(payload, indent=2)
                return out
        payload = {"user_lookup": user_lookup, "account": None}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserByUpnOrHrId",
                "description": "Retrieve a user's directory account using their UPN, HR ID, or Employee ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_lookup": {"type": "string"}},
                    "required": ["user_lookup"],
                },
            },
        }


class CreateDirectoryAccount(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        legal_name: str = None, 
        hr_id: str = None,
        department: Any = None,
        job_title: Any = None,
        default_email: str = None
    ) -> str:
        accounts = data.get("directory_accounts", {}).values()
        username = legal_name.lower().replace(" ", ".")
        upn = f"{username}@company.com"
        name_part = "".join(filter(str.isalnum, legal_name.split()[0])).lower()
        last_initial = legal_name.split()[-1][0].lower()
        hr_num = hr_id.split("-")[-1]
        account_id = f"acc_{name_part}{last_initial}{hr_num}"
        new_account = {
            "account_id": account_id,
            "employee_id": f"emp_{hr_num}",
            "hr_id": hr_id,
            "username": username,
            "upn": upn,
            "status": "enabled",
            "created_at": FIXED_NOW,
            "disabled_at": None,
        }
        _get_table(data, "accounts")[account_id] = new_account
        payload = new_account
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateDirectoryAccount",
                "description": "Create a new user account in the directory.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "legal_name": {"type": "string"},
                        "hr_id": {"type": "string"},
                        "department": {"type": "string"},
                        "job_title": {"type": "string"},
                    },
                    "required": ["legal_name", "hr_id", "department", "job_title"],
                },
            },
        }


class SetDirectoryAccountStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], account_id: str = None, status: str = None, department: Any = None) -> str:
        accounts = data.get("directory_accounts", {}).values()
        account = next((a for a in accounts.values() if a.get("account_id") == account_id), None)
        if not account:
            payload = {"error": f"Account {account_id} not found."}
            out = json.dumps(payload, indent=2)
            return out
        if status not in ["enabled", "disabled", "inactive"]:
            payload = {"error": "Status must be 'enabled', 'disabled', or 'inactive'."}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        account["status"] = status
        account["disabled_at"] = (
            FIXED_NOW if status in ["disabled", "inactive"] else None
        )
        payload = account
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetDirectoryAccountStatus",
                "description": "Enable or disable a user's directory account.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["account_id", "status"],
                },
            },
        }


class LookupRoleProfile(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], department: str = None, job_title: str = None) -> str:
        profiles = data.get("rbac_group_map", {}).values()
        profile = next(
            (
                p
                for p in profiles.values() if p.get("department") == department and p.get("job_title") == job_title
            ),
            None,
        )
        if not profile:
            payload = {"department": department, "job_title": job_title, "profile": None}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = profile
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LookupRoleProfile",
                "description": "Look up the role profile for a given department and job title to get group IDs and license bundles.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department": {"type": "string"},
                        "job_title": {"type": "string"},
                    },
                    "required": ["department", "job_title"],
                },
            },
        }


class AddUserToGroups(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], account_id: str, group_ids: list[str]) -> str:
        audit_log = _get_table(data, "group_membership_audit")
        added_groups = []
        for group_id in group_ids:
            audit_id = _get_next_id(audit_log, "audit_id", "gma")
            audit_log.append(
                {
                    "audit_id": audit_id,
                    "account_id": account_id,
                    "group_id": group_id,
                    "action": "add",
                    "actor": "SYSTEM",
                    "timestamp": FIXED_NOW,
                }
            )
            added_groups.append(group_id)
        payload = {
                "status": "success",
                "account_id": account_id,
                "groups_added": added_groups,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddUserToGroups",
                "description": "Add a user to a list of access groups and log the changes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string"},
                        "group_ids": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["account_id", "group_ids"],
                },
            },
        }


class CheckLicenseAvailability(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], license_id: str = None) -> str:
        inventory = data.get("license_inventory", {}).values()
        license_info = next(
            (lic for lic in inventory.values() if lic.get("license_id") == license_id), None
        )
        if not license_info:
            payload = {"error": f"License ID {license_id} not found in inventory."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        available = license_info.get("total_seats", 0) - license_info.get(
            "used_seats", 0
        )
        payload = {
                "license_id": license_id,
                "seats_available": available > 0,
                "available_count": available,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckLicenseAvailability",
                "description": "Check if there are available seats for a given license SKU.",
                "parameters": {
                    "type": "object",
                    "properties": {"license_id": {"type": "string"}},
                    "required": ["license_id"],
                },
            },
        }


class AssignLicense(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], account_id: str = None, employee_id: str = None, license_id: str = None) -> str:
        assignments = _get_table(data, "license_assignments")
        _id_var = _get_next_id(assignments, "assignment_id", "lca")
        new_assignment = {
            "assignment_id": assignment_id,
            "account_id": account_id,
            "employee_id": employee_id,
            "license_id": license_id,
            "status": "active",
            "assigned_at": FIXED_NOW,
        }
        _get_table(data, "license_assignments")[new_assignment["license_assignment_id"]] = new_assignment
        payload = new_assignment
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignLicense",
                "description": "Assign a single license to a user by creating an assignment record. Does not check availability.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                        "license_id": {"type": "string"},
                    },
                    "required": ["account_id", "employee_id", "license_id"],
                },
            },
        }


class UpdateLicenseInventory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], license_id: str = None, operation: str = None) -> str:
        inventory = data.get("license_inventory", {}).values()
        license_info = next(
            (lic for lic in inventory.values() if lic.get("license_id") == license_id), None
        )
        if not license_info:
            payload = {"error": f"License ID {license_id} not found in inventory."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        if operation == "increment":
            license_info["used_seats"] += 1
        elif operation == "decrement":
            license_info["used_seats"] = max(0, license_info.get("used_seats", 0) - 1)
        else:
            payload = {"error": "Operation must be 'increment' or 'decrement'."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {
                "license_id": license_id,
                "new_used_seats": license_info["used_seats"],
                "operation": operation,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateLicenseInventory",
                "description": "Atomically increment or decrement the used_seats count for a license in inventory.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "license_id": {"type": "string"},
                        "operation": {"type": "string"},
                    },
                    "required": ["license_id", "operation"],
                },
            },
        }


class FindAvailableAsset(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_type: str = None) -> str:
        assets = data.get("it_assets", {}).values()
        asset = next(
            (
                a
                for a in assets.values() if a.get("asset_type") == asset_type and a.get("status") == "in_stock"
            ),
            None,
        )
        if not asset:
            payload = {"asset_type": asset_type, "asset": None}
            out = json.dumps(payload, indent=2)
            return out
        payload = asset
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindAvailableAsset",
                "description": "Find an available IT asset of a specific type (e.g., 'laptop').",
                "parameters": {
                    "type": "object",
                    "properties": {"asset_type": {"type": "string"}},
                    "required": ["asset_type"],
                },
            },
        }


class AssignAsset(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_id: str = None, employee_id: str = None, timestamp: str = None) -> str:
        assets = data.get("it_assets", {}).values()
        asset = next((a for a in assets.values() if a.get("asset_id") == asset_id), None)
        if not asset:
            payload = {"error": f"Asset {asset_id} not found."}
            out = json.dumps(payload, indent=2)
            return out
        asset["assigned_to"] = employee_id
        asset["status"] = "READY FOR PICKUP"
        asset["mdm_enrolled"] = True
        payload = asset
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignAsset",
                "description": "Assign an IT asset to an employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                    },
                    "required": ["asset_id", "employee_id"],
                },
            },
        }


class CreateDeviceWorkflow(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str = None,
        asset_id: str = None,
        process: str = None,
        workflow_id: str = None,
        status: str = None,
        pickup_code: str = None,
        created_at: str = FIXED_NOW,
        completed_at: str = None
    ) -> str:
        if status is None:
            status = "pending_pickup" if process == "onboarding" else "pending_return"

        workflows = _get_table(data, "device_workflow")

        if not workflow_id:
            workflow_id = _get_next_id(workflows, "workflow_id", "dwf")
        if not pickup_code and process == "onboarding":
            pickup_code = f"PU{workflow_id[-4:]}"

        return_code = f"RT{workflow_id[-4:]}" if "offboarding" in process else None

        new_workflow = {
            "workflow_id": workflow_id,
            "employee_id": employee_id,
            "asset_id": asset_id,
            "process": process,
            "status": status,
            "pickup_code": pickup_code,
            "return_code": return_code,
            "created_at": created_at,
            "completed_at": completed_at,
        }
        workflows.append(new_workflow)
        payload = new_workflow
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateDeviceWorkflow",
                "description": "Create a device workflow entry for provisioning and pickup or for return.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "asset_id": {"type": "string"},
                        "process": {"type": "string"},
                    },
                    "required": ["employee_id", "asset_id", "process"],
                },
            },
        }


class CreateJiraTicket(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], issue_type: str = None, summary: str = None, priority: str = "P2") -> str:
        tickets = _get_table(data, "jira_tickets")
        jira_id = f"ITSD-{1001 + len(tickets)}"
        new_ticket = {
            "jira_id": jira_id,
            "issue_type": issue_type,
            "summary": summary,
            "priority": priority,
            "status": "To Do",
            "created_at": FIXED_NOW,
            "updated_at": FIXED_NOW,
        }
        _get_table(data, "tickets")[new_ticket["ticket_id"]] = new_ticket
        payload = new_ticket
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateJiraTicket",
                "description": "Create a Jira ticket for tracking issues.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "issue_type": {"type": "string"},
                        "summary": {"type": "string"},
                        "priority": {"type": "string"},
                    },
                    "required": ["issue_type", "summary"],
                },
            },
        }


class CreateAuditRecord(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        lifecycle_id: str,
        event: str,
        details: str,
        actor: str = "SYSTEM",
        timestamp: str = FIXED_NOW
    ) -> str:
        audit_table = _get_table(data, "lifecycle_audit")
        _id_var = _get_next_id(audit_table, "audit_id", "lcaud")
        audit_table.append(
            {
                "audit_id": audit_id,
                "lifecycle_id": lifecycle_id,
                "event": event,
                "details": details,
                "timestamp": timestamp,
                "actor": actor,
            }
        )
        payload = {"status": "success", "event_logged": event}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAuditRecord",
                "description": "Create a deterministic record in the lifecycle audit log.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lifecycle_id": {"type": "string"},
                        "event": {"type": "string"},
                        "details": {"type": "object"},
                        "actor": {"type": "string"},
                        "timestamp": {"type": "string"},
                    },
                    "required": [
                        "lifecycle_id",
                        "event",
                        "details",
                        "actor",
                        "timestamp",
                    ],
                },
            },
        }


class GetUserLicenseAssignments(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None) -> str:
        assignments = data.get("license_assignments", {}).values()
        user_licenses = [
            a
            for a in assignments.values() if a.get("employee_id") == employee_id and a.get("status") == "active"
        ]
        payload = user_licenses
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserLicenseAssignments",
                "description": "Get a list of all active license assignments for a given employee.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                },
            },
        }


class GetLicenseAssignmentByType(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, license_type: str = None) -> str:
        assignments = data.get("license_assignments", {}).values()
        assignment = next(
            (
                a
                for a in assignments.values() if a.get("employee_id") == employee_id
                and a.get("license_id") == license_type
                and a.get("status") == "active"
            ),
            None,
        )
        if not assignment:
            payload = {
                    "error": f"Active assignment for license {license_type} not found for employee {employee_id}."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = assignment
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getLicenseAssignmentByType",
                "description": "Get a specific active license assignment for a user by license ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "license_type": {"type": "string"},
                    },
                    "required": ["employee_id", "license_type"],
                },
            },
        }


class RevokeLicense(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], assignment_id: str = None) -> str:
        assignments = data.get("license_assignments", {}).values()
        assignment = next(
            (a for a in assignments.values() if a.get("assignment_id") == assignment_id), None
        )
        if not assignment:
            payload = {"error": f"Assignment {assignment_id} not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        assignment["status"] = "revoked"
        assignment["revoked_at"] = FIXED_NOW
        payload = assignment
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RevokeLicense",
                "description": "Revoke a user's license by updating its status. Does not check inventory.",
                "parameters": {
                    "type": "object",
                    "properties": {"assignment_id": {"type": "string"}},
                    "required": ["assignment_id"],
                },
            },
        }


class RemoveUserFromGroups(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], account_id: str, group_ids: list[str]) -> str:
        audit_log = _get_table(data, "group_membership_audit")
        removed_groups = []
        for group_id in group_ids:
            audit_id = _get_next_id(audit_log, "audit_id", "gma")
            audit_log.append(
                {
                    "audit_id": audit_id,
                    "account_id": account_id,
                    "group_id": group_id,
                    "action": "remove",
                    "actor": "SYSTEM",
                    "timestamp": FIXED_NOW,
                }
            )
            removed_groups.append(group_id)
        payload = {
                "status": "success",
                "account_id": account_id,
                "groups_removed": removed_groups,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveUserFromGroups",
                "description": "Remove a user from a list of access groups and log the changes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string"},
                        "group_ids": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["account_id", "group_ids"],
                },
            },
        }


class ArchiveMailbox(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str) -> str:
        mailboxes = data.get("mailboxes", {}).values()
        archives = _get_table(data, "data_archives")
        mailbox = next(
            (m for m in mailboxes.values() if m.get("employee_id") == employee_id), None
        )
        if not mailbox:
            payload = {"error": f"Mailbox for employee {employee_id} not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        mailbox["status"] = "archived"
        archive_id = f"arch_{mailbox['mailbox_id'].split('_')[-1]}"
        new_archive = {
            "archive_id": archive_id,
            "employee_id": employee_id,
            "mailbox_id": mailbox["mailbox_id"],
            "archive_path": f"s3://corp-archives/mail/{employee_id}/{FIXED_NOW.split('T')[0]}",
            "retention_policy": mailbox["retention_policy"],
            "created_at": FIXED_NOW,
        }
        _get_table(data, "archives")[archive_id] = new_archive
        payload = new_archive
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ArchiveMailbox",
                "description": "Archives a user's mailbox and creates a data archive record.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                },
            },
        }


class GetUserAsset(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None) -> str:
        assets = data.get("it_assets", {}).values()
        asset = next((a for a in assets.values() if a.get("assigned_to") == employee_id), None)
        if not asset:
            payload = {"employee_id": employee_id, "asset": None}
            out = json.dumps(payload, indent=2)
            return out
        payload = asset
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserAsset",
                "description": "Find an IT asset assigned to a specific employee.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                },
            },
        }


class ExportServiceDeskTickets(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], start_date: str = None, end_date: str = None, export_path: str = None) -> str:
        tickets = data.get("tickets", {}).values()
        payload = {
                "export_path": export_path,
                "ticket_count": len(tickets),
                "start_date": start_date,
                "end_date": end_date,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "exportServiceDeskTickets",
                "description": "Export service desk tickets within a date range to CSV.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"},
                        "export_path": {"type": "string"},
                    },
                    "required": ["start_date", "end_date", "export_path"],
                },
            },
        }


class NormalizeTicketTimestamps(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], input_path: str = None, output_path: str = None, timezone: str = "UTC") -> str:
        payload = {
            "status": "normalized",
            "input_path": input_path,
            "output_path": output_path,
            "timezone": timezone,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "normalizeTicketTimestamps",
                "description": "Normalize ticket timestamps to specified timezone.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "input_path": {"type": "string"},
                        "output_path": {"type": "string"},
                        "timezone": {"type": "string"},
                    },
                    "required": ["input_path", "output_path"],
                },
            },
        }


class CalculateServiceDeskKPIs(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], input_path: str = None, metrics: Any = None, output_path: str = None) -> str:
        kpis = {
            "total_open": 46,
            "avg_age_open_hours": 23.5,
            "avg_ttr_mins": 1440,
            "pct_closed_1d": 60.0,
            "p1_open_count": 5,
        }
        payload = {"kpis": kpis, "output_path": output_path}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculateServiceDeskKpis",
                "description": "Calculate service desk KPIs from ticket data.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "input_path": {"type": "string"},
                        "metrics": {"type": "array", "items": {"type": "string"}},
                        "output_path": {"type": "string"},
                    },
                    "required": ["input_path", "metrics", "output_path"],
                },
            },
        }


class GenerateReportPDF(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], kpi_data_path: str = None, template_path: str = None, output_path: str = None) -> str:
        payload = {"status": "generated", "output_path": output_path}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generateReportPdf",
                "description": "Generate a PDF report from KPI data using a template.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "kpi_data_path": {"type": "string"},
                        "template_path": {"type": "string"},
                        "output_path": {"type": "string"},
                    },
                    "required": ["kpi_data_path", "template_path", "output_path"],
                },
            },
        }


class SaveMetricsToDatabase(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], metrics_path: str = None, database_table: str = None, report_date: str = None) -> str:
        metrics_db = _get_table(data, "daily_metrics")
        run_id = f"run_{report_date.replace('-', '')}"
        new_metric = {
            "run_id": run_id,
            "report_date": report_date,
            "database_table": database_table,
        }
        metrics_db[run_id] = new_metric
        payload = {"status": "success", "run_id": run_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "saveMetricsToDatabase",
                "description": "Save calculated metrics to database.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "metrics_path": {"type": "string"},
                        "database_table": {"type": "string"},
                        "report_date": {"type": "string"},
                    },
                    "required": ["metrics_path", "database_table", "report_date"],
                },
            },
        }


class NotifyManagementTeam(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], report_path: str = None, recipient_group: str = None, subject: str = None) -> str:
        pass
        payload = {
            "status": "notified",
            "recipient_group": recipient_group,
            "subject": subject,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "notifyManagementTeam",
                "description": "Send notification to management team with report.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_path": {"type": "string"},
                        "recipient_group": {"type": "string"},
                        "subject": {"type": "string"},
                    },
                    "required": ["report_path", "recipient_group", "subject"],
                },
            },
        }


class ExportRecentTickets(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], days: int = 30) -> str:
        tickets = data.get("tickets", {}).values()
        report_path = f"\\\\IT\\Reports\\DailyReports\\{FIXED_NOW.split('T')[0]}\\Tickets_Export.csv"
        payload = {"export_path": report_path, "ticket_count": len(tickets)}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ExportRecentTickets",
                "description": "Exports all tickets updated in the last N days to a CSV file.",
                "parameters": {
                    "type": "object",
                    "properties": {"days": {"type": "integer"}},
                    "required": ["days"],
                },
            },
        }


class CalculateTicketKPIs(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], export_path: str) -> str:
        if "Tickets_Export.csv" not in export_path:
            payload = {"error": "Invalid export path provided."}
            out = json.dumps(payload, indent=2)
            return out
        kpis = {
            "total_open": 46,
            "avg_age_open_hours": 23.5,
            "avg_ttr_mins": 1440,
            "pct_closed_1d": 60.0,
            "p1_open_count": 5,
        }
        payload = kpis
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateTicketKpis",
                "description": "Calculates standard service desk KPIs from a ticket export CSV.",
                "parameters": {
                    "type": "object",
                    "properties": {"export_path": {"type": "string"}},
                    "required": ["export_path"],
                },
            },
        }


class GenerateHealthReportPDF(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], kpis: dict[str, Any] = None) -> str:
        if not all(k in kpis for k in ["total_open", "avg_age_open_hours"]):
            payload = {
                "status": "failed",
                "reason": "KPI data is incomplete",
                "missing_fields": [
                    k for k in ["total_open", "avg_age_open_hours"] if k not in kpis
                ],
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        report_path = f"\\\\IT\\Reports\\DailyReports\\{FIXED_NOW.split('T')[0]}\\ServiceDesk_Health_Report.pdf"
        payload = {"report_path": report_path, "status": "generated"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateHealthReportPdf",
                "description": "Generates a PDF health report from calculated KPI data.",
                "parameters": {
                    "type": "object",
                    "properties": {"kpis": {"type": "object"}},
                    "required": ["kpis"],
                },
            },
        }


class SaveReportToMetricsDB(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        kpis: dict[str, Any],
        report_date: Any = None,
        timestamp: Any = None,
    ) -> str:
        report_date = FIXED_NOW.split("T")[0]
        metrics_db = _get_table(data, "daily_metrics")
        run_id = f"run_{report_date.replace('-', '')}"
        new_metric = {"run_id": run_id, "report_date": report_date, **kpis}
        metrics_db[run_id] = new_metric
        payload = {"status": "success", "run_id": run_id}
        out = json.dumps(payload, indent=2)
        return out
        
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SaveReportToMetricsDb",
                "description": "Saves the calculated daily KPIs to the historical metrics database.",
                "parameters": {
                    "type": "object",
                    "properties": {"kpis": {"type": "object"}},
                    "required": ["kpis"],
                },
            },
        }


class NotifyTeamOfReport(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], pdf_path: str = None, csv_path: str = None, report_date: Any = None) -> str:
        recipient = "it-management-dl@company.com"
        payload = {
                "status": "notified",
                "recipient": recipient,
                "attachments": [pdf_path, csv_path],
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "NotifyTeamOfReport",
                "description": "Sends an email notification with the generated reports as attachments.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pdf_path": {"type": "string"},
                        "csv_path": {"type": "string"},
                    },
                    "required": ["pdf_path", "csv_path"],
                },
            },
        }


class ScheduleDeviceReturn(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, asset_id: str = None) -> str:
        workflows = _get_table(data, "device_workflow")
        _id_var = _get_next_id(workflows, "workflow_id", "dwf")
        return_code = f"RT{workflow_id[-4:]}"
        new_workflow = {
            "workflow_id": workflow_id,
            "employee_id": employee_id,
            "asset_id": asset_id,
            "process": "device_return",
            "status": "pending_return",
            "return_code": return_code,
            "created_at": FIXED_NOW,
            "completed_at": None,
        }
        workflows.append(new_workflow)
        payload = new_workflow
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "scheduleDeviceReturn",
                "description": "Schedule device return for an employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "asset_id": {"type": "string"},
                    },
                    "required": ["employee_id", "asset_id"],
                },
            },
        }


class ReadOnboardingMemo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], memo_id: str = None) -> str:
        memo = next(
            (
                m
                for m in data.get("hr_memos", {}).values()
                if m.get("memo_id") == memo_id and m.get("type") == "onboarding"
            ),
            None,
        )
        if not memo:
            payload = {"error": f"Onboarding memo {memo_id} not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = memo
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "readOnboardingMemo",
                "description": "Reads and returns a specific onboarding memo from the HR memos table.",
                "parameters": {
                    "type": "object",
                    "properties": {"memo_id": {"type": "string"}},
                    "required": ["memo_id"],
                },
            },
        }


class ValidateMemoFields(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], memo: dict[str, Any] = None) -> str:
        required_fields = [
            "legal_name",
            "department",
            "job_title",
            "manager_id",
            "start_date",
        ]
        missing_fields = [field for field in required_fields.values() if field not in memo]
        if missing_fields:
            payload = {"is_valid": False, "missing_fields": missing_fields}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"is_valid": True, "missing_fields": []}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "validateMemoFields",
                "description": "Validates that a parsed HR memo contains all required fields for onboarding.",
                "parameters": {
                    "type": "object",
                    "properties": {"memo": {"type": "object"}},
                    "required": ["memo"],
                },
            },
        }


class CreateMailbox(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, upn: str = None) -> str:
        mailboxes = _get_table(data, "mailboxes")
        _id_var = _get_next_id(mailboxes, "mailbox_id", "mbx")
        new_mailbox = {
            "mailbox_id": mailbox_id,
            "employee_id": employee_id,
            "address": upn,
            "status": "active",
            "retention_policy": "std_2y",
            "created_at": FIXED_NOW,
        }
        _get_table(data, "mailboxes")[new_mailbox["mailboxe_id"]] = new_mailbox
        payload = new_mailbox
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createMailbox",
                "description": "Creates an Exchange Online mailbox for a new user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "upn": {"type": "string"},
                    },
                    "required": ["employee_id", "upn"],
                },
            },
        }


class EnrollDeviceInMDM(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_id: str = None) -> str:
        asset = next(
            (a for a in data.get("it_assets", {}).values() if a.get("asset_id") == asset_id),
            None,
        )
        if asset:
            asset["mdm_enrolled"] = True
            payload = {"asset_id": asset_id, "enrollment_status": "success"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"error": f"Asset {asset_id} not found for MDM enrollment."}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "enrollDeviceInMdm",
                "description": "Enrolls a specified IT asset into the Mobile Device Management system.",
                "parameters": {
                    "type": "object",
                    "properties": {"asset_id": {"type": "string"}},
                    "required": ["asset_id"],
                },
            },
        }


class SendNewHireWelcomeEmail(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], upn: str = None, personal_email: str = None, pickup_code: str = None) -> str:
        payload = {
            "status": "sent",
            "recipients": [upn, personal_email],
            "pickup_code": pickup_code,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "sendNewHireWelcomeEmail",
                "description": "Sends a welcome email to the new hire's company and personal addresses with device pickup information.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "upn": {"type": "string"},
                        "personal_email": {"type": "string"},
                        "pickup_code": {"type": "string"},
                    },
                    "required": ["upn", "personal_email", "pickup_code"],
                },
            },
        }


class NotifyManager(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], manager_id: str = None, subject: str = None, body: str = None) -> str:
        payload = {"status": "sent", "recipient_manager_id": manager_id, "subject": subject}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "notifyManager",
                "description": "Sends a notification email to a manager for onboarding or offboarding events.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "manager_id": {"type": "string"},
                        "subject": {"type": "string"},
                        "body": {"type": "string"},
                    },
                    "required": ["manager_id", "subject", "body"],
                },
            },
        }


class AddMemoToLifecycleQueue(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], memo_id: str = None, hr_id: str = None, event_type: str = None) -> str:
        queue = _get_table(data, "lifecycle_queue")
        _id_var = _get_next_id(queue, "lifecycle_id", "lcq")
        new_entry = {
            "lifecycle_id": lifecycle_id,
            "memo_id": memo_id,
            "employee_ref": hr_id,
            "event": event_type,
            "status": "queued",
            "created_at": FIXED_NOW,
        }
        _get_table(data, "lifecycle_queue")[new_entry["lifecycle_queue_id"]] = new_entry
        payload = new_entry
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddMemoToLifecycleQueue",
                "description": "Adds a new memo to the lifecycle queue to initiate a process like onboarding or offboarding.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "memo_id": {"type": "string"},
                        "hr_id": {"type": "string"},
                        "event_type": {"type": "string"},
                    },
                    "required": ["memo_id", "hr_id", "event_type"],
                },
            },
        }


class CalculateTicketMetrics(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], tickets: list[dict[str, Any]]) -> str:
        pass
        calculated_tickets = []
        for ticket in tickets.values():
            ticket["age_hours"] = 72  # Simulated computation
            ticket["ttr_mins"] = 240  # Simulated computation
            calculated_data["tickets"][ticket["ticket_id"]] = ticket
        payload = calculated_tickets
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculateTicketMetrics",
                "description": "Calculates metrics like age and time-to-resolution for a list of tickets.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tickets": {"type": "array", "items": {"type": "object"}}
                    },
                    "required": ["tickets"],
                },
            },
        }


class AggregateTicketKPIs(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], tickets_with_metrics: list = None) -> str:
        tickets_with_metrics = tickets_with_metrics or []
        kpis = {
            "open_count": len(tickets_with_metrics),
            "open_count_p1": 5,
            "avg_age_open_hours": 72.5,
            "avg_ttr_mins": 240.0,
            "pct_closed_1d": 50.0,
        }
        payload = kpis
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "aggregateTicketKpis",
                "description": "Aggregates final KPIs from a list of tickets with pre-calculated metrics.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tickets_with_metrics": {
                            "type": "array",
                            "items": {"type": "object"},
                        }
                    },
                    "required": ["tickets_with_metrics"],
                },
            },
        }


class GetUserGroupMemberships(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], account_id: str = None) -> str:
        account = next(
            (
                a
                for a in data.get("directory_accounts", {}).values()
                if a.get("account_id") == account_id
            ),
            None,
        )
        if account and "group_ids" in account:
            payload = {"account_id": account_id, "group_ids": account["group_ids"]}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"account_id": account_id, "group_ids": []}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserGroupMemberships",
                "description": "Takes a snapshot of a user's current access groups for auditing.",
                "parameters": {
                    "type": "object",
                    "properties": {"account_id": {"type": "string"}},
                    "required": ["account_id"],
                },
            },
        }


class ScheduleDeviceMDMRemoval(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_id: str = None, last_day: str = None) -> str:
        payload = {
            "asset_id": asset_id,
            "removal_scheduled_for": last_day,
            "status": "pending_removal",
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "scheduleDeviceMdmRemoval",
                "description": "Schedules a device for removal from MDM on a specific date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_id": {"type": "string"},
                        "last_day": {"type": "string"},
                    },
                    "required": ["asset_id", "last_day"],
                },
            },
        }


class ArchiveUserAppAccounts(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None) -> str:
        app_accounts = data.get("app_accounts", {}).values()
        archived_count = 0
        for acc in app_accounts.values():
            if acc.get("employee_id") == employee_id:
                acc["status"] = "archived"
                archived_count += 1
        payload = {"employee_id": employee_id, "app_accounts_archived": archived_count}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "archiveUserAppAccounts",
                "description": "Archives a user's accounts in integrated applications like Slack or GitHub.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                },
            },
        }


class UpdateLifecycleQueueStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], lifecycle_id: str = None, status: str = None) -> str:
        queue = data.get("lifecycle_queue", {}).values()
        entry = next((e for e in queue.values() if e.get("lifecycle_id") == lifecycle_id), None)
        if not entry:
            payload = {"error": f"Lifecycle entry {lifecycle_id} not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        entry["status"] = status
        payload = entry
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateLifecycleQueueStatus",
                "description": "Updates the status of an event in the lifecycle queue (e.g., to 'completed').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lifecycle_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["lifecycle_id", "status"],
                },
            },
        }


class ReadOffboardingMemo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], memo_id: str = None) -> str:
        memo = next(
            (
                m
                for m in data.get("hr_memos", {}).values()
                if m.get("memo_id") == memo_id and m.get("type") == "offboarding"
            ),
            None,
        )
        if not memo:
            payload = {"error": f"Offboarding memo {memo_id} not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = memo
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "readOffboardingMemo",
                "description": "Reads and returns a specific offboarding memo from the HR memos table.",
                "parameters": {
                    "type": "object",
                    "properties": {"memo_id": {"type": "string"}},
                    "required": ["memo_id"],
                },
            },
        }


class CreateDataArchiveEntry(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, system: str = None, 
               retention_label: str = None, location_uri: str = None) -> str:
        archives = _get_table(data, "data_archives")
        _id_var = _get_next_id(archives, "archive_id", "arch")
        new_archive = {
            "archive_id": archive_id,
            "employee_id": employee_id,
            "system": system,
            "location_uri": location_uri,
            "retention_label": retention_label,
            "created_at": FIXED_NOW,
        }
        _get_table(data, "archives")[archive_id] = new_archive
        payload = new_archive
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createDataArchiveEntry",
                "description": "Creates an entry in the data archives table, typically after a mailbox export.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "system": {"type": "string"},
                        "retention_label": {"type": "string"},
                        "location_uri": {"type": "string"},
                    },
                    "required": [
                        "employee_id",
                        "system",
                        "retention_label",
                        "location_uri",
                    ],
                },
            },
        }


class FilterOpenTickets(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        tickets = data.get("tickets", {}).values()
        open_statuses = ["New", "In Progress", "On Hold", "Open"]
        open_tickets = [t for t in tickets.values() if t.get("status") in open_statuses]
        payload = open_tickets
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "filterOpenTickets",
                "description": "Filters a list of tickets to return only those that are not resolved or closed.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class BuildOpenTicketsCSV(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], open_tickets: list) -> str:
        file_path = f"\\\\IT\\Reports\\DailyReports\\{FIXED_NOW.split('T')[0]}\\Open_Tickets.csv"
        payload = {"file_path": file_path, "rows_written": len(open_tickets)}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "buildOpenTicketsCsv",
                "description": "Builds and saves the Open_Tickets.csv file from a list of open tickets.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "open_tickets": {"type": "array", "items": {"type": "object"}}
                    },
                    "required": ["open_tickets"],
                },
            },
        }


class UnassignAsset(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_id: str = None) -> str:
        assets = data.get("it_assets", {}).values()
        asset = next((a for a in assets.values() if a.get("asset_id") == asset_id), None)
        if not asset:
            payload = {"error": f"Asset {asset_id} not found."}
            out = json.dumps(payload, indent=2)
            return out
        asset["assigned_to"] = None
        asset["status"] = "in_stock"
        payload = asset
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UnassignAsset",
                "description": "Unassigns an IT asset from an employee and returns it to stock.",
                "parameters": {
                    "type": "object",
                    "properties": {"asset_id": {"type": "string"}},
                    "required": ["asset_id"],
                },
            },
        }


class GetLastReportRun(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        report_runs = data.get("report_runs", {}).values()
        if not report_runs:
            payload = {"error": "No previous report runs found."}
            out = json.dumps(payload, indent=2)
            return out
        last_run = report_runs[-1]
        #Simulating the KPIs that would have been recorded during the execution
        last_run["kpis"] = {
            "total_open": 45,
            "avg_age_open_hours": 22.0,
            "avg_ttr_mins": 1300,
            "pct_closed_1d": 65.0,
            "p1_open_count": 4,
        }
        payload = last_run
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetLastReportRun",
                "description": "Retrieves the data from the last successful service desk health report run.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }


class CompareTicketKPIs(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], current_kpis: dict[str, Any] = None, previous_kpis: dict[str, Any] = None) -> str:
        delta = {
            "total_open_delta": current_kpis.get("total_open", 0)
            - previous_kpis.get("total_open", 0),
            "p1_open_delta": current_kpis.get("p1_open_count", 0)
            - previous_kpis.get("p1_open_count", 0),
        }
        analysis_summary = f"KPI comparison complete. Open tickets changed by {delta['total_open_delta']}. P1 tickets changed by {delta['p1_open_delta']}."
        payload = {"analysis_summary": analysis_summary, "delta": delta}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CompareTicketKpis",
                "description": "Compares two sets of ticket KPIs to find the delta.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "current_kpis": {"type": "object"},
                        "previous_kpis": {"type": "object"},
                    },
                    "required": ["current_kpis", "previous_kpis"],
                },
            },
        }


def _find_all(collection: list[dict[str, Any]], **filters: Any) -> list[dict[str, Any]]:
    pass
    results = []
    for row in collection:
        ok = True
        for k, v in filters.items():
            if v is None:
                continue
            if isinstance(v, list):
                if row.get(k) not in v:
                    ok = False
                    break
            else:
                if row.get(k) != v:
                    ok = False
                    break
        if ok:
            results.append(row)
    return results


def _find_one(
    collection: list[dict[str, Any]], **filters: Any
) -> dict[str, Any] | None:
    pass
    for row in collection:
        if all(row.get(k) == v for k, v in filters.items()):
            return row
    return None


class GetEmployeeById(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str) -> str:
        emp = _find_one(_get_table(data, "employees"), employee_id=employee_id)
        payload = {"status": "ok", "employee": emp}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetEmployeeById",
                "description": "Retrieve a single employee record by employee_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                },
            },
        }


class GetDirectoryAccount(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str | None = None,
        account_id: str | None = None,
    ) -> str:
        acct = None
        if account_id:
            acct = _find_one(_get_table(data, "directory_accounts"), account_id=account_id)
        elif employee_id:
            acct = _find_one(_get_table(data, "directory_accounts"), employee_id=employee_id)
        payload = {"status": "ok", "account": acct}
        out = json.dumps(payload)
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDirectoryAccount",
                "description": "Get a directory account by employee_id or account_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "account_id": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class FindAssets(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        asset_type: str | None = None,
        status: str | None = None,
        model: str | None = None,
        assigned_to: str | None = None,
        mdm_enrolled: bool | None = None,
    ) -> str:
        results = []
        for a in _get_table(data, "it_assets").values():
            if asset_type and a["asset_type"] != asset_type:
                continue
            if status and a["status"] != status:
                continue
            if model and a["model"] != model:
                continue
            if assigned_to is not None and a.get("assigned_to") != assigned_to:
                continue
            if mdm_enrolled is not None and a.get("mdm_enrolled") != mdm_enrolled:
                continue
            results.append(a)
        payload = {"status": "ok", "assets": results}
        out = json.dumps(payload)
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindAssets",
                "description": "Find assets filtered by type, status, model, owner, or MDM enrolled flag.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_type": {"type": "string"},
                        "status": {"type": "string"},
                        "model": {"type": "string"},
                        "assigned_to": {"type": "string"},
                        "mdm_enrolled": {"type": "boolean"},
                    },
                    "required": [],
                },
            },
        }


class GetLicenseAssignments(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str | None = None,
        account_id: str | None = None,
    ) -> str:
        results: list[dict[str, Any]] = []
        for a in _get_table(data, "license_assignments").values():
            if employee_id and a["employee_id"] != employee_id:
                continue
            if account_id and a["account_id"] != account_id:
                continue
            results.append(a)
        payload = {"status": "ok", "assignments": results}
        out = json.dumps(payload)
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetLicenseAssignments",
                "description": "List license assignments filtered by employee_id or account_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "account_id": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class GetMailbox(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str | None = None,
        mailbox_id: str | None = None,
    ) -> str:
        mbx = None
        if mailbox_id:
            mbx = _find_one(_get_table(data, "mailboxes"), mailbox_id=mailbox_id)
        elif employee_id:
            mbx = _find_one(_get_table(data, "mailboxes"), employee_id=employee_id)
        payload = {"status": "ok", "mailbox": mbx}
        out = json.dumps(payload)
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getMailbox",
                "description": "Get a mailbox by employee_id or mailbox_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "mailbox_id": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


def _update_row(row: dict[str, Any], updates: dict[str, Any]) -> None:
    pass
    for k, v in updates.items():
        row[k] = v


def _append_row(table: list[dict[str, Any]], row: dict[str, Any]) -> None:
    pass
    table.append(row)


class RequestAssetReturn(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        asset_id: str,
        employee_id: str,
        due_ts: str,
        workflow_id: str,
    ) -> str:
        row = {
            "workflow_id": workflow_id,
            "employee_id": employee_id,
            "asset_id": asset_id,
            "process": "return",
            "status": "requested",
            "pickup_code": None,
            "created_at": due_ts,
            "completed_at": None,
        }
        _append_row(_get_table(data, "device_workflow"), row)
        payload = {"status": "ok", "workflow": row}
        out = json.dumps(payload)
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RequestAssetReturn",
                "description": "Create a device return request workflow entry with due timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                        "due_ts": {"type": "string"},
                        "workflow_id": {"type": "string"},
                    },
                    "required": ["asset_id", "employee_id", "due_ts", "workflow_id"],
                },
            },
        }


class UpdateAssetStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        asset_id: str,
        status: str,
        mdm_enrolled: bool | None = None,
    ) -> str:
        asset = _find_one(_get_table(data, "it_assets"), asset_id=asset_id)
        if not asset:
            payload = {"status": "error", "reason": "asset_not_found"}
            out = json.dumps(payload)
            return out
        asset["status"] = status
        if mdm_enrolled is not None:
            asset["mdm_enrolled"] = mdm_enrolled
        payload = {"status": "ok", "asset": asset}
        out = json.dumps(payload)
        return out
            

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAssetStatus",
                "description": "Update asset status and optionally its mdm_enrolled flag.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_id": {"type": "string"},
                        "status": {"type": "string"},
                        "mdm_enrolled": {"type": "boolean"},
                    },
                    "required": ["asset_id", "status"],
                },
            },
        }


class GetBaselineForRole(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], department: str, job_title: str) -> str:
        row = _find_one(
            _get_table(data, "rbac_group_map"), department=department, job_title=job_title
        )
        if not row:
            payload = {"status": "error", "reason": "rbac_baseline_not_found"}
            out = json.dumps(payload)
            return out
        payload = {
            "status": "ok",
            "group_ids": row.get("group_ids", []),
            "default_license_bundle": row.get("default_license_bundle", []),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetBaselineForRole",
                "description": "Return RBAC baseline group_ids and default license bundle for department/job_title.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department": {"type": "string"},
                        "job_title": {"type": "string"},
                    },
                    "required": ["department", "job_title"],
                },
            },
        }


class ScheduleMdmAction(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], asset_id: str, when: str, action: str, workflow_id: str
    ) -> str:
        row = {
            "workflow_id": workflow_id,
            "employee_id": None,
            "asset_id": asset_id,
            "process": action,
            "status": "scheduled",
            "pickup_code": None,
            "created_at": when,
            "completed_at": None,
        }
        _append_row(_get_table(data, "device_workflow"), row)
        payload = {"status": "ok", "workflow": row}
        out = json.dumps(payload)
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ScheduleMdmAction",
                "description": "Schedule an MDM action for an asset (stored as a workflow entry).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_id": {"type": "string"},
                        "when": {"type": "string"},
                        "action": {"type": "string"},
                        "workflow_id": {"type": "string"},
                    },
                    "required": ["asset_id", "when", "action", "workflow_id"],
                },
            },
        }


class EnqueueLifecycleEvent(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        lifecycle_id: str,
        memo_id: str,
        employee_ref: str,
        event: str,
        status: str,
        created_at: str,
    ) -> str:
        row = {
            "lifecycle_id": lifecycle_id,
            "memo_id": memo_id,
            "employee_ref": employee_ref,
            "event": event,
            "status": status,
            "created_at": created_at,
        }
        _append_row(_get_table(data, "lifecycle_queue"), row)
        _append_row(
            _get_table(data, "lifecycle_audit"),
            {
                "audit_id": f"lcaud_{lifecycle_id}_created",
                "lifecycle_id": lifecycle_id,
                "event": f"{event}_created",
                "timestamp": created_at,
                "actor": "system_policy",
            },
        )
        payload = {"status": "ok", "lifecycle": row}
        out = json.dumps(payload)
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EnqueueLifecycleEvent",
                "description": "Append a lifecycle_queue entry and a created audit record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lifecycle_id": {"type": "string"},
                        "memo_id": {"type": "string"},
                        "employee_ref": {"type": "string"},
                        "event": {"type": "string"},
                        "status": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": [
                        "lifecycle_id",
                        "memo_id",
                        "employee_ref",
                        "event",
                        "status",
                        "created_at",
                    ],
                },
            },
        }


class RecordLifecycleAudit(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], lifecycle_id: str, event: str, timestamp: str, actor: str
    ) -> str:
        row = {
            "audit_id": f"lcaud_{lifecycle_id}_{event}",
            "lifecycle_id": lifecycle_id,
            "event": event,
            "timestamp": timestamp,
            "actor": actor,
        }
        _append_row(_get_table(data, "lifecycle_audit"), row)
        payload = {"status": "ok", "audit": row}
        out = json.dumps(payload)
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordLifecycleAudit",
                "description": "Append a lifecycle_audit record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lifecycle_id": {"type": "string"},
                        "event": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "actor": {"type": "string"},
                    },
                    "required": ["lifecycle_id", "event", "timestamp", "actor"],
                },
            },
        }


class SetAccountGroups(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        account_id: str,
        group_ids: list[str],
        actor: str,
        timestamp: str,
    ) -> str:
        acct = _find_one(_get_table(data, "directory_accounts"), account_id=account_id)
        if not acct:
            payload = {"status": "error", "reason": "account_not_found"}
            out = json.dumps(payload)
            return out
        old = set(acct.get("group_ids", []))
        new = set(group_ids)
        to_add = sorted(list(new - old))
        to_remove = sorted(list(old - new))
        acct["group_ids"] = sorted(group_ids)
        if not to_add and not to_remove:
            _append_row(
                _get_table(data, "group_membership_audit"),
                {
                    "audit_id": f"gma_{account_id}_nochange_{timestamp}",
                    "account_id": account_id,
                    "group_id": None,
                    "action": "no_change",
                    "actor": actor,
                    "timestamp": timestamp,
                },
            )
        for gid in to_add:
            _append_row(
                _get_table(data, "group_membership_audit"),
                {
                    "audit_id": f"gma_{account_id}_{gid}_add_{timestamp}",
                    "account_id": account_id,
                    "group_id": gid,
                    "action": "add",
                    "actor": actor,
                    "timestamp": timestamp,
                },
            )
        for gid in to_remove:
            _append_row(
                _get_table(data, "group_membership_audit"),
                {
                    "audit_id": f"gma_{account_id}_{gid}_remove_{timestamp}",
                    "account_id": account_id,
                    "group_id": gid,
                    "action": "remove",
                    "actor": actor,
                    "timestamp": timestamp,
                },
            )
        payload = {"status": "ok", "account": acct, "added": to_add, "removed": to_remove}
        out = json.dumps(payload)
        return out
        

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setAccountGroups",
                "description": "Replace an account's groups and write add/remove entries to group_membership_audit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string"},
                        "group_ids": {"type": "array", "items": {"type": "string"}},
                        "actor": {"type": "string"},
                        "timestamp": {"type": "string"},
                    },
                    "required": ["account_id", "group_ids", "actor", "timestamp"],
                },
            },
        }


class EnsureLicenseCapacityOrOpenJira(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        license_id: str,
        needed_count: int,
        jira_id: str,
        priority: str,
        created_at: str,
    ) -> str:
        inv = _find_one(_get_table(data, "license_inventory"), license_id=license_id)
        if not inv:
            payload = {"status": "error", "reason": "license_not_found"}
            out = json.dumps(payload)
            return out
        if (
            inv["used_seats"] + inv["reserved_seats"] + needed_count
            <= inv["total_seats"]
        ):
            payload = {"status": "ok", "capacity": True}
            out = json.dumps(payload)
            return out
        jira = {
            "jira_id": jira_id,
            "issue_type": "License Shortage",
            "summary": f"License shortage for {license_id}",
            "priority": priority,
            "status": "To Do",
            "created_at": created_at,
            "updated_at": created_at,
        }
        _append_row(_get_table(data, "jira_tickets"), jira)
        payload = {"status": "ok", "capacity": False, "jira": jira}
        out = json.dumps(payload)
        return out
        

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ensureLicenseCapacityOrOpenJira",
                "description": "Check capacity for a license; otherwise create a TaskTrack 'License Shortage'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "license_id": {"type": "string"},
                        "needed_count": {"type": "integer"},
                        "jira_id": {"type": "string"},
                        "priority": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": [
                        "license_id",
                        "needed_count",
                        "jira_id",
                        "priority",
                        "created_at",
                    ],
                },
            },
        }


class UpdateLifecycleStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], lifecycle_id: str, status: str, timestamp: str, actor: str
    ) -> str:
        row = _find_one(_get_table(data, "lifecycle_queue"), lifecycle_id=lifecycle_id)
        if not row:
            payload = {"status": "error", "reason": "lifecycle_not_found"}
            out = json.dumps(payload)
            return out
        row["status"] = status
        _append_row(
            _get_table(data, "lifecycle_audit"),
            {
                "audit_id": f"lcaud_{lifecycle_id}_{status}",
                "lifecycle_id": lifecycle_id,
                "event": status,
                "timestamp": timestamp,
                "actor": actor,
            },
        )
        payload = {"status": "ok", "lifecycle": row}
        out = json.dumps(payload)
        return out
        

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateLifecycleStatus",
                "description": "Update lifecycle_queue status and append an audit row.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "lifecycle_id": {"type": "string"},
                        "status": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "actor": {"type": "string"},
                    },
                    "required": ["lifecycle_id", "status", "timestamp", "actor"],
                },
            },
        }


class UpsertAppAccount(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        app_account_id: str,
        employee_id: str,
        app_id: str,
        status: str,
        created_at: str,
    ) -> str:
        row = _find_one(_get_table(data, "app_accounts"), app_account_id=app_account_id)
        if row:
            _update_row(row, {"status": status})
        else:
            row = {
                "app_account_id": app_account_id,
                "employee_id": employee_id,
                "app_id": app_id,
                "status": status,
                "created_at": created_at,
            }
            _append_row(_get_table(data, "app_accounts"), row)
        payload = {"status": "ok", "app_account": row}
        out = json.dumps(payload)
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsertAppAccount",
                "description": "Create or update an app account for an employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "app_account_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                        "app_id": {"type": "string"},
                        "status": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": [
                        "app_account_id",
                        "employee_id",
                        "app_id",
                        "status",
                        "created_at",
                    ],
                },
            },
        }


TOOLS = [
    GetUserByUpnOrHrId(),
    CreateDirectoryAccount(),
    SetDirectoryAccountStatus(),
    LookupRoleProfile(),
    AddUserToGroups(),
    CheckLicenseAvailability(),
    AssignLicense(),
    UpdateLicenseInventory(),
    FindAvailableAsset(),
    AssignAsset(),
    CreateDeviceWorkflow(),
    CreateJiraTicket(),
    CreateAuditRecord(),
    GetUserLicenseAssignments(),
    GetLicenseAssignmentByType(),
    RevokeLicense(),
    RemoveUserFromGroups(),
    ArchiveMailbox(),
    GetUserAsset(),
    ExportRecentTickets(),
    CalculateTicketKPIs(),
    GenerateHealthReportPDF(),
    SaveReportToMetricsDB(),
    NotifyTeamOfReport(),
    ReadOnboardingMemo(),
    ValidateMemoFields(),
    CreateMailbox(),
    EnrollDeviceInMDM(),
    SendNewHireWelcomeEmail(),
    NotifyManager(),
    AddMemoToLifecycleQueue(),
    CalculateTicketMetrics(),
    AggregateTicketKPIs(),
    GetUserGroupMemberships(),
    ScheduleDeviceMDMRemoval(),
    ArchiveUserAppAccounts(),
    UpdateLifecycleQueueStatus(),
    ReadOffboardingMemo(),
    CreateDataArchiveEntry(),
    FilterOpenTickets(),
    BuildOpenTicketsCSV(),
    UnassignAsset(),
    GetLastReportRun(),
    CompareTicketKPIs(),
    GetEmployeeById(),
    GetDirectoryAccount(),
    FindAssets(),
    GetMailbox(),
    GetLicenseAssignments(),
    RequestAssetReturn(),
    UpdateAssetStatus(),
    GetBaselineForRole(),
    ScheduleMdmAction(),
    EnqueueLifecycleEvent(),
    RecordLifecycleAudit(),
    SetAccountGroups(),
    EnsureLicenseCapacityOrOpenJira(),
    UpdateLifecycleStatus(),
    UpsertAppAccount(),
]
