from typing import Dict, Any, List, Optional
import json

from domains.dto import Tool


def _find_one(collection: List[Dict[str, Any]], **filters: Any) -> Optional[Dict[str, Any]]:
    for row in collection:
        if all(row.get(k) == v for k, v in filters.items()):
            return row
    return None


def _find_all(collection: List[Dict[str, Any]], **filters: Any) -> List[Dict[str, Any]]:
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


def _append_row(table: List[Dict[str, Any]], row: Dict[str, Any]) -> None:
    table.append(row)


def _update_row(row: Dict[str, Any], updates: Dict[str, Any]) -> None:
    for k, v in updates.items():
        row[k] = v


class GetEmployeeById(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str) -> str:
        emp = _find_one(data["employees"], employee_id=employee_id)
        return json.dumps({"status": "ok", "employee": emp})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_employee_by_id",
                "description": "Retrieve a single employee record by employee_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                },
            },
        }


class FindEmployees(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        department: Optional[str] = None,
        job_title: Optional[str] = None,
        status: Optional[str] = None,
        manager_id: Optional[str] = None,
    ) -> str:
        results = _find_all(
            data["employees"],
            department=department,
            job_title=job_title,
            status=status,
            manager_id=manager_id,
        )
        return json.dumps({"status": "ok", "employees": results})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_employees",
                "description": "Find employees filtered by department, job_title, status, and/or manager_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department": {"type": "string"},
                        "job_title": {"type": "string"},
                        "status": {"type": "string"},
                        "manager_id": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class GetDirectoryAccount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: Optional[str] = None, account_id: Optional[str] = None) -> str:
        acct = None
        if account_id:
            acct = _find_one(data["directory_accounts"], account_id=account_id)
        elif employee_id:
            acct = _find_one(data["directory_accounts"], employee_id=employee_id)
        return json.dumps({"status": "ok", "account": acct})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_directory_account",
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


class CreateDirectoryAccount(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        account_id: str,
        employee_id: str,
        username: str,
        created_at: str,
        status: str = "enabled",
        group_ids: Optional[List[str]] = None,
    ) -> str:
        # Validate employee exists
        if not _find_one(data["employees"], employee_id=employee_id):
            _append_row(
                data["validation_issues"],
                {
                    "issue_id": f"vi_{account_id}",
                    "entity": "directory_accounts",
                    "entity_id": account_id,
                    "field": "employee_id",
                    "rule": "employee_must_exist",
                    "details": employee_id,
                    "created_at": created_at,
                },
            )
            return json.dumps({"status": "error", "reason": "employee_not_found"})

        row = {
            "account_id": account_id,
            "employee_id": employee_id,
            "username": username,
            "status": status,
            "group_ids": group_ids or [],
            "created_at": created_at,
            "disabled_at": None,
        }
        _append_row(data["directory_accounts"], row)
        return json.dumps({"status": "ok", "account": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_directory_account",
                "description": "Create a new directory account for an employee (deterministic IDs/timestamps provided by caller).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                        "username": {"type": "string"},
                        "created_at": {"type": "string"},
                        "status": {"type": "string"},
                        "group_ids": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["account_id", "employee_id", "username", "created_at"],
                },
            },
        }


class UpdateDirectoryAccountStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str, status: str, disabled_at: Optional[str] = None) -> str:
        acct = _find_one(data["directory_accounts"], account_id=account_id)
        if not acct:
            return json.dumps({"status": "error", "reason": "account_not_found"})
        if status not in {"enabled", "disabled"}:
            return json.dumps({"status": "error", "reason": "invalid_status"})
        acct["status"] = status
        acct["disabled_at"] = disabled_at
        return json.dumps({"status": "ok", "account": acct})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_directory_account_status",
                "description": "Set a directory account status to 'enabled' or 'disabled'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string"},
                        "status": {"type": "string"},
                        "disabled_at": {"type": "string"},
                    },
                    "required": ["account_id", "status"],
                },
            },
        }


