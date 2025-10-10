# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _fixed_now_iso


class AssignAsset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        asset_tag = kwargs.get("asset_tag")
        candidate_id = kwargs.get("candidate_id")
        assets = list(data.get("inventory_assets", {}).values())
        for a in assets:
            if a.get("asset_tag") == asset_tag:
                a["assigned_candidate_id_nullable"] = candidate_id
                a["status"] = "Assigned"
                a["updated_at"] = _fixed_now_iso()
        return json.dumps({"assigned_asset_tag": asset_tag, "candidate_id": candidate_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"assign_asset",
            "description":"Assign an asset to a candidate.",
            "parameters":{"type":"object","properties":{"asset_tag":{"type":"string"},"candidate_id":{"type":"string"}},"required":["asset_tag","candidate_id"]}
        }}
