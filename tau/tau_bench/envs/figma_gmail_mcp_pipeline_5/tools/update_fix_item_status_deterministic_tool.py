# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateFixItemStatusDeterministicTool(Tool):
    """Update a fix item status deterministically (requires explicit changed_ts)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        item_id = _require_str(kwargs.get("item_id"), "item_id")
        new_status = _require_str(kwargs.get("new_status"), "new_status")
        changed_ts = _require_str(kwargs.get("changed_ts"), "changed_ts")
        note = kwargs.get("note","")
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