class SetAccountGroups(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], account_id: str, group_ids: List[str], actor: str, timestamp: str
    ) -> str:
        acct = _find_one(data["directory_accounts"], account_id=account_id)
        if not acct:
            return json.dumps({"status": "error", "reason": "account_not_found"})
        old = set(acct.get("group_ids", []))
        new = set(group_ids)
        # compute diffs for audit
        to_add = sorted(list(new - old))
        to_remove = sorted(list(old - new))
        acct["group_ids"] = sorted(group_ids)
        if not to_add and not to_remove:
            # Even if no changes, policy implies an audit entry should be created for the action.
            _append_row(
                data["group_membership_audit"],
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
                data["group_membership_audit"],
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
                data["group_membership_audit"],
                {
                    "audit_id": f"gma_{account_id}_{gid}_remove_{timestamp}",
                    "account_id": account_id,
                    "group_id": gid,
                    "action": "remove",
                    "actor": actor,
                    "timestamp": timestamp,
                },
            )
        return json.dumps({"status": "ok", "account": acct, "added": to_add, "removed": to_remove})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_account_groups",
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


class AddAccountGroups(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str, group_ids: List[str], actor: str, timestamp: str) -> str:
        acct = _find_one(data["directory_accounts"], account_id=account_id)
        if not acct:
            return json.dumps({"status": "error", "reason": "account_not_found"})
        current = set(acct.get("group_ids", []))
        for gid in group_ids:
            if gid not in current:
                current.add(gid)
                _append_row(
                    data["group_membership_audit"],
                    {
                        "audit_id": f"gma_{account_id}_{gid}_add",
                        "account_id": account_id,
                        "group_id": gid,
                        "action": "add",
                        "actor": actor,
                        "timestamp": timestamp,
                    },
                )
        acct["group_ids"] = sorted(current)
        return json.dumps({"status": "ok", "account": acct})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_account_groups",
                "description": "Add groups to an account and append audit entries.",
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


class RemoveAccountGroups(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str, group_ids: List[str], actor: str, timestamp: str) -> str:
        acct = _find_one(data["directory_accounts"], account_id=account_id)
        if not acct:
            return json.dumps({"status": "error", "reason": "account_not_found"})
        current = set(acct.get("group_ids", []))
        for gid in group_ids:
            if gid in current:
                current.remove(gid)
                _append_row(
                    data["group_membership_audit"],
                    {
                        "audit_id": f"gma_{account_id}_{gid}_remove",
                        "account_id": account_id,
                        "group_id": gid,
                        "action": "remove",
                        "actor": actor,
                        "timestamp": timestamp,
                    },
                )
        acct["group_ids"] = sorted(current)
        return json.dumps({"status": "ok", "account": acct})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_account_groups",
                "description": "Remove groups from an account and append audit entries.",
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


class GetBaselineForRole(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], department: str, job_title: str) -> str:
        row = _find_one(data["rbac_group_map"], department=department, job_title=job_title)
        if not row:
            return json.dumps({"status": "error", "reason": "rbac_baseline_not_found"})
        return json.dumps(
            {
                "status": "ok",
                "group_ids": row.get("group_ids", []),
                "default_license_bundle": row.get("default_license_bundle", []),
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_baseline_for_role",
                "description": "Return RBAC baseline group_ids and default license bundle for department/job_title.",
                "parameters": {
                    "type": "object",
                    "properties": {"department": {"type": "string"}, "job_title": {"type": "string"}},
                    "required": ["department", "job_title"],
                },
            },
        }


class CreateMailbox(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        mailbox_id: str,
        employee_id: str,
        address: str,
        retention_policy: str,
        created_at: str,
        status: str = "active",
    ) -> str:
        if retention_policy not in {"std_2y", "finance_7y"}:
            return json.dumps({"status": "error", "reason": "invalid_retention"})
        row = {
            "mailbox_id": mailbox_id,
            "employee_id": employee_id,
            "address": address,
            "status": status,
            "retention_policy": retention_policy,
            "created_at": created_at,
        }
        _append_row(data["mailboxes"], row)
        return json.dumps({"status": "ok", "mailbox": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_mailbox",
                "description": "Create a mailbox with a fixed retention policy and status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "mailbox_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                        "address": {"type": "string"},
                        "retention_policy": {"type": "string"},
                        "created_at": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["mailbox_id", "employee_id", "address", "retention_policy", "created_at"],
                },
            },
        }


class UpdateMailboxStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], mailbox_id: str, status: str) -> str:
        mbx = _find_one(data["mailboxes"], mailbox_id=mailbox_id)
        if not mbx:
            return json.dumps({"status": "error", "reason": "mailbox_not_found"})
        if status not in {"active", "inactive"}:
            return json.dumps({"status": "error", "reason": "invalid_status"})
        mbx["status"] = status
        return json.dumps({"status": "ok", "mailbox": mbx})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_mailbox_status",
                "description": "Set mailbox status to active or inactive.",
                "parameters": {
                    "type": "object",
                    "properties": {"mailbox_id": {"type": "string"}, "status": {"type": "string"}},
                    "required": ["mailbox_id", "status"],
                },
            },
        }


class ArchiveMailbox(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        archive_id: str,
        mailbox_id: str,
        employee_id: str,
        archive_path: str,
        retention_policy: str,
        created_at: str,
    ) -> str:
        row = {
            "archive_id": archive_id,
            "employee_id": employee_id,
            "mailbox_id": mailbox_id,
            "archive_path": archive_path,
            "retention_policy": retention_policy,
            "created_at": created_at,
        }
        _append_row(data["data_archives"], row)
        return json.dumps({"status": "ok", "archive": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "archive_mailbox",
                "description": "Archive a mailbox to a storage path with retention policy.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "archive_id": {"type": "string"},
                        "mailbox_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                        "archive_path": {"type": "string"},
                        "retention_policy": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": ["archive_id", "mailbox_id", "employee_id", "archive_path", "retention_policy", "created_at"],
                },
            },
        }


class GetMailbox(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: Optional[str] = None, mailbox_id: Optional[str] = None) -> str:
        mbx = None
        if mailbox_id:
            mbx = _find_one(data["mailboxes"], mailbox_id=mailbox_id)
        elif employee_id:
            mbx = _find_one(data["mailboxes"], employee_id=employee_id)
        return json.dumps({"status": "ok", "mailbox": mbx})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_mailbox",
                "description": "Get a mailbox by employee_id or mailbox_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}, "mailbox_id": {"type": "string"}},
                    "required": [],
                },
            },
        }


class GetLicenseInventory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], license_id: Optional[str] = None) -> str:
        if license_id:
            row = _find_one(data["license_inventory"], license_id=license_id)
            return json.dumps({"status": "ok", "inventory": row})
        return json.dumps({"status": "ok", "inventory": data["license_inventory"]})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_license_inventory",
                "description": "Read license inventory optionally filtered by license_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"license_id": {"type": "string"}},
                    "required": [],
                },
            },
        }


class AssignLicense(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        assignment_id: str,
        account_id: str,
        employee_id: str,
        license_id: str,
        assigned_at: str,
    ) -> str:
        inv = _find_one(data["license_inventory"], license_id=license_id)
        if not inv:
            return json.dumps({"status": "error", "reason": "license_not_found"})
        if inv["used_seats"] + inv["reserved_seats"] + 1 > inv["total_seats"]:
            return json.dumps({"status": "error", "reason": "no_capacity"})

        # Directly modify the dictionary in the list
        for item in data["license_inventory"]:
            if item["license_id"] == license_id:
                item["used_seats"] += 1
                break

        row = {
            "assignment_id": assignment_id,
            "account_id": account_id,
            "employee_id": employee_id,
            "license_id": license_id,
            "status": "active",
            "assigned_at": assigned_at,
        }
        _append_row(data["license_assignments"], row)
        return json.dumps({"status": "ok", "assignment": row, "inventory": inv})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_license",
                "description": "Assign a license and increment used seats deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "assignment_id": {"type": "string"},
                        "account_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                        "license_id": {"type": "string"},
                        "assigned_at": {"type": "string"},
                    },
                    "required": ["assignment_id", "account_id", "employee_id", "license_id", "assigned_at"],
                },
            },
        }


class RevokeLicense(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str, employee_id: str, license_id: str, revoked_at: str) -> str:
        inv = _find_one(data["license_inventory"], license_id=license_id)
        if not inv:
            return json.dumps({"status": "error", "reason": "license_not_found"})
        # find active assignment
        row = None
        for a in data["license_assignments"]:
            if (
                a["account_id"] == account_id
                and a["employee_id"] == employee_id
                and a["license_id"] == license_id
                and a["status"] == "active"
            ):
                row = a
                break
        if not row:
            return json.dumps({"status": "error", "reason": "assignment_not_found"})
        row["status"] = "revoked"
        row["revoked_at"] = revoked_at
        if inv["used_seats"] > 0:
            inv["used_seats"] -= 1
        return json.dumps({"status": "ok", "assignment": row, "inventory": inv})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "revoke_license",
                "description": "Revoke an active license and decrement used seats.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                        "license_id": {"type": "string"},
                        "revoked_at": {"type": "string"},
                    },
                    "required": ["account_id", "employee_id", "license_id", "revoked_at"],
                },
            },
        }


