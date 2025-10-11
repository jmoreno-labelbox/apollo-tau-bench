# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






class AssignUserRoleTool(Tool):
    """assign_user_role"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_role_id = kwargs["user_role_id"]
        user_id = kwargs["user_id"]
        role_id = kwargs["role_id"]
        assigned_by = kwargs["assigned_by"]
        expires_on = kwargs.get("expires_on")
        roles = data.setdefault("user_roles", [])
        existing_active = next(
            (
                r
                for r in roles
                if r.get("user_id") == user_id
                and r.get("role_id") == role_id
                and not r.get("expires_on")
            ),
            None,
        )
        if existing_active:
            record = existing_active
        else:
            existing_by_id = next(
                (r for r in roles if r.get("user_role_id") == user_role_id), None
            )
            if existing_by_id:
                record = existing_by_id
            else:
                record = {
                    "user_role_id": user_role_id,
                    "user_id": user_id,
                    "role_id": role_id,
                    "assigned_by": assigned_by,
                    "assigned_on": _HARD_TS,
                    "expires_on": expires_on,
                }
                roles.append(record)
        return json.dumps(record, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_user_role",
                "description": "Create a user_role assignment if not already active.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_role_id": {"type": "string"},
                        "user_id": {"type": "string"},
                        "role_id": {"type": "string"},
                        "assigned_by": {"type": "string"},
                        "assigned_on": {"type": "string"},
                        "expires_on": {"type": ["string", "null"]},
                    },
                    "required": [
                        "user_role_id",
                        "user_id",
                        "role_id",
                        "assigned_by",
                        "assigned_on",
                    ],
                },
            },
        }

class AssignRoleOnApprovalTool(Tool):
    """
    Idempotently assign the role from an approved access request and ALWAYS
    return a user_role_id. Also heals existing assignments missing user_role_id.
    """

    @staticmethod
    def _derive_user_role_id(request_id: str, user_id: str, role_id: str) -> str:
        # Stable, deterministic; keeps it short if you prefer only digits
        import re

        digits = "".join(re.findall(r"\d+", request_id)) or "000"
        return f"UR-{digits}"

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        import json as _json

        request_id = kwargs.get("request_id")
        assigned_by = kwargs.get("assigned_by")
        provided_urid = kwargs.get("user_role_id")

        if not request_id or not assigned_by:
            return _json.dumps(
                {"error": "request_id and assigned_by are required"}, indent=2
            )

        # Locate the access request
        requests = data.get("access_requests", [])
        req = next((r for r in requests if r.get("request_id") == request_id), None)
        if not req:
            return _json.dumps(
                {"error": f"Access request {request_id} not found"}, indent=2
            )

        user_id = req.get("user_id")
        role_id = req.get("requested_role_id")

        if not user_id or not role_id:
            return _json.dumps(
                {"error": f"Request {request_id} missing user_id/requested_role_id"},
                indent=2,
            )

        assignments: List[Dict[str, Any]] = data.setdefault("user_roles", [])

        # Try to find an active existing assignment
        existing = next(
            (
                a
                for a in assignments
                if a.get("user_id") == user_id
                and a.get("role_id") == role_id
                and not a.get("expires_on")
            ),
            None,
        )

        if existing:
            # Heal missing user_role_id if necessary
            if "user_role_id" not in existing or not existing["user_role_id"]:
                existing["user_role_id"] = (
                    provided_urid
                    or AssignRoleOnApprovalTool._derive_user_role_id(
                        request_id, user_id, role_id
                    )
                )
            # Ensure required fields are present
            existing.setdefault("assigned_by", assigned_by)
            existing.setdefault("assigned_on", _HARD_TS)
            existing.setdefault("expires_on", None)

            out = {
                "user_role_id": existing["user_role_id"],
                "user_id": user_id,
                "role_id": role_id,
                "assigned_by": existing["assigned_by"],
                "assigned_on": _HARD_TS,
                "expires_on": existing["expires_on"],
            }
            return _json.dumps(out, indent=2)

        # Create a brand-new assignment
        user_role_id = provided_urid or AssignRoleOnApprovalTool._derive_user_role_id(
            request_id, user_id, role_id
        )

        record = {
            "user_role_id": user_role_id,
            "user_id": user_id,
            "role_id": role_id,
            "assigned_by": assigned_by,
            "assigned_on": _HARD_TS,
            "expires_on": None,
        }
        assignments.append(record)

        out = {
            "user_role_id": user_role_id,
            "user_id": user_id,
            "role_id": role_id,
            "assigned_by": assigned_by,
            "assigned_on": _HARD_TS,
            "expires_on": None,
        }
        return _json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_role_on_approval",
                "description": (
                    "Assign the role from an approved access request (idempotent; always returns user_role_id)."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {
                            "type": "string",
                            "description": "Access request ID (e.g., AR-008)",
                        },
                        "assigned_by": {
                            "type": "string",
                            "description": (
                                "Reviewer's user ID who approved the request (e.g., U-010)"
                            ),
                        },
                        "user_role_id": {
                            "type": "string",
                            "description": (
                                "Optional stable assignment ID to use (e.g., reuse audit log id)"
                            ),
                        },
                    },
                    "required": ["request_id", "assigned_by"],
                },
            },
        }

class GrantRoleTool(Tool):
    """grant_role: assign a role either by request_id or direct user_id/role_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], assigned_by, expires_on, request_id, role_id, user_id, user_role_id) -> str:
        if request_id:
            return AssignRoleOnApprovalTool.invoke(
                data, request_id=request_id, assigned_by=assigned_by
            )
        # straightforward
        return AssignUserRoleTool.invoke(
            data,
            user_role_id=user_role_id,
            user_id=user_id,
            role_id=role_id,
            assigned_by=assigned_by,
            expires_on=expires_on,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "grant_role",
                "description": "Assign a role by request_id or direct user/role pair.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "user_role_id": {"type": "string"},
                        "user_id": {"type": "string"},
                        "role_id": {"type": "string"},
                        "assigned_by": {"type": "string"},
                        "expires_on": {"type": ["string", "null"]},
                    },
                    "required": ["assigned_by"],
                },
            },
        }