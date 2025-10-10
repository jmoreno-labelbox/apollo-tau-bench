# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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