class ReserveLicense(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], license_id: str, count: int, reason: str) -> str:
        inv = _find_one(data["license_inventory"], license_id=license_id)
        if not inv:
            return json.dumps({"status": "error", "reason": "license_not_found"})
        if inv["used_seats"] + inv["reserved_seats"] + count > inv["total_seats"]:
            return json.dumps({"status": "error", "reason": "no_capacity"})
        inv["reserved_seats"] += count
        return json.dumps({"status": "ok", "inventory": inv, "reason": reason})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "reserve_license",
                "description": "Reserve seats for a license (inventory reserved_seats).",
                "parameters": {
                    "type": "object",
                    "properties": {"license_id": {"type": "string"}, "count": {"type": "integer"}, "reason": {"type": "string"}},
                    "required": ["license_id", "count", "reason"],
                },
            },
        }


class ReleaseLicenseReservation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], license_id: str, count: int) -> str:
        inv = _find_one(data["license_inventory"], license_id=license_id)
        if not inv:
            return json.dumps({"status": "error", "reason": "license_not_found"})
        inv["reserved_seats"] = max(0, inv["reserved_seats"] - count)
        return json.dumps({"status": "ok", "inventory": inv})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "release_license_reservation",
                "description": "Release previously reserved license seats.",
                "parameters": {
                    "type": "object",
                    "properties": {"license_id": {"type": "string"}, "count": {"type": "integer"}},
                    "required": ["license_id", "count"],
                },
            },
        }


class EnsureLicenseCapacityOrOpenJira(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        license_id: str,
        needed_count: int,
        jira_id: str,
        priority: str,
        created_at: str,
    ) -> str:
        inv = _find_one(data["license_inventory"], license_id=license_id)
        if not inv:
            return json.dumps({"status": "error", "reason": "license_not_found"})
        if inv["used_seats"] + inv["reserved_seats"] + needed_count <= inv["total_seats"]:
            return json.dumps({"status": "ok", "capacity": True})
        # open jira and indicate block
        jira = {
            "jira_id": jira_id,
            "issue_type": "License Shortage",
            "summary": f"License shortage for {license_id}",
            "priority": priority,
            "status": "To Do",
            "created_at": created_at,
            "updated_at": created_at,
        }
        _append_row(data["jira_tickets"], jira)
        return json.dumps({"status": "ok", "capacity": False, "jira": jira})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ensure_license_capacity_or_open_jira",
                "description": "Check capacity for a license; otherwise create a Jira 'License Shortage'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "license_id": {"type": "string"},
                        "needed_count": {"type": "integer"},
                        "jira_id": {"type": "string"},
                        "priority": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": ["license_id", "needed_count", "jira_id", "priority", "created_at"],
                },
            },
        }


class GetLicenseAssignments(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: Optional[str] = None, account_id: Optional[str] = None) -> str:
        results: List[Dict[str, Any]] = []
        for a in data["license_assignments"]:
            if employee_id and a["employee_id"] != employee_id:
                continue
            if account_id and a["account_id"] != account_id:
                continue
            results.append(a)
        return json.dumps({"status": "ok", "assignments": results})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_license_assignments",
                "description": "List license assignments filtered by employee_id or account_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}, "account_id": {"type": "string"}},
                    "required": [],
                },
            },
        }


class FindAssets(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        asset_type: Optional[str] = None,
        status: Optional[str] = None,
        model: Optional[str] = None,
        assigned_to: Optional[str] = None,
        mdm_enrolled: Optional[bool] = None,
    ) -> str:
        results = []
        for a in data["it_assets"]:
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
        return json.dumps({"status": "ok", "assets": results})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_assets",
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


