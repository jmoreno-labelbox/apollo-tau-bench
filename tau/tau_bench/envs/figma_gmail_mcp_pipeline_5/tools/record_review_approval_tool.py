from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class RecordReviewApprovalTool(Tool):
    """Document a reviewer's decision for a cycle (deterministic approval_id)."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        approver_email: str = None,
        comment: str = "",
        cycle_id: str = None,
        decided_ts: str = None,
        decision: str = None
    ) -> str:
        cycle_id = _require_str(cycle_id, "cycle_id")
        approver_email = _require_str(approver_email, "approver_email")
        decision = _require_str(decision, "decision")
        decided_ts = _require_str(decided_ts, "decided_ts")
        if not all([cycle_id, approver_email, decision, decided_ts]):
            payload = {"error": "cycle_id, approver_email, decision, decided_ts required"}
            out = json.dumps(payload)
            return out

        approvals = _safe_table(data, "review_approvals")
        approval_id = _det_id("appr", [cycle_id, approver_email, decided_ts, decision])
        idx = _index_by(approvals, "approval_id")
        row = {
            "approval_id": approval_id,
            "cycle_id": cycle_id,
            "approver_email": approver_email,
            "decision": decision,
            "decision_ts": decided_ts,
            "comments": comment,
        }
        if approval_id in idx:
            approvals[idx[approval_id]] = row
        else:
            approvals.append(row)
        payload = {"success": True, "approval_id": approval_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordReviewApproval",
                "description": "Record reviewer decision (deterministic id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"},
                        "approver_email": {"type": "string"},
                        "decision": {
                            "type": "string",
                            "description": "APPROVED | CHANGES_REQUESTED | BLOCKED",
                        },
                        "decided_ts": {"type": "string"},
                        "comment": {"type": "string"},
                    },
                    "required": [
                        "cycle_id",
                        "approver_email",
                        "decision",
                        "decided_ts",
                    ],
                },
            },
        }
