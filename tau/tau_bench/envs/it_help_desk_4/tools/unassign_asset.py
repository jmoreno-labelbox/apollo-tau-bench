# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UnassignAsset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], asset_id) -> str:
        assets = list(data.get("it_assets", {}).values())
        asset = next((a for a in assets if a.get("asset_id") == asset_id), None)
        if not asset:
            return json.dumps({"error": f"Asset {asset_id} not found."}, indent=2)
        asset["assigned_to"] = None
        asset["status"] = "in_stock"
        return json.dumps(asset, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "unassign_asset", "description": "Unassigns an IT asset from an employee and returns it to stock.", "parameters": {"type": "object", "properties": {"asset_id": {"type": "string"}}, "required": ["asset_id"]}}}
