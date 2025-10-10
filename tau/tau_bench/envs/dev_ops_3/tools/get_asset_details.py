# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_asset_details(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], asset_id: str) -> str:
        assets = data.get("asset_catalog", [])
        for asset in assets:
            if asset.get("id") == asset_id:
                return json.dumps(asset, indent=2)
        return json.dumps({"error": f"Asset with id '{asset_id}' not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return { "type": "function", "function": { "name": "get_asset_details", "description": "Retrieves the full details for a given asset from the asset catalog.", "parameters": { "type": "object", "properties": { "asset_id": { "type": "string" } }, "required": ["asset_id"] } } }
