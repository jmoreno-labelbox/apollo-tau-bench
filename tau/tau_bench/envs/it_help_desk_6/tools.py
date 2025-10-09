import json
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


def _append_row(table: list[dict[str, Any]], row: dict[str, Any]) -> None:
    pass
    table.append(row)


def _find_one(
    collection: list[dict[str, Any]], **filters: Any
) -> dict[str, Any] | None:
    pass
    for row in collection:
        if all(row.get(k) == v for k, v in filters.items()):
            return row
    return None


def _update_row(row: dict[str, Any], updates: dict[str, Any]) -> None:
    pass
    for k, v in updates.items():
        row[k] = v


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


class GetEmployeeById(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str) -> str:
        pass
        emp = _find_one(data["employees"], employee_id=employee_id)
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


class FindEmployees(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        department: str | None = None,
        job_title: str | None = None,
        status: str | None = None,
        manager_id: str | None = None,
    ) -> str:
        pass
        results = _find_all(
            data["employees"],
            department=department,
            job_title=job_title,
            status=status,
            manager_id=manager_id,
        )
        payload = {"status": "ok", "employees": results}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindEmployees",
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
    def invoke(
        data: dict[str, Any],
        employee_id: str | None = None,
        account_id: str | None = None,
    ) -> str:
        pass
        acct = None
        if account_id:
            acct = _find_one(data["directory_accounts"], account_id=account_id)
        elif employee_id:
            acct = _find_one(data["directory_accounts"], employee_id=employee_id)
        payload = {"status": "ok", "account": acct}
        out = json.dumps(payload)
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


class CreateDirectoryAccount(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        account_id: str,
        employee_id: str,
        username: str,
        created_at: str,
        status: str = "enabled",
        group_ids: list[str] | None = None,
        department: Any = None,
        job_title: Any = None,
    ) -> str:
        pass
        #Check if the employee is present
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
            payload = {"status": "error", "reason": "employee_not_found"}
            out = json.dumps(payload)
            return out

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
        payload = {"status": "ok", "account": row}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createDirectoryAccount",
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
    def invoke(
        data: dict[str, Any],
        account_id: str,
        status: str,
        disabled_at: str | None = None,
    ) -> str:
        pass
        acct = _find_one(data["directory_accounts"], account_id=account_id)
        if not acct:
            payload = {"status": "error", "reason": "account_not_found"}
            out = json.dumps(payload)
            return out
        if status not in {"enabled", "disabled"}:
            payload = {"status": "error", "reason": "invalid_status"}
            out = json.dumps(payload)
            return out
        acct["status"] = status
        acct["disabled_at"] = disabled_at
        payload = {"status": "ok", "account": acct}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateDirectoryAccountStatus",
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
        data: dict[str, Any],
        account_id: str,
        group_ids: list[str],
        actor: str,
        timestamp: str,
    ) -> str:
        pass
        acct = _find_one(data["directory_accounts"], account_id=account_id)
        if not acct:
            payload = {"status": "error", "reason": "account_not_found"}
            out = json.dumps(payload)
            return out
        old = set(acct.get("group_ids", []))
        new = set(group_ids)
        #calculate differences for auditing purposes
        to_add = sorted(list(new - old))
        to_remove = sorted(list(old - new))
        acct["group_ids"] = sorted(group_ids)
        if not to_add and not to_remove:
            #Regardless of changes, the policy requires an audit record to be generated for the action.
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
        payload = {"status": "ok", "account": acct, "added": to_add, "removed": to_remove}
        out = json.dumps(
            payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetAccountGroups",
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
    def invoke(
        data: dict[str, Any],
        account_id: str,
        group_ids: list[str],
        actor: str,
        timestamp: str,
    ) -> str:
        pass
        acct = _find_one(data["directory_accounts"], account_id=account_id)
        if not acct:
            payload = {"status": "error", "reason": "account_not_found"}
            out = json.dumps(payload)
            return out
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
        payload = {"status": "ok", "account": acct}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addAccountGroups",
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
    def invoke(
        data: dict[str, Any],
        account_id: str,
        group_ids: list[str],
        actor: str,
        timestamp: str,
    ) -> str:
        pass
        acct = _find_one(data["directory_accounts"], account_id=account_id)
        if not acct:
            payload = {"status": "error", "reason": "account_not_found"}
            out = json.dumps(payload)
            return out
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
        payload = {"status": "ok", "account": acct}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveAccountGroups",
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
    def invoke(data: dict[str, Any], department: str, job_title: str) -> str:
        pass
        row = _find_one(
            data["rbac_group_map"], department=department, job_title=job_title
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
        out = json.dumps(
            payload)
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


class CreateMailbox(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        mailbox_id: str,
        employee_id: str,
        address: str,
        retention_policy: str,
        created_at: str,
        status: str = "active",
    ) -> str:
        pass
        if retention_policy not in {"std_2y", "finance_7y"}:
            payload = {"status": "error", "reason": "invalid_retention"}
            out = json.dumps(payload)
            return out
        row = {
            "mailbox_id": mailbox_id,
            "employee_id": employee_id,
            "address": address,
            "status": status,
            "retention_policy": retention_policy,
            "created_at": created_at,
        }
        _append_row(data["mailboxes"], row)
        payload = {"status": "ok", "mailbox": row}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateMailbox",
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
                    "required": [
                        "mailbox_id",
                        "employee_id",
                        "address",
                        "retention_policy",
                        "created_at",
                    ],
                },
            },
        }


class UpdateMailboxStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], mailbox_id: str, status: str) -> str:
        pass
        mbx = _find_one(data["mailboxes"], mailbox_id=mailbox_id)
        if not mbx:
            payload = {"status": "error", "reason": "mailbox_not_found"}
            out = json.dumps(payload)
            return out
        if status not in {"active", "inactive"}:
            payload = {"status": "error", "reason": "invalid_status"}
            out = json.dumps(payload)
            return out
        mbx["status"] = status
        payload = {"status": "ok", "mailbox": mbx}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateMailboxStatus",
                "description": "Set mailbox status to active or inactive.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "mailbox_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["mailbox_id", "status"],
                },
            },
        }


class ArchiveMailbox(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        archive_id: str,
        mailbox_id: str,
        employee_id: str,
        archive_path: str,
        retention_policy: str,
        created_at: str,
    ) -> str:
        pass
        row = {
            "archive_id": archive_id,
            "employee_id": employee_id,
            "mailbox_id": mailbox_id,
            "archive_path": archive_path,
            "retention_policy": retention_policy,
            "created_at": created_at,
        }
        _append_row(data["data_archives"], row)
        payload = {"status": "ok", "archive": row}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ArchiveMailbox",
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
                    "required": [
                        "archive_id",
                        "mailbox_id",
                        "employee_id",
                        "archive_path",
                        "retention_policy",
                        "created_at",
                    ],
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
        pass
        mbx = None
        if mailbox_id:
            mbx = _find_one(data["mailboxes"], mailbox_id=mailbox_id)
        elif employee_id:
            mbx = _find_one(data["mailboxes"], employee_id=employee_id)
        payload = {"status": "ok", "mailbox": mbx}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMailbox",
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


class GetLicenseInventory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], license_id: str | None = None) -> str:
        pass
        if license_id:
            row = _find_one(data["license_inventory"], license_id=license_id)
            payload = {"status": "ok", "inventory": row}
            out = json.dumps(payload)
            return out
        payload = {"status": "ok", "inventory": data["license_inventory"]}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetLicenseInventory",
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
        data: dict[str, Any],
        assignment_id: str,
        account_id: str,
        employee_id: str,
        license_id: str,
        assigned_at: str,
    ) -> str:
        pass
        inv = _find_one(data["license_inventory"], license_id=license_id)
        if not inv:
            payload = {"status": "error", "reason": "license_not_found"}
            out = json.dumps(payload)
            return out
        if inv["used_seats"] + inv["reserved_seats"] + 1 > inv["total_seats"]:
            payload = {"status": "error", "reason": "no_capacity"}
            out = json.dumps(payload)
            return out

        #Alter the dictionary within the list directly
        for item in data["license_inventory"].values():
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
        payload = {"status": "ok", "assignment": row, "inventory": inv}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignLicense",
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
                    "required": [
                        "assignment_id",
                        "account_id",
                        "employee_id",
                        "license_id",
                        "assigned_at",
                    ],
                },
            },
        }


class RevokeLicense(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        account_id: str,
        employee_id: str,
        license_id: str,
        revoked_at: str,
    ) -> str:
        pass
        inv = _find_one(data["license_inventory"], license_id=license_id)
        if not inv:
            payload = {"status": "error", "reason": "license_not_found"}
            out = json.dumps(payload)
            return out
        #locate the current assignment
        row = None
        for a in data["license_assignments"].values():
            if (
                a["account_id"] == account_id
                and a["employee_id"] == employee_id
                and a["license_id"] == license_id
                and a["status"] == "active"
            ):
                row = a
                break
        if not row:
            payload = {"status": "error", "reason": "assignment_not_found"}
            out = json.dumps(payload)
            return out
        row["status"] = "revoked"
        row["revoked_at"] = revoked_at
        if inv["used_seats"] > 0:
            inv["used_seats"] -= 1
        payload = {"status": "ok", "assignment": row, "inventory": inv}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RevokeLicense",
                "description": "Revoke an active license and decrement used seats.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                        "license_id": {"type": "string"},
                        "revoked_at": {"type": "string"},
                    },
                    "required": [
                        "account_id",
                        "employee_id",
                        "license_id",
                        "revoked_at",
                    ],
                },
            },
        }


