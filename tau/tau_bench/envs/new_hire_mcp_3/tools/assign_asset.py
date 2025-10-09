from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AssignAsset(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_tag: str = None, candidate_id: str = None) -> str:
        assets = data.get("inventory_assets", [])
        for a in assets:
            if a.get("asset_tag") == asset_tag:
                a["assigned_candidate_id_nullable"] = candidate_id
                a["status"] = "Assigned"
                a["updated_at"] = _fixed_now_iso()
        payload = {"assigned_asset_tag": asset_tag, "candidate_id": candidate_id}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignAsset",
                "description": "Assign an asset to a candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_tag": {"type": "string"},
                        "candidate_id": {"type": "string"},
                    },
                    "required": ["asset_tag", "candidate_id"],
                },
            },
        }
