# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _table(data: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    tbl = data.get(name)
    if not isinstance(tbl, list):
        tbl = []
        data[name] = tbl
    return tbl

def _get_next_id(prefix: str, existing_ids: List[str]) -> str:
    max_id_num = 0
    seen = False
    for s in existing_ids:
        if isinstance(s, str) and s.startswith(prefix + "_"):
            seen = True
            try:
                n = int(s.split("_")[-1])
                if n > max_id_num:
                    max_id_num = n
            except Exception:
                pass
    return f"{prefix}_{(1 if not seen else max_id_num + 1):03d}"

class record_review_approval(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cycle_id: str, approver_email: str, intent: str) -> str:
        approvals = _table(data, "review_approvals")
        cycles = _table(data, "review_cycles")

        cyc = next((c for c in cycles if c.get("cycle_id") == cycle_id), None)
        if not cyc:
            return json.dumps({"error": f"cycle_id '{cycle_id}' not found"}, indent=2)

        existing = next(
            (a for a in approvals
             if a.get("cycle_id") == cycle_id
             and a.get("approver_email") == approver_email
             and a.get("intent") == intent),
            None
        )
        if existing:
            return json.dumps(existing, indent=2)

        new_id = _get_next_id("approval", [a.get("approval_id", "") for a in approvals])
        row = {
            "approval_id": new_id,
            "cycle_id": cycle_id,
            "approver_email": approver_email,
            "intent": intent,
        }
        approvals.append(row)

        if intent == "APPROVE":
            count = sum(1 for a in approvals if a.get("cycle_id") == cycle_id and a.get("intent") == "APPROVE")
            cyc["approvals_recorded"] = count

        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "record_review_approval",
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