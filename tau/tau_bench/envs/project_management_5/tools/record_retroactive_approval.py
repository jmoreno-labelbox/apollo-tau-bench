from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RecordRetroactiveApproval(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        emergency_log_id: str,
        approver_id: str,
        approval_decision: str,
        comments: str = ""
    ) -> str:
        if not all([emergency_log_id, approver_id, approval_decision]):
            payload = {
                "error": "emergency_log_id, approver_id, and approval_decision are required"
            }
            out = json.dumps(payload)
            return out

        emergency_logs = data.get("emergency_logs", {}).values()
        change_requests = data.get("change_requests", {}).values()

        log = next(
            (e for e in emergency_logs.values() if e.get("log_id") == emergency_log_id), None
        )
        if not log:
            payload = {"error": f"Emergency log '{emergency_log_id}' not found"}
            out = json.dumps(payload)
            return out

        if log.get("retroactive_status") != "pending":
            payload = {"error": f"Emergency log already {log.get('retroactive_status')}"}
            out = json.dumps(payload)
            return out

        current_time = datetime.now()
        deadline = datetime.fromisoformat(
            log.get("retroactive_approval_deadline")
            .replace("Z", "+00:00")
            .replace("+00:00", "")
        )

        if current_time > deadline:
            log["retroactive_status"] = "failed_deadline"
            log["automatic_rollback_triggered"] = True
            log["rollback_trigger_date"] = current_time.isoformat()

            cr = next(
                (c for c in change_requests.values() if c.get("cr_id") == log.get("cr_id")), None
            )
            if cr:
                cr["requires_rollback"] = True
                cr["rollback_triggered_date"] = current_time.isoformat()
            payload = {
                "error": "Retroactive approval deadline exceeded. Automatic rollback has been triggered.",
                "deadline_was": log.get("retroactive_approval_deadline"),
                "current_time": current_time.isoformat(),
                "rollback_triggered": True,
            }
            out = json.dumps(payload)
            return out

        if "retroactive_approvers" not in log:
            log["retroactive_approvers"] = []

        log["retroactive_approvers"].append(approver_id)

        if approval_decision == "approve":
            log["retroactive_status"] = "approved"
            log["retroactive_approval_date"] = current_time.isoformat()
            log["approval_comments"] = comments
        else:
            log["retroactive_status"] = "rejected"
            log["retroactive_rejection_date"] = current_time.isoformat()
            log["rejection_comments"] = comments

            cr = next(
                (c for c in change_requests.values() if c.get("cr_id") == log.get("cr_id")), None
            )
            if cr:
                cr["requires_rollback"] = True
                cr["rollback_triggered_date"] = current_time.isoformat()
                log["automatic_rollback_triggered"] = True
        payload = {
            "success": True,
            "retroactive_approval": {
                "log_id": emergency_log_id,
                "decision": approval_decision,
                "status": log["retroactive_status"],
                "rollback_triggered": log.get("automatic_rollback_triggered", False),
            },
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordRetroactiveApproval",
                "description": "Record retroactive approval for emergency changes",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "emergency_log_id": {
                            "type": "string",
                            "description": "Emergency log ID",
                        },
                        "approver_id": {
                            "type": "string",
                            "description": "Retroactive approver ID",
                        },
                        "approval_decision": {
                            "type": "string",
                            "description": "Decision: approve or reject",
                        },
                        "comments": {
                            "type": "string",
                            "description": "Approval comments",
                        },
                    },
                    "required": [
                        "emergency_log_id",
                        "approver_id",
                        "approval_decision",
                    ],
                },
            },
        }
