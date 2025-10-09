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

class QueryAvailableAssetsByTypeTool(Tool):
    """Looks through the inventory_assets table for available assets that meet specifications, along with their assignment status."""

    @staticmethod
    def invoke(data: dict[str, Any], asset_type: str = None, status_filter: str = None) -> str:
        if not asset_type:
            return _err("asset_type is required")
        if not status_filter:
            return _err("status_filter is required")

        valid_statuses = {"Available", "Reserved", "Assigned", "In Repair"}
        if status_filter not in valid_statuses:
            return _err(
                f"Invalid status_filter. Valid statuses are: {sorted(list(valid_statuses))}"
            )

        assets = data.get("inventory_assets", {}).values()

        matching_assets = [
            asset
            for asset in assets.values() if asset.get("asset_type") == asset_type
            and asset.get("status") == status_filter
        ]
        payload = matching_assets
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "QueryAvailableAssetsByType",
                "description": "Searches inventory_assets table for available assets matching specifications, with assignment status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_type": {
                            "type": "string",
                            "description": "Equipment type needed ('Laptop', 'Phone', 'Monitor', etc.)",
                        },
                        "status_filter": {
                            "type": "string",
                            "description": "Asset status ('Available', 'Reserved', 'Assigned', 'In Repair')",
                        },
                    },
                    "required": ["asset_type", "status_filter"],
                },
            },
        }