class AssignAsset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], asset_id: str, employee_id: str) -> str:
        asset = _find_one(data["it_assets"], asset_id=asset_id)
        if not asset:
            return json.dumps({"status": "error", "reason": "asset_not_found"})
        asset["assigned_to"] = employee_id
        asset["status"] = "assigned"
        return json.dumps({"status": "ok", "asset": asset})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_asset",
                "description": "Assign an asset to an employee and set status to 'assigned'.",
                "parameters": {
                    "type": "object",
                    "properties": {"asset_id": {"type": "string"}, "employee_id": {"type": "string"}},
                    "required": ["asset_id", "employee_id"],
                },
            },
        }


class UpdateAssetStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], asset_id: str, status: str, mdm_enrolled: Optional[bool] = None) -> str:
        asset = _find_one(data["it_assets"], asset_id=asset_id)
        if not asset:
            return json.dumps({"status": "error", "reason": "asset_not_found"})
        asset["status"] = status
        if mdm_enrolled is not None:
            asset["mdm_enrolled"] = mdm_enrolled
        return json.dumps({"status": "ok", "asset": asset})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_asset_status",
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


class CreateDeviceWorkflow(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        workflow_id: str,
        employee_id: str,
        asset_id: str,
        process: str,
        status: str,
        pickup_code: Optional[str],
        created_at: str,
        completed_at: Optional[str] = None,
    ) -> str:
        row = {
            "workflow_id": workflow_id,
            "employee_id": employee_id,
            "asset_id": asset_id,
            "process": process,
            "status": status,
            "pickup_code": pickup_code,
            "created_at": created_at,
            "completed_at": completed_at,
        }
        _append_row(data["device_workflow"], row)
        return json.dumps({"status": "ok", "workflow": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_device_workflow",
                "description": "Create a device workflow record (e.g., provisioning or return).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "workflow_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                        "asset_id": {"type": "string"},
                        "process": {"type": "string"},
                        "status": {"type": "string"},
                        "pickup_code": {"type": "string"},
                        "created_at": {"type": "string"},
                        "completed_at": {"type": "string"},
                    },
                    "required": ["workflow_id", "employee_id", "asset_id", "process", "status", "created_at"],
                },
            },
        }


class ScheduleMdmAction(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], asset_id: str, when: str, action: str, workflow_id: str) -> str:
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
        _append_row(data["device_workflow"], row)
        return json.dumps({"status": "ok", "workflow": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "schedule_mdm_action",
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


class RequestAssetReturn(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], asset_id: str, employee_id: str, due_ts: str, workflow_id: str) -> str:
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
        _append_row(data["device_workflow"], row)
        return json.dumps({"status": "ok", "workflow": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "request_asset_return",
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


class CreateTicket(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        ticket_id: str,
        employee_id: str,
        category: str,
        priority: str,
        status: str,
        subject: str,
        opened_at: str,
        related_asset_id: Optional[str] = None,
    ) -> str:
        row = {
            "ticket_id": ticket_id,
            "employee_id": employee_id,
            "category": category,
            "priority": priority,
            "status": status,
            "subject": subject,
            "opened_at": opened_at,
            "closed_at": None,
            "related_asset_id": related_asset_id,
        }
        _append_row(data["tickets"], row)
        return json.dumps({"status": "ok", "ticket": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_ticket",
                "description": "Create a service desk ticket.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                        "category": {"type": "string"},
                        "priority": {"type": "string"},
                        "status": {"type": "string"},
                        "subject": {"type": "string"},
                        "opened_at": {"type": "string"},
                        "related_asset_id": {"type": "string"},
                    },
                    "required": ["ticket_id", "employee_id", "category", "priority", "status", "subject", "opened_at"],
                },
            },
        }


class UpdateTicketStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ticket_id: str, status: str, closed_at: Optional[str] = None) -> str:
        t = _find_one(data["tickets"], ticket_id=ticket_id)
        if not t:
            return json.dumps({"status": "error", "reason": "ticket_not_found"})
        valid = {"New", "Open", "In Progress", "On Hold", "Resolved", "Closed"}
        if status not in valid:
            return json.dumps({"status": "error", "reason": "invalid_status"})
        t["status"] = status
        if closed_at is not None:
            t["closed_at"] = closed_at
        return json.dumps({"status": "ok", "ticket": t})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_ticket_status",
                "description": "Update a ticket's status and optional closed_at timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {"ticket_id": {"type": "string"}, "status": {"type": "string"}, "closed_at": {"type": "string"}},
                    "required": ["ticket_id", "status"],
                },
            },
        }


