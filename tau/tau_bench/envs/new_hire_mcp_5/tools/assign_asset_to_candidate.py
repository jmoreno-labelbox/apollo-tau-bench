# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssignAssetToCandidate(Tool):
    """
    Assign an asset_tag to a candidate:
    - inventory_assets.assigned_candidate_id_nullable = candidate_id and status='allocated'
    - candidates updated with asset_tag (optional via fields)
    """

    @staticmethod
    def invoke(data: Dict[str, Any], asset_tag, candidate_id) -> str:
        cand_id = candidate_id

        inv = data.get("inventory_assets", [])
        row = next((a for a in inv if a.get("asset_tag") == asset_tag), None)
        if not row:
            return json.dumps({"error": f"asset_tag {asset_tag} not found"}, indent=2)

        row["assigned_candidate_id_nullable"] = cand_id
        row["status"] = "allocated"
        for c in list(data.get("candidates", {}).values()):
            if c.get("candidate_id") == cand_id:
                c["allocated_asset_tag_nullable"] = asset_tag
        return json.dumps({"asset_tag": asset_tag, "assigned_to": cand_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_asset_to_candidate",
                "description": "Assign inventory asset to candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_tag": {"type": "string"},
                        "candidate_id": {"type": "string"}
                    },
                    "required": ["asset_tag", "candidate_id"]
                }
            }
        }
