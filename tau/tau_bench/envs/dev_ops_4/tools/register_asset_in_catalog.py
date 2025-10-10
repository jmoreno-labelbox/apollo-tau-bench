# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RegisterAssetInCatalog(Tool):
    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "register_asset_in_catalog",
                "description": "Registers or updates an asset in the catalog.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_path": {"type": "string", "description": "Asset path"},
                        "asset_type": {"type": "string", "description": "Asset type"},
                        "validation_status": {"type": "string", "description": "Validation status"},
                        "performance_rating": {"type": "string", "description": "Performance rating"}
                    },
                    "required": ["asset_path", "asset_type", "validation_status"]
                }
            }
        }

    @staticmethod
    def invoke(data, asset_path, asset_type, performance_rating, validation_status):
        catalog = list(data.get("asset_catalog", {}).values())
        row = next((a for a in catalog if a.get("asset_path") == asset_path), None)
        if row:
            row["asset_type"] = asset_type
            row["validation_status"] = validation_status
            if performance_rating is not None:
                row["performance_rating"] = performance_rating
        else:
            catalog.append({"asset_path": asset_path, "asset_type": asset_type, "validation_status": validation_status, "performance_rating": performance_rating})
        data["asset_catalog"] = catalog
        return json.dumps({"asset": next(a for a in catalog if a.get("asset_path") == asset_path)}, indent=2)