class FindTickets(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        status: Optional[str] = None,
        priority: Optional[str] = None,
        category: Optional[str] = None,
        employee_id: Optional[str] = None,
    ) -> str:
        results = []
        for t in data["tickets"]:
            if status and t["status"] != status:
                continue
            if priority and t["priority"] != priority:
                continue
            if category and t["category"] != category:
                continue
            if employee_id and t["employee_id"] != employee_id:
                continue
            results.append(t)
        return json.dumps({"status": "ok", "tickets": results})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_tickets",
                "description": "Find tickets filtered by status, priority, category, and/or employee_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {"type": "string"},
                        "priority": {"type": "string"},
                        "category": {"type": "string"},
                        "employee_id": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class TakeBacklogSnapshot(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        snapshot_id: str,
        taken_at: str,
        statuses_in_scope: List[str],
    ) -> str:
        open_ids = [t["ticket_id"] for t in data["tickets"] if t["status"] in statuses_in_scope]
        row = {
            "snapshot_id": snapshot_id,
            "taken_at": taken_at,
            "open_ticket_ids": open_ids,
        }
        _append_row(data["backlog_snapshot_open"], row)
        return json.dumps({"status": "ok", "snapshot": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "take_backlog_snapshot",
                "description": "Write a backlog snapshot of ticket IDs for the given statuses.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {"type": "string"},
                        "taken_at": {"type": "string"},
                        "statuses_in_scope": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["snapshot_id", "taken_at", "statuses_in_scope"],
                },
            },
        }


class RecomputeDailyMetrics(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], date: str) -> str:
        opened = len([t for t in data["tickets"] if t["opened_at"].startswith(date)])
        closed = len([t for t in data["tickets"] if t.get("closed_at") and t["closed_at"].startswith(date)])
        closed_24 = 0
        # Approximate: treat any closed on same date as within 24h
        for t in data["tickets"]:
            if t.get("closed_at") and t["closed_at"].startswith(date) and t["opened_at"][:10] == date:
                closed_24 += 1
        avg_age_open_hours = 0
        row = {
            "date": date,
            "tickets_opened": opened,
            "tickets_closed": closed,
            "closed_within_24h": closed_24,
            "avg_open_age_hours": avg_age_open_hours,
        }
        _append_row(data["daily_metrics"], row)
        return json.dumps({"status": "ok", "metrics": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "recompute_daily_metrics",
                "description": "Recompute and append daily ticket metrics for a given date.",
                "parameters": {
                    "type": "object",
                    "properties": {"date": {"type": "string"}},
                    "required": ["date"],
                },
            },
        }


class CreateJiraTicket(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        jira_id: str,
        issue_type: str,
        summary: str,
        priority: str,
        status: str,
        created_at: str,
        updated_at: Optional[str] = None,
    ) -> str:
        row = {
            "jira_id": jira_id,
            "issue_type": issue_type,
            "summary": summary,
            "priority": priority,
            "status": status,
            "created_at": created_at,
            "updated_at": updated_at or created_at,
        }
        _append_row(data["jira_tickets"], row)
        return json.dumps({"status": "ok", "jira": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_jira_ticket",
                "description": "Create a Jira ticket (e.g., License Shortage, Hardware Shortage, Incident).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "jira_id": {"type": "string"},
                        "issue_type": {"type": "string"},
                        "summary": {"type": "string"},
                        "priority": {"type": "string"},
                        "status": {"type": "string"},
                        "created_at": {"type": "string"},
                        "updated_at": {"type": "string"},
                    },
                    "required": ["jira_id", "issue_type", "summary", "priority", "status", "created_at"],
                },
            },
        }


class UpdateJiraStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], jira_id: str, status: str, updated_at: str) -> str:
        row = _find_one(data["jira_tickets"], jira_id=jira_id)
        if not row:
            return json.dumps({"status": "error", "reason": "jira_not_found"})
        row["status"] = status
        row["updated_at"] = updated_at
        return json.dumps({"status": "ok", "jira": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_jira_status",
                "description": "Update the status of a Jira ticket.",
                "parameters": {
                    "type": "object",
                    "properties": {"jira_id": {"type": "string"}, "status": {"type": "string"}, "updated_at": {"type": "string"}},
                    "required": ["jira_id", "status", "updated_at"],
                },
            },
        }


