from tau_bench.envs.tool import Tool
import json
from typing import Any

class update_review_status_by_quorum(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], review_cycles: list[dict] = None, review_approvals: list[dict] = None, system_config: dict = None, cycle_id: str = None) -> str:
        review_cycles = review_cycles or []
        approvals = review_approvals or []
        cfg = system_config or {}

        review_cfg = {}
        if isinstance(cfg, dict):
            review_cfg = cfg.get("review_workflow_config", {}).values() or {}
        quorum = review_cfg.get("approval_quorum", 2)
        try:
            quorum = int(quorum)
        except Exception:
            quorum = 2

        cycle = None
        if isinstance(review_cycles, list):
            for row in review_cycles:
                if isinstance(row, dict) and row.get("cycle_id") == cycle_id:
                    cycle = row
                    break

        if not cycle:
            payload = {"error": f"Review cycle {cycle_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        approve_emails: list[str] = []
        if isinstance(approvals, list):
            for a in approvals:
                if not isinstance(a, dict):
                    continue
                if a.get("cycle_id") == cycle_id and a.get("intent") == "APPROVE":
                    email = a.get("approver_email")
                    if isinstance(email, str):
                        approve_emails.append(email)

        unique_reviewers = set(approve_emails)
        approvals_count = len(unique_reviewers)

        if approvals_count >= quorum:
            cycle.get("status")
            cycle["status"] = "APPROVED"
        else:
            pass

        try:
            cycle["approvals_recorded"] = approvals_count
        except Exception:
            pass
        payload = cycle
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateReviewStatusByQuorum",
                "description": "Checks unique APPROVE intents against configured quorum and sets status to APPROVED if met.",
                "parameters": {
                    "type": "object",
                    "properties": {"cycle_id": {"type": "string"}},
                    "required": ["cycle_id"],
                },
            },
        }
