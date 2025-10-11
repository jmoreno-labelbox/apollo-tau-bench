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

class AdvanceReviewStatusTool(Tool):
    """Advance review cycle status with allowed transitions; deterministic (requires changed_ts)."""

    ALLOWED = {
        "IN_FLIGHT": {"NEEDS_REVIEW","ESCALATED"},
        "NEEDS_REVIEW": {"APPROVED","CHANGES_REQUESTED","ESCALATED"},
        "CHANGES_REQUESTED": {"NEEDS_REVIEW","ESCALATED"},
        "ESCALATED": {"NEEDS_REVIEW","APPROVED","CHANGES_REQUESTED"},
        "APPROVED": set()
    }

    @staticmethod
    def invoke(data: Dict[str, Any], changed_ts, cycle_id, new_status, allow_override = False) -> str:
        cycle_id = _require_str(cycle_id, "cycle_id")
        new_status = _require_str(new_status, "new_status")
        changed_ts = _require_str(changed_ts, "changed_ts")
        allow_override = bool(allow_override)
        if not (cycle_id and new_status and changed_ts):
            return json.dumps({"error":"cycle_id, new_status, changed_ts required"})

        cycles = _safe_table(data, "review_cycles")
        idx = _index_by(cycles, "cycle_id")
        if cycle_id not in idx:
            return json.dumps({"error": f"cycle_id {cycle_id} not found"})

        row = cycles[idx[cycle_id]]
        old = row.get("status")
        if not allow_override and new_status not in AdvanceReviewStatusTool.ALLOWED.get(old, set()):
            return json.dumps({"error": f"transition {old} -> {new_status} not allowed"})

        row["status"] = new_status
        row["last_updated"] = changed_ts
        return json.dumps({"success": True, "cycle_id": cycle_id, "from": old, "to": new_status}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"advance_review_status",
            "description":"Advance review status with allowed transitions (override optional). Requires changed_ts.",
            "parameters":{"type":"object","properties":{
                "cycle_id":{"type":"string"},
                "new_status":{"type":"string"},
                "changed_ts":{"type":"string"},
                "allow_override":{"type":"boolean"}
            },"required":["cycle_id","new_status","changed_ts"]}
        }}