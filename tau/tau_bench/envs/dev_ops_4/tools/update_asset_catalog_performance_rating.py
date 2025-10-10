# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAssetCatalogPerformanceRating(Tool):
    """Update performance_rating for an asset in the asset_catalog."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        asset_path = kwargs.get("asset_path")
        performance_rating = kwargs.get("performance_rating")
        rows = data.get("asset_catalog", [])
        idx = next((i for i, r in enumerate(rows) if r.get("asset_path") == asset_path), None)
        if idx is None:
            return json.dumps({"asset_catalog": None}, indent=2)
        row = rows[idx]
        row["performance_rating"] = performance_rating
        row["validation_status"] = row.get("validation_status", "failed")
        row["updated_at"] = "2025-01-27T13:35:00Z"
        row["validation_date"] = "2025-01-27T13:35:00Z"
        rows[idx] = row
        return json.dumps({"asset_catalog": row}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_asset_catalog_performance_rating",
                "description": "Set performance_rating for the given asset_path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_path": {"type": "string"},
                        "performance_rating": {"type": "string", "enum": ["low", "medium", "high"]}
                    },
                    "required": ["asset_path", "performance_rating"]
                }
            }
        }
