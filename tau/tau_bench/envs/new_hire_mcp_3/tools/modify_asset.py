from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ModifyAsset(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], updates: dict = None, asset_tag: str = None) -> str:
        updates = updates or {}
        assets = data.get("inventory_assets", [])
        for a in assets:
            if a.get("asset_tag") == asset_tag:
                a.update(updates)
                a["updated_at"] = _fixed_now_iso()
        payload = {"updated_asset_tag": asset_tag, "updates": updates}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAsset",
                "description": "Update an inventory asset.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_tag": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["asset_tag", "updates"],
                },
            },
        }
