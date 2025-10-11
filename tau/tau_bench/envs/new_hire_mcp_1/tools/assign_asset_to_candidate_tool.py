# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssignAssetToCandidateTool(Tool):
    """Updates inventory_assets table to assign specific asset and updates corresponding asset_requests status."""

    @staticmethod
    def invoke(data: Dict[str, Any], asset_request_id, asset_tag) -> str:

        if not asset_request_id or not asset_tag:
            return _err("asset_request_id and asset_tag are required.")

        # Locate the asset and submit a request.
        asset = next((a for a in data.get("inventory_assets", []) if a.get("asset_tag") == asset_tag), None)
        request = next((r for r in data.get("asset_requests", []) if str(r.get("request_id")) == str(asset_request_id)), None)

        if not asset:
            return _err(f"Asset with tag '{asset_tag}' not found.", code="not_found")
        if not request:
            return _err(f"Asset request '{asset_request_id}' not found.", code="not_found")

        if asset.get("status") != "Available":
            return _err(f"Asset '{asset_tag}' is not available for assignment.")

        # Allocate asset
        asset["status"] = "Assigned"
        asset["assigned_candidate_id_nullable"] = request.get("candidate_id")

        # Modification request
        request["status"] = "Completed"
        request["asset_tag_nullable"] = asset_tag
        request["updated_ts"] = HARD_TS

        result = {
            "asset": asset,
            "asset_request": request
        }

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_asset_to_candidate",
                "description": "Updates inventory_assets table to assign specific asset and updates corresponding asset_requests status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_request_id": {"type": "string", "description": "Request being fulfilled"},
                        "asset_tag": {"type": "string", "description": "Specific asset from availability search"},
                    },
                    "required": ["asset_request_id", "asset_tag"],
                },
            },
        }
