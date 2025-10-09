from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RegisterAssetInCatalog(Tool):
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "RegisterAssetInCatalog",
                "description": "Registers or updates an asset in the catalog.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_path": {"type": "string", "description": "Asset path"},
                        "asset_type": {"type": "string", "description": "Asset type"},
                        "validation_status": {
                            "type": "string",
                            "description": "Validation status",
                        },
                        "performance_rating": {
                            "type": "string",
                            "description": "Performance rating",
                        },
                    },
                    "required": ["asset_path", "asset_type", "validation_status"],
                },
            },
        }

    @staticmethod
    def invoke(data, asset_path=None, asset_type=None, validation_status=None, performance_rating=None, asset_name=None):
        # Support asset_name as an alternative to asset_path
        if asset_name is not None:
            asset_path = asset_name
        catalog = data.get("asset_catalog", {}).values()
        row = next((a for a in catalog.values() if a.get("asset_path") == asset_path), None)
        if row:
            row["asset_type"] = asset_type
            row["validation_status"] = validation_status
            if performance_rating is not None:
                row["performance_rating"] = performance_rating
        else:
            catalog.append(
                {
                    "asset_path": asset_path,
                    "asset_type": asset_type,
                    "validation_status": validation_status,
                    "performance_rating": performance_rating,
                }
            )
        data["asset_catalog"] = catalog
        payload = {"asset": next(a for a in catalog.values() if a.get("asset_path") == asset_path)}
        out = json.dumps(
            payload, indent=2,
        )
        return out
