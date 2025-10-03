from tau_bench.envs.tool import Tool
import json
from typing import Any

class record_review_approval(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], cycle_id: str, approver_email: str, intent: str
    ) -> str:
        approvals = _table(data, "review_approvals")
        cycles = _table(data, "review_cycles")

        cyc = next((c for c in cycles if c.get("cycle_id") == cycle_id), None)
        if not cyc:
            payload = {"error": f"cycle_id '{cycle_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out

        existing = next(
            (
                a
                for a in approvals
                if a.get("cycle_id") == cycle_id
                and a.get("approver_email") == approver_email
                and a.get("intent") == intent
            ),
            None,
        )
        if existing:
            payload = existing
            out = json.dumps(payload, indent=2)
            return out

        new_id = _get_next_id("approval", [a.get("approval_id", "") for a in approvals])
        row = {
            "approval_id": new_id,
            "cycle_id": cycle_id,
            "approver_email": approver_email,
            "intent": intent,
        }
        approvals.append(row)

        if intent == "APPROVE":
            count = sum(
                1
                for a in approvals
                if a.get("cycle_id") == cycle_id and a.get("intent") == "APPROVE"
            )
            cyc["approvals_recorded"] = count
        payload = row
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordReviewApproval",
                "description": "Record an approval intent (idempotent). APPROVE contributes to quorum.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"},
                        "approver_email": {"type": "string"},
                        "intent": {"type": "string"},
                    },
                    "required": ["cycle_id", "approver_email", "intent"],
                },
            },
        }
