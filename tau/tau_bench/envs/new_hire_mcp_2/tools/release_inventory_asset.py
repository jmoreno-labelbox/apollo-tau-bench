# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReleaseInventoryAsset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], asset_tag) -> str:
        rows = _ensure_list(data, "inventory_assets")
        row = _find_by_key(rows, "asset_tag", asset_tag)
        if row:
            row["assigned_candidate_id_nullable"] = None
            row["status"] = "Available"
            row.setdefault("updated_ts", NOW_TS)
            return json.dumps({"asset_tag": asset_tag, "released": True}, indent=2)
        return json.dumps({"asset_tag": asset_tag, "released": False, "reason": "not_found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "release_inventory_asset",
                                                 "description": "Release an inventory asset. No-op if not found.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"asset_tag": {"type": "string"}},
                                                                "required": ["asset_tag"]}}}
