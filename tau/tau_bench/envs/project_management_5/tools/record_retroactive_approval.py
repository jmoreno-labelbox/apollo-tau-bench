# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RecordRetroactiveApproval(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        emergency_log_id = kwargs.get("emergency_log_id")
        approver_id = kwargs.get("approver_id")
        approval_decision = kwargs.get("approval_decision")
        comments = kwargs.get("comments", "")

        if not all([emergency_log_id, approver_id, approval_decision]):
            return json.dumps(
                {
                    "error": "emergency_log_id, approver_id, and approval_decision are required"
                }
            )

        emergency_logs = data.get("emergency_logs", [])
        change_requests = data.get("change_requests", [])

        log = next(
            (e for e in emergency_logs if e.get("log_id") == emergency_log_id), None
        )
        if not log:
            return json.dumps(
                {"error": f"Emergency log '{emergency_log_id}' not found"}
            )

        if log.get("retroactive_status") != "pending":
            return json.dumps(
                {"error": f"Emergency log already {log.get('retroactive_status')}"}
            )

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
                (c for c in change_requests if c.get("cr_id") == log.get("cr_id")), None
            )
            if cr:
                cr["requires_rollback"] = True
                cr["rollback_triggered_date"] = current_time.isoformat()

            return json.dumps(
                {
                    "error": "Retroactive approval deadline exceeded. Automatic rollback has been triggered.",
                    "deadline_was": log.get("retroactive_approval_deadline"),
                    "current_time": current_time.isoformat(),
                    "rollback_triggered": True,
                }
            )

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
                (c for c in change_requests if c.get("cr_id") == log.get("cr_id")), None
            )
            if cr:
                cr["requires_rollback"] = True
                cr["rollback_triggered_date"] = current_time.isoformat()
                log["automatic_rollback_triggered"] = True

        return json.dumps(
            {
                "success": True,
                "retroactive_approval": {
                    "log_id": emergency_log_id,
                    "decision": approval_decision,
                    "status": log["retroactive_status"],
                    "rollback_triggered": log.get(
                        "automatic_rollback_triggered", False
                    ),
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "record_retroactive_approval",
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
