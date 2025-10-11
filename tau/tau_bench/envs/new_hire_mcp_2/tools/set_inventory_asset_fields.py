# Sierra copyright.

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

class SetInventoryAssetFields(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], asset_tag, fields = {}) -> str:
        rows = _ensure_list(data, "inventory_assets")
        row = _find_by_key(rows, "asset_tag", asset_tag)
        if row:
            for k, v in fields.items():
                row[k] = v
            row.setdefault("updated_ts", NOW_TS)
            return json.dumps({"asset_tag": asset_tag, "updated": True, "fields": fields}, indent=2)
        return json.dumps({"asset_tag": asset_tag, "updated": False, "reason": "not_found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "set_inventory_asset_fields",
                                                 "description": "Update fields on an inventory asset.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"asset_tag": {"type": "string"},
                                                                               "fields": {"type": "object"}},
                                                                "required": ["asset_tag", "fields"]}}}