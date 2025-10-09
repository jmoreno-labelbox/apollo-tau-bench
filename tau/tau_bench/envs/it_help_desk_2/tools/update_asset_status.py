from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateAssetStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        asset_id: str,
        status: str,
        mdm_enrolled: bool | None = None
    ) -> str:
        asset = _find_one(data["it_assets"], asset_id=asset_id)
        if not asset:
            payload = {"status": "error", "reason": "asset_not_found"}
            out = json.dumps(payload)
            return out
        asset["status"] = status
        if mdm_enrolled is not None:
            asset["mdm_enrolled"] = mdm_enrolled
        payload = {"status": "ok", "asset": asset}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAssetStatus",
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
