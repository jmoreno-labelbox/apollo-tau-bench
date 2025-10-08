from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetAssetByPath(Tool):
    """Fetches an asset using its file path."""

    @staticmethod
    def invoke(data: dict[str, Any], asset_path: str = None) -> str:
        path = asset_path
        assets = data.get("asset_catalog", [])
        for asset in assets:
            if asset.get("asset_path") == path:
                payload = asset
                out = json.dumps(payload)
                return out
        payload = {"error": f"Asset with path '{path}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAssetByPath",
                "description": "Retrieves an asset by its file path.",
                "parameters": {
                    "type": "object",
                    "properties": {"asset_path": {"type": "string"}},
                    "required": ["asset_path"],
                },
            },
        }
