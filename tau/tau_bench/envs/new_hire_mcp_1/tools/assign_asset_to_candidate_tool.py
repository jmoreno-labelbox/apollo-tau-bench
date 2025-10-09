from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AssignAssetToCandidateTool(Tool):
    """Refreshes the inventory_assets table to allocate a specific asset and updates the status of related asset_requests."""

    @staticmethod
    def invoke(data: dict[str, Any], asset_request_id: str = None, asset_tag: str = None) -> str:
        if not asset_request_id or not asset_tag:
            return _err("asset_request_id and asset_tag are required.")

        # Locate asset and request
        asset = next(
            (
                a
                for a in data.get("inventory_assets", {}).values()
                if a.get("asset_tag") == asset_tag
            ),
            None,
        )
        request = next(
            (
                r
                for r in data.get("asset_requests", {}).values()
                if str(r.get("request_id")) == str(asset_request_id)
            ),
            None,
        )

        if not asset:
            return _err(f"Asset with tag '{asset_tag}' not found.", code="not_found")
        if not request:
            return _err(
                f"Asset request '{asset_request_id}' not found.", code="not_found"
            )

        if asset.get("status") != "Available":
            return _err(f"Asset '{asset_tag}' is not available for assignment.")

        # Allocate asset
        asset["status"] = "Assigned"
        asset["assigned_candidate_id_nullable"] = request.get("candidate_id")

        # Refresh request
        request["status"] = "Completed"
        request["asset_tag_nullable"] = asset_tag
        request["updated_ts"] = HARD_TS

        result = {"asset": asset, "asset_request": request}
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignAssetToCandidate",
                "description": "Updates inventory_assets table to assign specific asset and updates corresponding asset_requests status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_request_id": {
                            "type": "string",
                            "description": "Request being fulfilled",
                        },
                        "asset_tag": {
                            "type": "string",
                            "description": "Specific asset from availability search",
                        },
                    },
                    "required": ["asset_request_id", "asset_tag"],
                },
            },
        }
