from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class DeprecateAssetInCatalog(Tool):
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "deprecateAssetInCatalog",
                "description": "Marks an asset in the catalog as deprecated.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_path": {"type": "string", "description": "Asset path"}
                    },
                    "required": ["asset_path"],
                },
            },
        }

    @staticmethod
    def invoke(data, asset_path=None):
        pass
        catalog = data.get("asset_catalog", [])
        row = next((a for a in catalog if a.get("asset_path") == asset_path), None)
        if not row:
            payload = {"error": "asset_not_found", "asset_path": asset_path}
            out = json.dumps(payload)
            return out
        row["validation_status"] = "deprecated"
        payload = {"asset": row}
        out = json.dumps(payload, indent=2)
        return out
