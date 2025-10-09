from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AssignRoleOnApprovalTool(Tool):
    """
    Idempotently allocate the role from an approved access request and ALWAYS
    return a user_role_id. Additionally, repairs existing assignments lacking user_role_id.
    """

    @staticmethod
    def _derive_user_role_id(request_id: str, user_id: str, role_id: str) -> str:
        pass
        #Consistent and predictable; maintains brevity if only digits are desired
        import re

        digits = "".join(re.findall(r"\d+", request_id)) or "000"
        return f"UR-{digits}"

    @staticmethod
    def invoke(data: dict[str, Any], request_id: str = None, assigned_by: str = None, provided_urid: str = None) -> str:
        import json as _json

        if not request_id or not assigned_by:
            return _json.dumps(
                {"error": "request_id and assigned_by are required"}, indent=2
            )

        # Find the access request
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

        assignments: list[dict[str, Any]] = data.setdefault("user_roles", [])

        # Attempt to locate an active existing assignment
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
            # Repair any missing user_role_id if needed
            if "user_role_id" not in existing or not existing["user_role_id"]:
                existing["user_role_id"] = (
                    provided_urid
                    or AssignRoleOnApprovalTool._derive_user_role_id(
                        request_id, user_id, role_id
                    )
                )
            # Confirm that necessary fields are included
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

        # Establish a completely new assignment
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
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assignRoleOnApproval",
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
