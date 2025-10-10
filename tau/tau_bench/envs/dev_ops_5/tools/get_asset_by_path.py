# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAssetByPath(Tool):
    """Retrieves an asset by its file path."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        path = kwargs.get("asset_path")
        assets = data.get("asset_catalog", [])
        for asset in assets:
            if asset.get("asset_path") == path:
                return json.dumps(asset)
        return json.dumps({"error": f"Asset with path '{path}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_asset_by_path",
                "description": "Retrieves an asset by its file path.",
                "parameters": {
                    "type": "object",
                    "properties": {"asset_path": {"type": "string"}},
                    "required": ["asset_path"],
                },
            },
        }