class ReserveLicense(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], license_id: str, count: int, reason: str) -> str:
        pass
        inv = _find_one(data["license_inventory"], license_id=license_id)
        if not inv:
            payload = {"status": "error", "reason": "license_not_found"}
            out = json.dumps(payload)
            return out
        if inv["used_seats"] + inv["reserved_seats"] + count > inv["total_seats"]:
            payload = {"status": "error", "reason": "no_capacity"}
            out = json.dumps(payload)
            return out
        inv["reserved_seats"] += count
        payload = {"status": "ok", "inventory": inv, "reason": reason}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReserveLicense",
                "description": "Reserve seats for a license (inventory reserved_seats).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "license_id": {"type": "string"},
                        "count": {"type": "integer"},
                        "reason": {"type": "string"},
                    },
                    "required": ["license_id", "count", "reason"],
                },
            },
        }


class ReleaseLicenseReservation(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], license_id: str, count: int) -> str:
        pass
        inv = _find_one(data["license_inventory"], license_id=license_id)
        if not inv:
            payload = {"status": "error", "reason": "license_not_found"}
            out = json.dumps(payload)
            return out
        inv["reserved_seats"] = max(0, inv["reserved_seats"] - count)
        payload = {"status": "ok", "inventory": inv}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReleaseLicenseReservation",
                "description": "Release previously reserved license seats.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "license_id": {"type": "string"},
                        "count": {"type": "integer"},
                    },
                    "required": ["license_id", "count"],
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
        pass
        inv = _find_one(data["license_inventory"], license_id=license_id)
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
        #access Jira and mark the block
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
        payload = {"status": "ok", "capacity": False, "jira": jira}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EnsureLicenseCapacityOrOpenTaskTrack",
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


class GetLicenseAssignments(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str | None = None,
        account_id: str | None = None,
    ) -> str:
        pass
        results: list[dict[str, Any]] = []
        for a in data["license_assignments"].values():
            if employee_id and a["employee_id"] != employee_id:
                continue
            if account_id and a["account_id"] != account_id:
                continue
            results.append(a)
        payload = {"status": "ok", "assignments": results}
        out = json.dumps(payload)
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
        pass
        results = []
        for a in data["it_assets"].values():
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


class AssignAsset(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_id: str, employee_id: str) -> str:
        pass
        asset = _find_one(data["it_assets"], asset_id=asset_id)
        if not asset:
            payload = {"status": "error", "reason": "asset_not_found"}
            out = json.dumps(payload)
            return out
        asset["assigned_to"] = employee_id
        asset["status"] = "assigned"
        payload = {"status": "ok", "asset": asset}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignAsset",
                "description": "Assign an asset to an employee and set status to 'assigned'.",
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


class UpdateAssetStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        asset_id: str,
        status: str,
        mdm_enrolled: bool | None = None,
    ) -> str:
        pass
        asset = _find_one(data["it_assets"], asset_id=asset_id)
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
                "name": "updateAssetStatus",
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
        data: dict[str, Any],
        workflow_id: str,
        employee_id: str,
        asset_id: str,
        process: str,
        status: str,
        pickup_code: str | None,
        created_at: str,
        completed_at: str | None = None,
    ) -> str:
        pass
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
        payload = {"status": "ok", "workflow": row}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateDeviceWorkflow",
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
                    "required": [
                        "workflow_id",
                        "employee_id",
                        "asset_id",
                        "process",
                        "status",
                        "created_at",
                    ],
                },
            },
        }


class ScheduleMdmAction(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], asset_id: str, when: str, action: str, workflow_id: str
    ) -> str:
        pass
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
        payload = {"status": "ok", "workflow": row}
        out = json.dumps(payload)
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


class RequestAssetReturn(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        asset_id: str,
        employee_id: str,
        due_ts: str,
        workflow_id: str,
    ) -> str:
        pass
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
        payload = {"status": "ok", "workflow": row}
        out = json.dumps(payload)
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


