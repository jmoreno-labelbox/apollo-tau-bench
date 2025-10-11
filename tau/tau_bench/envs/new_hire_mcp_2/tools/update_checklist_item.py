# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _find_by_key(rows: List[Dict[str, Any]], key: str, val: Any) -> Dict[str, Any]:
    for r in rows:
        if r.get(key) == val:
            return r
    return None

def _ensure_list(d: Dict[str, Any], key: str) -> List[Any]:
    if key not in d or not isinstance(d[key], list):
        d[key] = []
    return d[key]

class UpdateChecklistItem(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], item_id, fields = {}) -> str:
        rows = _ensure_list(data, "checklist_items")
        row = _find_by_key(rows, "item_id", item_id)
        if row:
            for k, v in fields.items():
                row[k] = v
            row["updated_ts"] = NOW_TS
            return json.dumps({"item_id": item_id, "updated": True, "fields": fields}, indent=2)
        return json.dumps({"item_id": item_id, "updated": False, "reason": "not_found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "update_checklist_item", "description": "Update a checklist item.",
                             "parameters": {"type": "object",
                                            "properties": {"item_id": {"type": "string"}, "fields": {"type": "object"}},
                                            "required": ["item_id", "fields"]}}}