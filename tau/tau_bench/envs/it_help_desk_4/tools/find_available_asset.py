# Copyright belongs to Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindAvailableAsset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        asset_type = kwargs.get("asset_type")
        assets = data.get("it_assets", [])
        asset = next((a for a in assets if a.get("asset_type") == asset_type and a.get("status") == "in_stock"), None)
        if not asset:
            return json.dumps({"asset_type": asset_type, "asset": None}, indent=2)
        return json.dumps(asset, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "find_available_asset", "description": "Find an available IT asset of a specific type (e.g., 'laptop').", "parameters": {"type": "object", "properties": {"asset_type": {"type": "string"}}, "required": ["asset_type"]}}}
