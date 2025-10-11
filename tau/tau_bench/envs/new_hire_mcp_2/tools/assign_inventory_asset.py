# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssignInventoryAsset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], asset_tag, candidate_id) -> str:
        rows = _ensure_list(data, "inventory_assets")
        row = _find_by_key(rows, "asset_tag", asset_tag)
        if row:
            row["assigned_candidate_id_nullable"] = candidate_id
            row["status"] = "Assigned"
            row.setdefault("updated_ts", NOW_TS)
            return json.dumps({"asset_tag": asset_tag, "assigned": True, "candidate_id": candidate_id}, indent=2)
        return json.dumps({"asset_tag": asset_tag, "assigned": False, "reason": "not_found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "assign_inventory_asset",
                                                 "description": "Assign an inventory asset. No-op if not found.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"asset_tag": {"type": "string"},
                                                                               "candidate_id": {"type": "string"}},
                                                                "required": ["asset_tag", "candidate_id"]}}}
