# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool










def _safe_table(data: Dict[str, Any], table: str) -> List[Dict[str, Any]]:
    """Get or create a list table."""
    return data.setdefault(table, [])

def _require_str(arg: Any, name: str) -> Optional[str]:
    """Return arg as str if valid, else None."""
    return arg if isinstance(arg, str) and arg.strip() else None

def _index_by(table: List[Dict[str, Any]], key: str) -> Dict[str, int]:
    """Build index map from key -> row_index (first occurrence)."""
    idx = {}
    for i, r in enumerate(table):
        k = r.get(key)
        if isinstance(k, str) and k not in idx:
            idx[k] = i
    return idx

def _det_id(prefix: str, parts: List[str], length: int = 8) -> str:
    """
    Deterministic ID from input parts. Stable across runs.
    """
    m = hashlib.md5()
    m.update(("|".join(parts)).encode("utf-8"))
    return f"{prefix}_{m.hexdigest()[:length]}"

class RecordReviewApprovalTool(Tool):
    """Record a reviewer decision for a cycle (deterministic approval_id)."""

    @staticmethod
    def invoke(data: Dict[str, Any], approver_email, cycle_id, decided_ts, decision, comment = "") -> str:
        cycle_id = _require_str(cycle_id, "cycle_id")
        approver_email = _require_str(approver_email, "approver_email")
        decision = _require_str(decision, "decision")  # AUTHORIZED|MODIFICATIONS_NEEDED|DENIED
        decided_ts = _require_str(decided_ts, "decided_ts")
        if not all([cycle_id, approver_email, decision, decided_ts]):
            return json.dumps({"error":"cycle_id, approver_email, decision, decided_ts required"})

        approvals = _safe_table(data, "review_approvals")
        approval_id = _det_id("appr", [cycle_id, approver_email, decided_ts, decision])
        idx = _index_by(approvals, "approval_id")
        row = {
            "approval_id": approval_id,
            "cycle_id": cycle_id,
            "approver_email": approver_email,
            "decision": decision,
            "decision_ts": decided_ts,
            "comments": comment
        }
        if approval_id in idx:
            approvals[idx[approval_id]] = row
        else:
            approvals.append(row)

        return json.dumps({"success": True, "approval_id": approval_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"record_review_approval",
            "description":"Record reviewer decision (deterministic id).",
            "parameters":{"type":"object","properties":{
                "cycle_id":{"type":"string"},
                "approver_email":{"type":"string"},
                "decision":{"type":"string","description":"APPROVED | CHANGES_REQUESTED | BLOCKED"},
                "decided_ts":{"type":"string"},
                "comment":{"type":"string"}
            },"required":["cycle_id","approver_email","decision","decided_ts"]}
        }}