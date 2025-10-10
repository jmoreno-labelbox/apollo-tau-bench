# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAssetValidationStatus(Tool):
    """Updates the validation status of an asset."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        asset_id = kwargs.get("id")
        new_status = kwargs.get("validation_status")
        assets = data.get("asset_catalog", [])
        for asset in assets:
            if asset.get("id") == asset_id:
                asset["validation_status"] = new_status
                return json.dumps({"status": "success", "message": f"Validation status for asset '{asset_id}' updated to '{new_status}'."})
        return json.dumps({"error": f"Asset with ID '{asset_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_asset_validation_status",
                "description": "Updates the validation status of an asset.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "validation_status": {"type": "string"}
                    },
                    "required": ["id", "validation_status"],
                },
            },
        }