class FindJiraTickets(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        issue_type: Optional[str] = None,
        status: Optional[str] = None,
        priority: Optional[str] = None,
        summary: Optional[str] = None,
    ) -> str:
        results = []
        for j in data["jira_tickets"]:
            if issue_type and j["issue_type"] != issue_type:
                continue
            if status and j["status"] != status:
                continue
            if priority and j["priority"] != priority:
                continue
            if summary and summary not in j["summary"]:
                continue
            results.append(j)
        return json.dumps({"status": "ok", "jira_tickets": results})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_jira_tickets",
                "description": "Find Jira tickets filtered by type, status, priority, or summary substring.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "issue_type": {"type": "string"},
                        "status": {"type": "string"},
                        "priority": {"type": "string"},
                        "summary": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }


class IngestHrMemo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], memo_id: str, memo_json: Dict[str, Any]) -> str:
        row = {"memo_id": memo_id, **memo_json}
        _append_row(data["hr_memos"], row)
        return json.dumps({"status": "ok", "memo": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ingest_hr_memo",
                "description": "Insert an HR memo into the hr_memos table.",
                "parameters": {
                    "type": "object",
                    "properties": {"memo_id": {"type": "string"}, "memo_json": {"type": "object"}},
                    "required": ["memo_id", "memo_json"],
                },
            },
        }


class EnqueueLifecycleEvent(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], lifecycle_id: str, memo_id: str, employee_ref: str, event: str, status: str, created_at: str
    ) -> str:
        row = {
            "lifecycle_id": lifecycle_id,
            "memo_id": memo_id,
            "employee_ref": employee_ref,
            "event": event,
            "status": status,
            "created_at": created_at,
        }
        _append_row(data["lifecycle_queue"], row)
        _append_row(
            data["lifecycle_audit"],
            {
                "audit_id": f"lcaud_{lifecycle_id}_created",
                "lifecycle_id": lifecycle_id,
                "event": f"{event}_created",
                "timestamp": created_at,
                "actor": "system_policy",
            },
        )
        return json.dumps({"status": "ok", "lifecycle": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "enqueue_lifecycle_event",
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
                    "required": ["lifecycle_id", "memo_id", "employee_ref", "event", "status", "created_at"],
                },
            },
        }


class UpdateLifecycleStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], lifecycle_id: str, status: str, timestamp: str, actor: str) -> str:
        row = _find_one(data["lifecycle_queue"], lifecycle_id=lifecycle_id)
        if not row:
            return json.dumps({"status": "error", "reason": "lifecycle_not_found"})
        row["status"] = status
        _append_row(
            data["lifecycle_audit"],
            {
                "audit_id": f"lcaud_{lifecycle_id}_{status}",
                "lifecycle_id": lifecycle_id,
                "event": status,
                "timestamp": timestamp,
                "actor": actor,
            },
        )
        return json.dumps({"status": "ok", "lifecycle": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_lifecycle_status",
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


class RecordLifecycleAudit(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], lifecycle_id: str, event: str, timestamp: str, actor: str) -> str:
        row = {
            "audit_id": f"lcaud_{lifecycle_id}_{event}",
            "lifecycle_id": lifecycle_id,
            "event": event,
            "timestamp": timestamp,
            "actor": actor,
        }
        _append_row(data["lifecycle_audit"], row)
        return json.dumps({"status": "ok", "audit": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "record_lifecycle_audit",
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


class GetAppAccounts(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str, app_id: Optional[str] = None) -> str:
        results = []
        for a in data["app_accounts"]:
            if a["employee_id"] != employee_id:
                continue
            if app_id and a["app_id"] != app_id:
                continue
            results.append(a)
        return json.dumps({"status": "ok", "app_accounts": results})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_app_accounts",
                "description": "Get app accounts for an employee, optionally filtered by app_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}, "app_id": {"type": "string"}},
                    "required": ["employee_id"],
                },
            },
        }


