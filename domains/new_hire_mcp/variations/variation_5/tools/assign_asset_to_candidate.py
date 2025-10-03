from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timezone
from typing import Any

class AssignAssetToCandidate(Tool):
    """
    Allocate an asset_tag to a candidate:
    - inventory_assets.assigned_candidate_id_nullable = candidate_id and status='allocated'
    - candidates updated with asset_tag (optional through fields)
    """

    @staticmethod
    def invoke(data: dict[str, Any], asset_tag: str, candidate_id: str) -> str:
        inv = data.get("inventory_assets", [])
        row = next((a for a in inv if a.get("asset_tag") == asset_tag), None)
        if not row:
            payload = {"error": f"asset_tag {asset_tag} not found"}
            out = json.dumps(payload, indent=2)
            return out

        row["assigned_candidate_id_nullable"] = candidate_id
        row["status"] = "allocated"
        for c in data.get("candidates", []):
            if c.get("candidate_id") == candidate_id:
                c["allocated_asset_tag_nullable"] = asset_tag
        payload = {"asset_tag": asset_tag, "assigned_to": candidate_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assignAssetToCandidate",
                "description": "Assign inventory asset to candidate.",
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