class CreateTicket(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        ticket_id: str,
        employee_id: str,
        category: str,
        priority: str,
        status: str,
        subject: str,
        opened_at: str,
        related_asset_id: str | None = None,
    ) -> str:
        pass
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
        payload = {"status": "ok", "ticket": row}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateTicket",
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
                    "required": [
                        "ticket_id",
                        "employee_id",
                        "category",
                        "priority",
                        "status",
                        "subject",
                        "opened_at",
                    ],
                },
            },
        }


class UpdateTicketStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], ticket_id: str, status: str, closed_at: str | None = None
    ) -> str:
        pass
        t = _find_one(data["tickets"], ticket_id=ticket_id)
        if not t:
            payload = {"status": "error", "reason": "ticket_not_found"}
            out = json.dumps(payload)
            return out
        valid = {"New", "Open", "In Progress", "On Hold", "Resolved", "Closed"}
        if status not in valid:
            payload = {"status": "error", "reason": "invalid_status"}
            out = json.dumps(payload)
            return out
        t["status"] = status
        if closed_at is not None:
            t["closed_at"] = closed_at
        payload = {"status": "ok", "ticket": t}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateTicketStatus",
                "description": "Update a ticket's status and optional closed_at timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {"type": "string"},
                        "status": {"type": "string"},
                        "closed_at": {"type": "string"},
                    },
                    "required": ["ticket_id", "status"],
                },
            },
        }


class FindTickets(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        status: str | None = None,
        priority: str | None = None,
        category: str | None = None,
        employee_id: str | None = None,
    ) -> str:
        pass
        results = []
        for t in data["tickets"].values():
            if status and t["status"] != status:
                continue
            if priority and t["priority"] != priority:
                continue
            if category and t["category"] != category:
                continue
            if employee_id and t["employee_id"] != employee_id:
                continue
            results.append(t)
        payload = {"status": "ok", "tickets": results}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindTickets",
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
        data: dict[str, Any],
        snapshot_id: str,
        taken_at: str,
        statuses_in_scope: list[str],
    ) -> str:
        pass
        open_ids = [
            t["ticket_id"] for t in data["tickets"].values() if t["status"] in statuses_in_scope
        ]
        row = {
            "snapshot_id": snapshot_id,
            "taken_at": taken_at,
            "open_ticket_ids": open_ids,
        }
        _append_row(data["backlog_snapshot_open"], row)
        payload = {"status": "ok", "snapshot": row}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "TakeBacklogSnapshot",
                "description": "Write a backlog snapshot of ticket IDs for the given statuses.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {"type": "string"},
                        "taken_at": {"type": "string"},
                        "statuses_in_scope": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["snapshot_id", "taken_at", "statuses_in_scope"],
                },
            },
        }


class RecomputeDailyMetrics(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], date: str) -> str:
        pass
        opened = len([t for t in data["tickets"].values() if t["opened_at"].startswith(date)])
        closed = len(
            [
                t
                for t in data["tickets"].values()
                if t.get("closed_at") and t["closed_at"].startswith(date)
            ]
        )
        closed_24 = 0
        #Estimate: consider any closures on the same date as occurring within 24 hours
        for t in data["tickets"].values():
            if (
                t.get("closed_at")
                and t["closed_at"].startswith(date)
                and t["opened_at"][:10] == date
            ):
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
        payload = {"status": "ok", "metrics": row}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecomputeDailyMetrics",
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
        data: dict[str, Any],
        jira_id: str,
        issue_type: str,
        summary: str,
        priority: str,
        status: str,
        created_at: str,
        updated_at: str | None = None,
    ) -> str:
        pass
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
        payload = {"status": "ok", "jira": row}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateJiraTicket",
                "description": "Create a TaskTrack ticket (e.g., License Shortage, Hardware Shortage, Incident).",
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
                    "required": [
                        "jira_id",
                        "issue_type",
                        "summary",
                        "priority",
                        "status",
                        "created_at",
                    ],
                },
            },
        }


class UpdateJiraStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], jira_id: str, status: str, updated_at: str) -> str:
        pass
        row = _find_one(data["jira_tickets"], jira_id=jira_id)
        if not row:
            payload = {"status": "error", "reason": "jira_not_found"}
            out = json.dumps(payload)
            return out
        row["status"] = status
        row["updated_at"] = updated_at
        payload = {"status": "ok", "jira": row}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateJiraStatus",
                "description": "Update the status of a TaskTrack ticket.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "jira_id": {"type": "string"},
                        "status": {"type": "string"},
                        "updated_at": {"type": "string"},
                    },
                    "required": ["jira_id", "status", "updated_at"],
                },
            },
        }


