from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UnassignAsset(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_id: str = None) -> str:
        assets = data.get("it_assets", {}).values()
        asset = next((a for a in assets.values() if a.get("asset_id") == asset_id), None)
        if not asset:
            payload = {"error": f"Asset {asset_id} not found."}
            out = json.dumps(payload, indent=2)
            return out
        asset["assigned_to"] = None
        asset["status"] = "in_stock"
        payload = asset
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UnassignAsset",
                "description": "Unassigns an IT asset from an employee and returns it to stock.",
                "parameters": {
                    "type": "object",
                    "properties": {"asset_id": {"type": "string"}},
                    "required": ["asset_id"],
                },
            },
        }
