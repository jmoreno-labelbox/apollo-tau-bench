# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _err(msg: str, code: str = "bad_request", ) -> str:
    """Creates a JSON error message."""
    out = {"error": msg, "code": code}
    if extra:
        out.update(extra)
    return json.dumps(out, indent=2)

class QueryAvailableAssetsByTypeTool(Tool):
    """Searches inventory_assets table for available assets matching specifications, with assignment status."""

    @staticmethod
    def invoke(data: Dict[str, Any], asset_type, status_filter) -> str:

        if not asset_type:
            return _err("asset_type is required")
        if not status_filter:
            return _err("status_filter is required")

        valid_statuses = {"Available", "Reserved", "Assigned", "In Repair"}
        if status_filter not in valid_statuses:
            return _err(f"Invalid status_filter. Valid statuses are: {sorted(list(valid_statuses))}")

        assets = data.get("inventory_assets", [])

        matching_assets = [
            asset for asset in assets
            if asset.get("asset_type") == asset_type and asset.get("status") == status_filter
        ]

        return json.dumps(matching_assets, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "query_available_assets_by_type",
                "description": "Searches inventory_assets table for available assets matching specifications, with assignment status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_type": {"type": "string", "description": "Equipment type needed ('Laptop', 'Phone', 'Monitor', etc.)"},
                        "status_filter": {"type": "string", "description": "Asset status ('Available', 'Reserved', 'Assigned', 'In Repair')"}
                    },
                    "required": ["asset_type", "status_filter"],
                },
            },
        }