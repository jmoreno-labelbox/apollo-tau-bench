from tau_bench.envs.tool import Tool
import json
from typing import Any

class render_asset_preview(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_id: str) -> str:
        pass
        preview_uri = f"https://previews.techcorp.com/{asset_id}_360.mp4"
        payload = {"preview_uri": preview_uri}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "renderAssetPreview",
                "description": "Renders a 360-degree turntable video preview for a given asset.",
                "parameters": {
                    "type": "object",
                    "properties": {"asset_id": {"type": "string"}},
                    "required": ["asset_id"],
                },
            },
        }
