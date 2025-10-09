from tau_bench.envs.tool import Tool
import html
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ApproveReview(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cycle_id: str = None, approver_email: str = None, approval_comment_ref: str = None) -> str:
        required = ["cycle_id", "approver_email"]
        params_dict = {k: v for k, v in locals().items() if k != "data"}

        missing = [f for f in required if params_dict.get(f) is None]
        if missing:
            payload = {"error": f"Missing required fields: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        approvals: list[dict[str, Any]] = data.get("review_approvals", [])
        cycles: list[dict[str, Any]] = data.get("review_cycles", [])

        cycle = None
        for row in cycles:
            if row.get("cycle_id") == cycle_id:
                cycle = row
                break
        if not cycle:
            payload = {"error": f"No cycle with id '{cycle_id}'"}
            out = json.dumps(payload, indent=2)
            return out

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
            "approval_comment_ref_nullable": approval_comment_ref,
        }

        approvals.append(new_approval)
        cycle["status"] = "APPROVED"

        data["review_approvals"] = approvals
        data["review_cycles"] = cycles
        payload = {"approval": new_approval, "cycle": cycle}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApproveReview",
                "description": "Approve a review cycle; recompute and set the SLA-breached flag by comparing sla_deadline_ts with the current timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"},
                        "approver_email": {"type": "string"},
                        "approval_comment_ref": {"type": ["string", "null"]},
                    },
                    "required": ["cycle_id", "approver_email"],
                },
            },
        }
