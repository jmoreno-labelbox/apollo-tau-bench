# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReleaseAsset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        asset_tag = kwargs.get("asset_tag")
        assets = data.get("inventory_assets", [])
        for a in assets:
            if a.get("asset_tag") == asset_tag:
                a["assigned_candidate_id_nullable"] = None
                a["status"] = "Available"
                a["updated_at"] = _fixed_now_iso()
        return json.dumps({"released_asset_tag": asset_tag}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"release_asset",
            "description":"Release an assigned asset.",
            "parameters":{"type":"object","properties":{"asset_tag":{"type":"string"}},"required":["asset_tag"]}
        }}
