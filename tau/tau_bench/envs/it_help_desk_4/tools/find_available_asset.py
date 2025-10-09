from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FindAvailableAsset(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_type: str = None) -> str:
        assets = data.get("it_assets", {}).values()
        asset = next(
            (
                a
                for a in assets.values() if a.get("asset_type") == asset_type and a.get("status") == "in_stock"
            ),
            None,
        )
        if not asset:
            payload = {"asset_type": asset_type, "asset": None}
            out = json.dumps(payload, indent=2)
            return out
        payload = asset
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindAvailableAsset",
                "description": "Find an available IT asset of a specific type (e.g., 'laptop').",
                "parameters": {
                    "type": "object",
                    "properties": {"asset_type": {"type": "string"}},
                    "required": ["asset_type"],
                },
            },
        }
