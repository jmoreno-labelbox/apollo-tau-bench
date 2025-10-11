# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _fixed_now_iso




def _fixed_now_iso():
    return datetime.utcnow().isoformat() + "Z"

class ModifyAsset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], asset_tag, updates) -> str:
        updates = updates or {}
        assets = list(data.get("inventory_assets", {}).values())
        for a in assets:
            if a.get("asset_tag") == asset_tag:
                a.update(updates)
                a["updated_at"] = _fixed_now_iso()
        return json.dumps({"updated_asset_tag": asset_tag, "updates": updates}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_asset",
            "description":"Update an inventory asset.",
            "parameters":{"type":"object","properties":{"asset_tag":{"type":"string"},"updates":{"type":"object"}},"required":["asset_tag","updates"]}
        }}