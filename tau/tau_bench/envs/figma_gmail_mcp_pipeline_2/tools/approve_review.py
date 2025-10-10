# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ApproveReview(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required = ["cycle_id", "approver_email"]
        missing = [f for f in required if f not in kwargs or kwargs[f] is None]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        cycle_id = kwargs.get("cycle_id")
        approver_email = kwargs.get("approver_email")
        approval_comment_ref: Optional[str] = kwargs.get("approval_comment_ref")

        approvals: List[Dict[str, Any]] = data.get("review_approvals", [])
        cycles: List[Dict[str, Any]] = list(data.get("review_cycles", {}).values())

        cycle = None
        for row in cycles:
            if row.get("cycle_id") == cycle_id:
                cycle = row
                break
        if not cycle:
            return json.dumps({"error": f"No cycle with id '{cycle_id}'"}, indent=2)

        now_ts = get_now_timestamp()
        deadline_ts = cycle.get("sla_deadline_ts")
        if deadline_ts is not None and str(now_ts) > str(deadline_ts):
            cycle["sla_breached_flag"] = True
        else:
            cycle["sla_breached_flag"] = False

        sla_breached_flag = bool(cycle.get("sla_breached_flag"))
        ts = get_now_timestamp()
        approval_id = get_next_approve_id(data)

        new_approval = {
            "approval_id": approval_id,
            "cycle_id": cycle_id,
            "approver_email": approver_email,
            "approved_ts": ts,
            "sla_breached_flag": sla_breached_flag,
            "approval_comment_ref_nullable": approval_comment_ref
        }

        approvals.append(new_approval)
        cycle["status"] = "APPROVED"

        data["review_approvals"] = approvals
        data["review_cycles"] = cycles

        return json.dumps({"approval": new_approval, "cycle": cycle}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "approve_review",
                "description": "Approve a review cycle; recompute and set the SLA-breached flag by comparing sla_deadline_ts with the current timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"},
                        "approver_email": {"type": "string"},
                        "approval_comment_ref": {"type": ["string", "null"]}
                    },
                    "required": ["cycle_id", "approver_email"]
                }
            }
        }