class UpsertAppAccount(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], app_account_id: str, employee_id: str, app_id: str, status: str, created_at: str
    ) -> str:
        row = _find_one(data["app_accounts"], app_account_id=app_account_id)
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
            _append_row(data["app_accounts"], row)
        return json.dumps({"status": "ok", "app_account": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_app_account",
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
                    "required": ["app_account_id", "employee_id", "app_id", "status", "created_at"],
                },
            },
        }


class DisableAppAccount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], app_account_id: str, disabled_at: str) -> str:
        row = _find_one(data["app_accounts"], app_account_id=app_account_id)
        if not row:
            return json.dumps({"status": "error", "reason": "app_account_not_found"})
        row["status"] = "disabled"
        row["disabled_at"] = disabled_at
        return json.dumps({"status": "ok", "app_account": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "disable_app_account",
                "description": "Disable an app account and record disabled_at.",
                "parameters": {
                    "type": "object",
                    "properties": {"app_account_id": {"type": "string"}, "disabled_at": {"type": "string"}},
                    "required": ["app_account_id", "disabled_at"],
                },
            },
        }


class GenerateServiceDeskHealthReport(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        run_id: str,
        started_at: str,
        completed_at: str,
        source_ticket_window_days: int,
        output_path_pdf: str,
    ) -> str:
        row = {
            "run_id": run_id,
            "report_type": "service_desk_health",
            "started_at": started_at,
            "completed_at": completed_at,
            "output_path_pdf": output_path_pdf,
            "source_ticket_window_days": source_ticket_window_days,
        }
        _append_row(data["report_runs"], row)
        return json.dumps({"status": "ok", "report": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_service_desk_health_report",
                "description": "Record a service desk health report generation run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "run_id": {"type": "string"},
                        "started_at": {"type": "string"},
                        "completed_at": {"type": "string"},
                        "source_ticket_window_days": {"type": "integer"},
                        "output_path_pdf": {"type": "string"},
                    },
                    "required": ["run_id", "started_at", "completed_at", "source_ticket_window_days", "output_path_pdf"],
                },
            },
        }


class RecordValidationIssue(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], issue_id: str, entity: str, entity_id: str, field: str, rule: str, details: str, created_at: str
    ) -> str:
        row = {
            "issue_id": issue_id,
            "entity": entity,
            "entity_id": entity_id,
            "field": field,
            "rule": rule,
            "details": details,
            "created_at": created_at,
        }
        _append_row(data["validation_issues"], row)
        return json.dumps({"status": "ok", "validation_issue": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "record_validation_issue",
                "description": "Append a validation issue entry describing an input or data inconsistency.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "issue_id": {"type": "string"},
                        "entity": {"type": "string"},
                        "entity_id": {"type": "string"},
                        "field": {"type": "string"},
                        "rule": {"type": "string"},
                        "details": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": ["issue_id", "entity", "entity_id", "field", "rule", "details", "created_at"],
                },
            },
        }


TOOLS = [
    GetEmployeeById(),
    FindEmployees(),
    GetDirectoryAccount(),
    CreateDirectoryAccount(),
    UpdateDirectoryAccountStatus(),
    SetAccountGroups(),
    AddAccountGroups(),
    RemoveAccountGroups(),
    GetBaselineForRole(),
    CreateMailbox(),
    UpdateMailboxStatus(),
    ArchiveMailbox(),
    GetMailbox(),
    GetLicenseInventory(),
    AssignLicense(),
    RevokeLicense(),
    ReserveLicense(),
    ReleaseLicenseReservation(),
    EnsureLicenseCapacityOrOpenJira(),
    GetLicenseAssignments(),
    FindAssets(),
    AssignAsset(),
    UpdateAssetStatus(),
    CreateDeviceWorkflow(),
    ScheduleMdmAction(),
    RequestAssetReturn(),
    CreateTicket(),
    UpdateTicketStatus(),
    FindTickets(),
    TakeBacklogSnapshot(),
    RecomputeDailyMetrics(),
    CreateJiraTicket(),
    UpdateJiraStatus(),
    FindJiraTickets(),
    IngestHrMemo(),
    EnqueueLifecycleEvent(),
    UpdateLifecycleStatus(),
    RecordLifecycleAudit(),
    GetAppAccounts(),
    UpsertAppAccount(),
    DisableAppAccount(),
    GenerateServiceDeskHealthReport(),
    RecordValidationIssue(),
]
