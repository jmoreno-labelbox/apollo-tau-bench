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

class ProcessAccessRequestE2ETool(Tool):
    """
    process_access_request_e2e
    Comprehensive processing of an access request:
      - Assess policy (duplicate, admin-like, coverage, certifications, exceptions)
      - Document decision in the audit log
      - If granted, assign role idempotently
      - Return decision, notes, roles, active sessions for the requester, and audit log id
    """

    @staticmethod
    def invoke(data: dict[str, Any], request_id: str = None, reviewer_id: str = None) -> str:
        if not request_id or not reviewer_id:
            payload = {"error": "request_id and reviewer_id are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        # Assess policy based on current logic
        decision_raw = json.loads(
            CheckUserStatusTool.invoke(data, request_id=request_id)
        )
        if "error" in decision_raw:
            payload = decision_raw
            out = json.dumps(payload, indent=2)
            return out

        approve = bool(decision_raw.get("approve"))
        notes = decision_raw.get("notes")

        # Document decision in the audit log
        reviewed_raw = json.loads(
            ReviewAccessRequestTool.invoke(
                data,
                request_id=request_id,
                reviewer_id=reviewer_id,
                approve=approve,
                notes=notes,
            )
        )
        if "error" in reviewed_raw:
            payload = reviewed_raw
            out = json.dumps(payload, indent=2)
            return out

        # If granted, assign role idempotently
        assignment_info = None
        if approve:
            assignment_info = json.loads(
                AssignRoleOnApprovalTool.invoke(
                    data, request_id=request_id, assigned_by=reviewer_id
                )
            )

        # Gather the final state of the requester
        req = next(
            (
                r
                for r in data.get("access_requests", [])
                if r.get("request_id") == request_id
            ),
            None,
        )
        user_id = req.get("user_id") if req else None

        roles_after = [
            ur.get("role_id")
            for ur in data.get("user_roles", [])
            if user_id and ur.get("user_id") == user_id and not ur.get("expires_on")
        ]
        sessions_after = [
            s
            for s in data.get("sessions", [])
            if user_id and s.get("user_id") == user_id and not s.get("end_time")
        ]

        out = {
            "request_id": request_id,
            "user_id": user_id,
            "decision": "APPROVED" if approve else "REJECTED",
            "notes": notes,
            "roles": roles_after,
            "sessions": sessions_after,
            "audit_log_id": f"LOG-{request_id}-decision",
        }
        if assignment_info and isinstance(assignment_info, dict):
            out["assignment"] = assignment_info
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "processAccessRequestE2e",
                "description": (
                    "End-to-end processing of an access request with audit and optional assignment."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "reviewer_id": {"type": "string"},
                    },
                    "required": ["request_id", "reviewer_id"],
                },
            },
        }
