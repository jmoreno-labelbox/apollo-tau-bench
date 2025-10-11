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

class UpdateAssetRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], request_id, fields = {}) -> str:
        rows = _ensure_list(data, "asset_requests")
        row = _find_by_key(rows, "request_id", request_id)
        if row:
            for k, v in fields.items():
                row[k] = v
            row.setdefault("updated_ts", NOW_TS)
            return json.dumps({"request_id": request_id, "updated": True, "fields": fields}, indent=2)
        return json.dumps({"request_id": request_id, "updated": False, "reason": "not_found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_asset_request",
                                                 "description": "Update existing asset_requests row. No-op if not found.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"request_id": {"type": "string"},
                                                                               "fields": {"type": "object"}},
                                                                "required": ["request_id", "fields"]}}}