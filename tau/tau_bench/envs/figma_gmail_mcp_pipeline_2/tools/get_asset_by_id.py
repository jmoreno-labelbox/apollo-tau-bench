# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAssetById(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        if not kwargs.get("asset_id"):
            return json.dumps({"error": "Missing required field: asset_id"}, indent=2)

        asset_id = kwargs.get("asset_id")
        assets = data.get("assets", [])
        for row in assets:
            if row.get("asset_id") == asset_id:
                return json.dumps(row, indent=2)
        return json.dumps({"error": f"No asset with id '{asset_id}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_asset_by_id",
                "description": "Fetch a single asset object by asset_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_id": {"type": "string"}
                    },
                    "required": ["asset_id"]
                }
            }
        }
