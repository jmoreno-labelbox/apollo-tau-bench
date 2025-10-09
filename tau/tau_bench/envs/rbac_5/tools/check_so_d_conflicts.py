from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any

class CheckSoDConflicts(Tool):
    """
    Assess if a user has Separation of Duties (SoD) conflicts based on their active roles,
    or if incorporating a specific role would lead to a conflict.

    SoD conflicts are recognized by predefined conflicting role pairs that breach
    business control principles (e.g., finance processing versus auditing).

    kwargs:
      user_id: str (mandatory)
      on_date: str ISO (optional; defaults to now)
      include_role_details: bool = False (include role names and descriptions)
      role_id: str (optional) - If supplied, checks if adding this role to the user would create a conflict
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str = "",
        on_date: str = None,
        include_role_details: bool = False,
        role_id: str = None
    ) -> str:
        pass
        on_date_iso = on_date or get_current_timestamp()
        test_role_id = role_id

        if not user_id:
            payload = {"error": "user_id is required"}
            out = json.dumps(payload)
            return out

        # Confirm the user is present
        if not _find_by_id(data.get("users", []), "user_id", user_id):
            payload = {"error": f"user_id {user_id} not found"}
            out = json.dumps(payload)
            return out

        on_dt = _parse_iso(on_date_iso) or datetime.now(tz=timezone.utc)

        def is_active(ur: dict[str, Any]) -> bool:
            pass
            exp = _parse_iso(ur.get("expires_on"))
            return (exp is None) or (exp > on_dt)

        # Retrieve the user's current role assignments
        assignments = [
            ur
            for ur in data.get("user_roles", [])
            if ur.get("user_id") == user_id and is_active(ur)
        ]

        active_role_ids = {ur.get("role_id") for ur in assignments}
        # If test_role_id is supplied, simulate its addition
        if test_role_id:
            active_role_ids = set(active_role_ids)
            active_role_ids.add(test_role_id)

        # Establish SoD conflict guidelines based on role evaluation
        sod_conflicts = [
            # Financial SoD conflicts
            {
                "conflict_id": "FINANCE_SOD_001",
                "name": "Finance Processing vs Audit Access",
                "description": "Users cannot both process financial transactions and audit them",
                "conflicting_roles": [
                    "ROL-031",
                    "ROL-033",
                ],  # finance-invoice-processor compared to finance-audit-access
                "risk_level": "HIGH",
            },
            {
                "conflict_id": "FINANCE_SOD_002",
                "name": "Budget Admin vs Audit Access",
                "description": "Users cannot both manage budgets and audit financial records",
                "conflicting_roles": [
                    "ROL-032",
                    "ROL-033",
                ],  # finance-budget-admin compared to finance-audit-access
                "risk_level": "HIGH",
            },
            # Engineering-related SoD conflicts
            {
                "conflict_id": "ENGINEERING_SOD_001",
                "name": "Code Development vs Production Deployment",
                "description": "Developers cannot deploy their own code to production without review",
                "conflicting_roles": [
                    "ROL-002",
                    "ROL-025",
                ],  # engineering-code-commit compared to operations-deployment-admin
                "risk_level": "CRITICAL",
            },
            {
                "conflict_id": "ENGINEERING_SOD_002",
                "name": "Code Development vs Production Access",
                "description": "Developers should not have direct production system access",
                "conflicting_roles": [
                    "ROL-002",
                    "ROL-003",
                ],  # engineering-code-commit compared to engineering-prod-access
                "risk_level": "HIGH",
            },
            # Conflicts among operations administrators
            {
                "conflict_id": "OPERATIONS_SOD_001",
                "name": "System Admin vs Database Admin",
                "description": "Excessive administrative privileges across system and database layers",
                "conflicting_roles": [
                    "ROL-026",
                    "ROL-027",
                ],  # operations-system-admin compared to operations-db-admin
                "risk_level": "MEDIUM",
            },
            {
                "conflict_id": "OPERATIONS_SOD_002",
                "name": "System Admin vs Network Admin",
                "description": "Excessive administrative privileges across system and network layers",
                "conflicting_roles": [
                    "ROL-026",
                    "ROL-028",
                ],  # operations-system-admin compared to operations-network-admin
                "risk_level": "MEDIUM",
            },
            # HR-related SoD conflicts
            {
                "conflict_id": "HR_SOD_001",
                "name": "Employee Data Access vs Payroll Admin",
                "description": "Users cannot both access employee data and manage payroll",
                "conflicting_roles": [
                    "ROL-017",
                    "ROL-018",
                ],  # hr-employee-data-read compared to hr-payroll-admin
                "risk_level": "HIGH",
            },
            {
                "conflict_id": "HR_SOD_002",
                "name": "Employee Data Access vs Benefits Admin",
                "description": "Users cannot both access employee data and manage benefits",
                "conflicting_roles": [
                    "ROL-017",
                    "ROL-020",
                ],  # hr-employee-data-read compared to hr-benefits-admin
                "risk_level": "MEDIUM",
            },
            # Sales-related SoD conflicts
            {
                "conflict_id": "SALES_SOD_001",
                "name": "Lead Management vs Commission Viewing",
                "description": "Sales leads managers should not view commission data to prevent manipulation",
                "conflicting_roles": [
                    "ROL-013",
                    "ROL-015",
                ],  # sales-lead-manager compared to sales-commission-view
                "risk_level": "MEDIUM",
            },
        ]

        # Verify for conflicts
        detected_conflicts = []
        role_map = {r.get("role_id"): r for r in data.get("roles", [])}

        for conflict in sod_conflicts:
            conflicting_role_ids = conflict["conflicting_roles"]
            # Determine if the user possesses ALL roles in the conflicting group
            if all(role_id in active_role_ids for role_id in conflicting_role_ids):
                conflict_entry = {
                    "conflict_id": conflict["conflict_id"],
                    "name": conflict["name"],
                    "description": conflict["description"],
                    "risk_level": conflict["risk_level"],
                    "conflicting_role_ids": conflicting_role_ids,
                }

                if include_role_details:
                    conflict_entry["conflicting_roles"] = []
                    for role_id in conflicting_role_ids:
                        role = role_map.get(role_id, {})
                        conflict_entry["conflicting_roles"].append(
                            {
                                "role_id": role_id,
                                "role_name": role.get("role_name"),
                                "description": role.get("description"),
                            }
                        )

                detected_conflicts.append(conflict_entry)
        payload = {
                "ok": True,
                "user_id": user_id,
                "has_sod_conflicts": len(detected_conflicts) > 0,
                "conflict_count": len(detected_conflicts),
                "conflicts": detected_conflicts,
                "checked_on": on_date_iso,
                "simulated_role_id": test_role_id if test_role_id else None,
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CheckSodConflicts",
                "description": "Check if a user has Separation of Duties (SoD) conflicts based on their active roles, or if adding a specific role would result in a conflict.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "Target user_id (e.g., U-001).",
                        },
                        "on_date": {
                            "type": "string",
                            "description": "ISO timestamp to evaluate role assignments against (optional).",
                        },
                        "include_role_details": {
                            "type": "boolean",
                            "description": "Include role names and descriptions in conflict details.",
                            "default": False,
                        },
                        "role_id": {
                            "type": "string",
                            "description": "If provided, checks if adding this role to the user would cause a conflict.",
                        },
                    },
                    "required": ["user_id"],
                    "additionalProperties": False,
                },
            },
        }
