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

class ReserveInventoryAsset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], asset_tag, candidate_id) -> str:
        rows = _ensure_list(data, "inventory_assets")
        row = _find_by_key(rows, "asset_tag", asset_tag)
        if row:
            row["assigned_candidate_id_nullable"] = candidate_id
            row["status"] = "Reserved"
            row.setdefault("updated_ts", NOW_TS)
            return json.dumps({"asset_tag": asset_tag, "reserved": True, "candidate_id": candidate_id}, indent=2)
        return json.dumps({"asset_tag": asset_tag, "reserved": False, "reason": "not_found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "reserve_inventory_asset",
                                                 "description": "Reserve an inventory asset for a candidate.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"asset_tag": {"type": "string"},
                                                                               "candidate_id": {"type": "string"}},
                                                                "required": ["asset_tag", "candidate_id"]}}}