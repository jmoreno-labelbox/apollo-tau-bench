from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ReleaseAsset(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_tag: str = None) -> str:
        assets = data.get("inventory_assets", [])
        for a in assets:
            if a.get("asset_tag") == asset_tag:
                a["assigned_candidate_id_nullable"] = None
                a["status"] = "Available"
                a["updated_at"] = _fixed_now_iso()
        payload = {"released_asset_tag": asset_tag}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReleaseAsset",
                "description": "Release an assigned asset.",
                "parameters": {
                    "type": "object",
                    "properties": {"asset_tag": {"type": "string"}},
                    "required": ["asset_tag"],
                },
            },
        }
