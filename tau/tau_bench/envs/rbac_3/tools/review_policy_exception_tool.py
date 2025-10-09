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

class ReviewPolicyExceptionTool(Tool):
    """review_policy_exception
    Deterministically authorize or deny a policy exception record by ID. Reflects the behavior of ReviewAccessRequestTool.
    """

    @staticmethod
    def invoke(data: dict[str, Any], exception_id: str = None, reviewer_id: str = None, approve: bool = None, notes: str = None) -> str:
        exceptions = data.get("policy_exceptions", [])
        for pe in exceptions:
            if pe.get("exception_id") == exception_id:
                pe["status"] = "APPROVED" if approve else "DENIED"
                pe["reviewed_by"] = reviewer_id
                pe["reviewed_on"] = _HARD_TS
                if notes:
                    pe["decision_notes"] = notes
                # examine
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
                payload = out
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Policy exception {exception_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "reviewPolicyException",
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
