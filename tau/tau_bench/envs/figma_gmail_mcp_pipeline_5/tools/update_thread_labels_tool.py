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

class UpdateThreadLabelsTool(Tool):
    """Update Gmail thread labels deterministically (idempotent)."""

    @staticmethod
    def invoke(data: Dict[str, Any], changed_ts, thread_id, add_labels = [], remove_labels = []) -> str:
        thread_id = _require_str(thread_id, "thread_id")
        add_labels = add_labels or []
        remove_labels = remove_labels or []
        changed_ts = _require_str(changed_ts, "changed_ts")
        if not (thread_id and changed_ts):
            return json.dumps({"error":"thread_id and changed_ts required"})

        threads = _safe_table(data, "gmail_threads")
        idx = _index_by(threads, "thread_id")
        if thread_id not in idx:
            return json.dumps({"error": f"thread_id {thread_id} not found"})

        row = threads[idx[thread_id]]
        labels: List[str] = list(row.get("current_labels", []))
        for lab in add_labels:
            if lab not in labels:
                labels.append(lab)
        for lab in remove_labels:
            if lab in labels:
                labels.remove(lab)
        row["current_labels"] = labels
        row["updated_ts"] = changed_ts

        return json.dumps({"success": True, "thread_id": thread_id, "labels": labels}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_thread_labels",
            "description":"Add/remove labels on a Gmail thread (idempotent). Requires explicit 'changed_ts'.",
            "parameters":{"type":"object","properties":{
                "thread_id":{"type":"string"},
                "add_labels":{"type":"array","items":{"type":"string"}},
                "remove_labels":{"type":"array","items":{"type":"string"}},
                "changed_ts":{"type":"string"}
            },"required":["thread_id","changed_ts"]}
        }}