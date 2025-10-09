from tau_bench.envs.tool import Tool
import html
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetAssetById(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_id: str = None) -> str:
        if not asset_id:
            payload = {"error": "Missing required field: asset_id"}
            out = json.dumps(payload, indent=2)
            return out

        assets = data.get("assets", [])
        for row in assets:
            if row.get("asset_id") == asset_id:
                payload = row
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No asset with id '{asset_id}'"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAssetById",
                "description": "Fetch a single asset object by asset_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"asset_id": {"type": "string"}},
                    "required": ["asset_id"],
                },
            },
        }
