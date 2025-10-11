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

class LinkReviewToThreadTool(Tool):
    """Link a review cycle to a Gmail thread (idempotent)."""

    @staticmethod
    def invoke(data: Dict[str, Any], changed_ts, cycle_id, thread_id) -> str:
        cycle_id = _require_str(cycle_id, "cycle_id")
        thread_id = _require_str(thread_id, "thread_id")
        changed_ts = _require_str(changed_ts, "changed_ts")
        if not (cycle_id and thread_id and changed_ts):
            return json.dumps({"error":"cycle_id, thread_id, changed_ts required"})

        cycles = _safe_table(data, "review_cycles")
        idx = _index_by(cycles, "cycle_id")
        if cycle_id not in idx:
            return json.dumps({"error": f"cycle_id {cycle_id} not found"})

        cycles[idx[cycle_id]]["thread_id_nullable"] = thread_id
        cycles[idx[cycle_id]]["last_updated"] = changed_ts
        return json.dumps({"success": True, "cycle_id": cycle_id, "thread_id": thread_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"link_review_to_thread",
            "description":"Link review cycle to Gmail thread (idempotent).",
            "parameters":{"type":"object","properties":{
                "cycle_id":{"type":"string"},
                "thread_id":{"type":"string"},
                "changed_ts":{"type":"string"}
            },"required":["cycle_id","thread_id","changed_ts"]}
        }}