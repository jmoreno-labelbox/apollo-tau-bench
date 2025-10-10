# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReviewPolicyExceptionTool(Tool):
    """review_policy_exception
    Deterministically approve or reject a policy exception record by ID. Mirrors the behaviour of ReviewAccessRequestTool.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        exception_id = kwargs.get("exception_id")
        reviewer_id = kwargs.get("reviewer_id")
        approve = kwargs.get("approve")
        notes = kwargs.get("notes")

        exceptions = data.get("policy_exceptions", [])
        for pe in exceptions:
            if pe.get("exception_id") == exception_id:
                pe["status"] = "APPROVED" if approve else "DENIED"
                pe["reviewed_by"] = reviewer_id
                pe["reviewed_on"] = _HARD_TS
                if notes:
                    pe["decision_notes"] = notes
                # audit
                logs = data.setdefault("audit_logs", [])
                log_id = f"LOG-{exception_id}-decision"
                audit_entry = {
                    "log_id": log_id,
                    "actor_id": reviewer_id,
                    "action_type": "review_policy_exception",
                    "target_id": exception_id,
                    "timestamp": _HARD_TS,
                    "details": pe["status"],
                }
                existing = next((l for l in logs if l.get("log_id") == log_id), None)
                if existing:
                    existing.update(audit_entry)
                else:
                    logs.append(audit_entry)
                out = dict(pe)
                out["audit_log"] = audit_entry
                return json.dumps(out, indent=2)
        return json.dumps(
            {"error": f"Policy exception {exception_id} not found"}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "review_policy_exception",
                "description": (
                    "Approve or reject a policy exception by ID with reviewer notes."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "exception_id": {"type": "string"},
                        "reviewer_id": {"type": "string"},
                        "approve": {"type": "boolean"},
                        "notes": {"type": "string"},
                    },
                    "required": ["exception_id", "reviewer_id", "approve"],
                },
            },
        }
