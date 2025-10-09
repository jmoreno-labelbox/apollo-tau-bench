from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class get_asset_details(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_id: str) -> str:
        pass
        assets = data.get("asset_catalog", {}).values()
        for asset in assets.values():
            if asset.get("id") == asset_id:
                payload = asset
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Asset with id '{asset_id}' not found"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAssetDetails",
                "description": "Retrieves the full details for a given asset from the asset catalog.",
                "parameters": {
                    "type": "object",
                    "properties": {"asset_id": {"type": "string"}},
                    "required": ["asset_id"],
                },
            },
        }
