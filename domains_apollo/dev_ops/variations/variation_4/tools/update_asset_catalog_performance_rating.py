from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateAssetCatalogPerformanceRating(Tool):
    """Revise performance_rating for an asset within the asset_catalog."""

    @staticmethod
    def invoke(data: dict[str, Any], asset_path: str = None, performance_rating: str = None) -> str:
        rows = data.get("asset_catalog", [])
        idx = next(
            (i for i, r in enumerate(rows) if r.get("asset_path") == asset_path), None
        )
        if idx is None:
            payload = {"asset_catalog": None}
            out = json.dumps(payload, indent=2)
            return out
        row = rows[idx]
        row["performance_rating"] = performance_rating
        row["validation_status"] = row.get("validation_status", "failed")
        row["updated_at"] = "2025-01-27T13:35:00Z"
        row["validation_date"] = "2025-01-27T13:35:00Z"
        rows[idx] = row
        payload = {"asset_catalog": row}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAssetCatalogPerformanceRating",
                "description": "Set performance_rating for the given asset_path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_path": {"type": "string"},
                        "performance_rating": {
                            "type": "string",
                            "enum": ["low", "medium", "high"],
                        },
                    },
                    "required": ["asset_path", "performance_rating"],
                },
            },
        }
