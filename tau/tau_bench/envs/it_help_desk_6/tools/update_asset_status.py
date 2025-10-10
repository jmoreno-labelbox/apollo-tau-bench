# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAssetStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], asset_id: str, status: str, mdm_enrolled: Optional[bool] = None) -> str:
        asset = _find_one(data["it_assets"], asset_id=asset_id)
        if not asset:
            return json.dumps({"status": "error", "reason": "asset_not_found"})
        asset["status"] = status
        if mdm_enrolled is not None:
            asset["mdm_enrolled"] = mdm_enrolled
        return json.dumps({"status": "ok", "asset": asset})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_asset_status",
                "description": "Update asset status and optionally its mdm_enrolled flag.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_id": {"type": "string"},
                        "status": {"type": "string"},
                        "mdm_enrolled": {"type": "boolean"},
                    },
                    "required": ["asset_id", "status"],
                },
            },
        }
