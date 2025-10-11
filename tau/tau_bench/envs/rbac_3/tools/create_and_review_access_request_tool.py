# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






class ProcessAccessRequestE2ETool(Tool):
    """
    process_access_request_e2e
    End-to-end processing of an access request:
      - Evaluate policy (duplicate, admin-like, coverage, certifications, exceptions)
      - Record decision with audit log
      - If approved, assign role idempotently
      - Return decision, notes, roles and active sessions for the requester, and audit log id
    """

    @staticmethod
    def invoke(data: Dict[str, Any], request_id, reviewer_id) -> str:
        if not request_id or not reviewer_id:
            return json.dumps(
                {"error": "request_id and reviewer_id are required"}, indent=2
            )

        # Evaluate policy using existing logic
        decision_raw = json.loads(
            CheckUserStatusTool.invoke(data, request_id=request_id)
        )
        if "error" in decision_raw:
            return json.dumps(decision_raw, indent=2)

        approve = bool(decision_raw.get("approve"))
        notes = decision_raw.get("notes")

        # Record decision with audit log
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
            return json.dumps(reviewed_raw, indent=2)

        # If approved, assign role idempotently
        assignment_info = None
        if approve:
            assignment_info = json.loads(
                AssignRoleOnApprovalTool.invoke(
                    data, request_id=request_id, assigned_by=reviewer_id
                )
            )

        # Collect final requester state
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
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "process_access_request_e2e",
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

class CreateAccessRequestTool(Tool):
    """create_access_request"""

    @staticmethod
    def invoke(data: Dict[str, Any], request_id, user_id, resource_id, requested_role_id, justification) -> str:
        req = {
            "request_id": request_id,
            "user_id": user_id,
            "resource_id": resource_id,
            "role": requested_role_id,
            "requested_role_id": requested_role_id,
            "justification": justification,
            "submitted_at": _HARD_TS,
            "status": "PENDING",
            "reviewed_by": None,
            "decision_notes": None,
            "decision_at": None,
        }
        ar = data.setdefault("access_requests", [])
        existing = next(
            (r for r in ar if r.get("request_id") == req["request_id"]), None
        )
        if existing is None:
            ar.append(req)
            out = req
        else:
            out = existing
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_access_request",
                "description": "Append a new access request (status=PENDING).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "user_id": {"type": "string"},
                        "resource_id": {"type": "string"},
                        "requested_role_id": {"type": "string"},
                        "justification": {"type": "string"},
                        "submitted_at": {"type": "string"},
                    },
                    "required": [
                        "request_id",
                        "user_id",
                        "resource_id",
                        "requested_role_id",
                        "justification",
                        "submitted_at",
                    ],
                },
            },
        }

class CreateAndReviewAccessRequestTool(Tool):
    """
    create_and_review_access_request
    Create an access request and immediately review it per policy (with audit). If approved, assign role.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], justification, request_id, requested_role_id, resource_id, reviewer_id, user_id) -> str:
        justification = justification or ""

        missing = [
            k
            for k in [
                "request_id",
                "user_id",
                "resource_id",
                "requested_role_id",
                "reviewer_id",
            ]
            if not kwargs.get(k)
        ]
        if missing:
            return json.dumps(
                {"error": f"Missing required: {', '.join(missing)}"}, indent=2
            )

        # Generate if not present
        json.loads(
            CreateAccessRequestTool.invoke(
                data,
                request_id=request_id,
                user_id=user_id,
                resource_id=resource_id,
                requested_role_id=requested_role_id,
                justification=justification,
                submitted_at=_HARD_TS,
            )
        )

        # Execute the entire process utilizing the current composite.
        return ProcessAccessRequestE2ETool.invoke(
            data, request_id=request_id, reviewer_id=reviewer_id
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_and_review_access_request",
                "description": (
                    "Create an access request and process it end-to-end per policy."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "user_id": {"type": "string"},
                        "resource_id": {"type": "string"},
                        "requested_role_id": {"type": "string"},
                        "justification": {"type": "string"},
                        "reviewer_id": {"type": "string"},
                    },
                    "required": [
                        "request_id",
                        "user_id",
                        "resource_id",
                        "requested_role_id",
                        "reviewer_id",
                    ],
                },
            },
        }