from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta

class ReviewAccessRequestTool(Tool):
    """Authorize or deny an access request with reviewer comments (deterministic decision_at + returns audit data)."""

    @staticmethod
    def invoke(data: dict[str, Any], request_id: str = None, reviewer_id: str = None, approve: bool = None, notes: str = None) -> str:
        requests = data.get("access_requests", [])
        for req in requests:
            if req.get("request_id") == request_id:
                req["status"] = "APPROVED" if approve else "REJECTED"
                req["reviewed_by"] = reviewer_id
                req["decision_notes"] = notes
                req["decision_at"] = _HARD_TS
                # Idempotent audit record to prevent downstream lists/filters from appearing
                # clear out
                logs = data.setdefault("audit_logs", [])
                log_id = f"LOG-{request_id}-decision"
                audit_entry = {
                    "log_id": log_id,
                    "actor_id": reviewer_id,
                    "action_type": "ReviewAccessRequest",
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
                # Include subject and body as specified
                status = req["status"]
                out["subject"] = f"{request_id} {status}"
                out["body"] = f"{reviewer_id} {_HARD_TS}"
                payload = out
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Access request {request_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReviewAccessRequest",
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
