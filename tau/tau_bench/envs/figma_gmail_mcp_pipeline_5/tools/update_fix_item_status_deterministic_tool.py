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

class UpdateFixItemStatusDeterministicTool(Tool):
    """Update a fix item status deterministically (requires explicit changed_ts)."""

    @staticmethod
    def invoke(data: Dict[str, Any], changed_ts, item_id, new_status, note = "") -> str:
        item_id = _require_str(item_id, "item_id")
        new_status = _require_str(new_status, "new_status")
        changed_ts = _require_str(changed_ts, "changed_ts")
        if not all([item_id, new_status, changed_ts]):
            return json.dumps({"error":"item_id, new_status, changed_ts required"})

        items = _safe_table(data, "fix_items")
        idx = _index_by(items, "item_id")
        if item_id not in idx:
            return json.dumps({"error": f"item_id {item_id} not found"})

        row = items[idx[item_id]]
        old = row.get("status")
        row["status"] = new_status
        row["last_updated"] = changed_ts
        hist = row.setdefault("status_history", [])
        hist.append({"from": old, "to": new_status, "changed_ts": changed_ts, "note": note})
        return json.dumps({"success": True, "item_id": item_id, "from": old, "to": new_status}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_fix_item_status_deterministic",
            "description":"Update fix item status (deterministic; requires changed_ts).",
            "parameters":{"type":"object","properties":{
                "item_id":{"type":"string"},
                "new_status":{"type":"string"},
                "changed_ts":{"type":"string"},
                "note":{"type":"string"}
            },"required":["item_id","new_status","changed_ts"]}
        }}