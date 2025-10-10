# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class update_review_status_by_quorum(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cycle_id: str) -> str:
        review_cycles = data.get("review_cycles", [])
        approvals = data.get("review_approvals", [])
        cfg = data.get("system_config", {}) or {}

        review_cfg = {}
        if isinstance(cfg, dict):
            review_cfg = cfg.get("review_workflow_config", {}) or {}
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
            return json.dumps({"error": f"Review cycle {cycle_id} not found"}, indent=2)

        approve_emails: List[str] = []
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
            old = cycle.get("status")
            cycle["status"] = "APPROVED"
        else:
            pass

        try:
            cycle["approvals_recorded"] = approvals_count
        except Exception:
            pass

        return json.dumps(cycle, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_review_status_by_quorum",
                "description": "Checks unique APPROVE intents against configured quorum and sets status to APPROVED if met.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"}
                    },
                    "required": ["cycle_id"],
                },
            },
        }