class FindJiraTickets(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        issue_type: str | None = None,
        status: str | None = None,
        priority: str | None = None,
        summary: str | None = None,
    ) -> str:
        pass
        results = []
        for j in data["jira_tickets"].values():
            if issue_type and j["issue_type"] != issue_type:
                continue
            if status and j["status"] != status:
                continue
            if priority and j["priority"] != priority:
                continue
            if summary and summary not in j["summary"]:
                continue
            results.append(j)
        payload = {"status": "ok", "jira_tickets": results}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindJiraTickets",
                "description": "Find TaskTrack tickets filtered by type, status, priority, or summary substring.",
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
    def invoke(data: dict[str, Any], memo_id: str, memo_json: dict[str, Any]) -> str:
        pass
        row = {"memo_id": memo_id, **memo_json}
        _append_row(data["hr_memos"], row)
        payload = {"status": "ok", "memo": row}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ingestHrMemo",
                "description": "Insert an HR memo into the hr_memos table.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "memo_id": {"type": "string"},
                        "memo_json": {"type": "object"},
                    },
                    "required": ["memo_id", "memo_json"],
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
        pass
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
        payload = {"status": "ok", "lifecycle": row}
        out = json.dumps(payload)
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


class UpdateLifecycleStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], lifecycle_id: str, status: str, timestamp: str, actor: str
    ) -> str:
        pass
        row = _find_one(data["lifecycle_queue"], lifecycle_id=lifecycle_id)
        if not row:
            payload = {"status": "error", "reason": "lifecycle_not_found"}
            out = json.dumps(payload)
            return out
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


class RecordLifecycleAudit(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], lifecycle_id: str, event: str, timestamp: str, actor: str
    ) -> str:
        pass
        row = {
            "audit_id": f"lcaud_{lifecycle_id}_{event}",
            "lifecycle_id": lifecycle_id,
            "event": event,
            "timestamp": timestamp,
            "actor": actor,
        }
        _append_row(data["lifecycle_audit"], row)
        payload = {"status": "ok", "audit": row}
        out = json.dumps(payload)
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


class GetAppAccounts(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], employee_id: str, app_id: str | None = None
    ) -> str:
        pass
        results = []
        for a in data["app_accounts"].values():
            if a["employee_id"] != employee_id:
                continue
            if app_id and a["app_id"] != app_id:
                continue
            results.append(a)
        payload = {"status": "ok", "app_accounts": results}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAppAccounts",
                "description": "Get app accounts for an employee, optionally filtered by app_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "app_id": {"type": "string"},
                    },
                    "required": ["employee_id"],
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
        pass
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
        payload = {"status": "ok", "app_account": row}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpsertAppAccount",
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


class DisableAppAccount(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], app_account_id: str, disabled_at: str) -> str:
        pass
        row = _find_one(data["app_accounts"], app_account_id=app_account_id)
        if not row:
            payload = {"status": "error", "reason": "app_account_not_found"}
            out = json.dumps(payload)
            return out
        row["status"] = "disabled"
        row["disabled_at"] = disabled_at
        payload = {"status": "ok", "app_account": row}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DisableAppAccount",
                "description": "Disable an app account and record disabled_at.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "app_account_id": {"type": "string"},
                        "disabled_at": {"type": "string"},
                    },
                    "required": ["app_account_id", "disabled_at"],
                },
            },
        }


class GenerateServiceDeskHealthReport(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        run_id: str,
        started_at: str,
        completed_at: str,
        source_ticket_window_days: int,
        output_path_pdf: str,
    ) -> str:
        pass
        row = {
            "run_id": run_id,
            "report_type": "service_desk_health",
            "started_at": started_at,
            "completed_at": completed_at,
            "output_path_pdf": output_path_pdf,
            "source_ticket_window_days": source_ticket_window_days,
        }
        _append_row(data["report_runs"], row)
        payload = {"status": "ok", "report": row}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateServiceDeskHealthReport",
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
                    "required": [
                        "run_id",
                        "started_at",
                        "completed_at",
                        "source_ticket_window_days",
                        "output_path_pdf",
                    ],
                },
            },
        }


class RecordValidationIssue(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        issue_id: str,
        entity: str,
        entity_id: str,
        field: str,
        rule: str,
        details: str,
        created_at: str,
    ) -> str:
        pass
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
        payload = {"status": "ok", "validation_issue": row}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordValidationIssue",
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
                    "required": [
                        "issue_id",
                        "entity",
                        "entity_id",
                        "field",
                        "rule",
                        "details",
                        "created_at",
                    ],
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
