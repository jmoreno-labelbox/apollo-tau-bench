from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateAssetValidationStatus(Tool):
    """Modifies the validation status of an asset."""

    def invoke(
        data: dict[str, Any],
        asset_id: str = None,
        id: Any = None,
        new_status: str = None
    ) -> str:
        assets = data.get("asset_catalog", {}).values()
        for asset in assets.values():
            if asset.get("id") == asset_id:
                asset["validation_status"] = new_status
                payload = {
                    "status": "success",
                    "message": f"Validation status for asset '{asset_id}' updated to '{new_status}'.",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Asset with ID '{asset_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateAssetValidationStatus",
                "description": "Updates the validation status of an asset.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "validation_status": {"type": "string"},
                    },
                    "required": ["id", "validation_status"],
                },
            },
        }
