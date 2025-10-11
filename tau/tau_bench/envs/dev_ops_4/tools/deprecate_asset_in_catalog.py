# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeprecateAssetInCatalog(Tool):
    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "deprecate_asset_in_catalog",
                "description": "Marks an asset in the catalog as deprecated.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_path": {"type": "string", "description": "Asset path"}
                    },
                    "required": ["asset_path"]
                }
            }
        }

    @staticmethod
    def invoke(data, asset_path):
        catalog = list(data.get("asset_catalog", {}).values())
        row = next((a for a in catalog if a.get("asset_path") == asset_path), None)
        if not row:
            return json.dumps({"error": "asset_not_found", "asset_path": asset_path})
        row["validation_status"] = "deprecated"
        return json.dumps({"asset": row}, indent=2)
