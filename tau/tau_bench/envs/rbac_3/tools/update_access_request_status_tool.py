# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




class ReviewAccessRequestTool(Tool):
    """Approve or reject an access request with reviewer notes (deterministic decision_at + returns audit payload)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        request_id = kwargs.get("request_id")
        reviewer_id = kwargs.get("reviewer_id")
        approve = kwargs.get("approve")
        notes = kwargs.get("notes")

        requests = data.get("access_requests", [])
        for req in requests:
            if req.get("request_id") == request_id:
                req["status"] = "APPROVED" if approve else "REJECTED"
                req["reviewed_by"] = reviewer_id
                req["decision_notes"] = notes
                req["decision_at"] = _HARD_TS
                # Idempotent audit entry so downstream list/filters never come
                # up empty
                logs = data.setdefault("audit_logs", [])
                log_id = f"LOG-{request_id}-decision"
                audit_entry = {
                    "log_id": log_id,
                    "actor_id": reviewer_id,
                    "action_type": "review_access_request",
                    "target_id": request_id,
                    "timestamp": _HARD_TS,
                    "details": req["status"],
                }
                existing = next((l for l in logs if l.get("log_id") == log_id), None)
                if existing:
                    existing.update(audit_entry)
                else:
                    logs.append(audit_entry)
                out = dict(req)
                out["audit_log"] = audit_entry
                # Add subject and body as requested
                status = req["status"]
                out["subject"] = f"{request_id} {status}"
                out["body"] = f"{reviewer_id} {_HARD_TS}"
                return json.dumps(out, indent=2)

        return json.dumps({"error": f"Access request {request_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "review_access_request",
                "description": (
                    "Approve or reject an access request by ID with reviewer notes."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {
                            "type": "string",
                            "description": "Unique request identifier",
                        },
                        "reviewer_id": {
                            "type": "string",
                            "description": "Reviewer's user ID (e.g., U-010)",
                        },
                        "approve": {
                            "type": "boolean",
                            "description": "True to approve, False to reject",
                        },
                        "notes": {
                            "type": "string",
                            "description": "Decision notes explaining the reason",
                        },
                        "decision_at": {
                            "type": "string",
                            "description": (
                                "ISO 8601 timestamp of the decision (pass explicitly for determinism)"
                            ),
                        },
                    },
                    "required": ["request_id", "reviewer_id", "approve", "notes"],
                },
            },
        }

class UpdateAccessRequestStatusTool(Tool):
    """update_access_request_status: approve/reject with notes and audit."""

    @staticmethod
    def invoke(data: Dict[str, Any], approve, notes, request_id, reviewer_id, status) -> str:
        if status is not None and approve is None:
            approve = True if str(status).upper() == "APPROVED" else False
        return ReviewAccessRequestTool.invoke(
            data,
            request_id=request_id,
            reviewer_id=reviewer_id,
            approve=approve,
            notes=notes,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_access_request_status",
                "description": (
                    "Approve or reject an access request with reviewer notes and audit."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "reviewer_id": {"type": "string"},
                        "approve": {"type": "boolean"},
                        "status": {"type": "string"},
                        "notes": {"type": "string"},
                    },
                    "required": ["request_id", "reviewer_id"],
                },
            },
        }