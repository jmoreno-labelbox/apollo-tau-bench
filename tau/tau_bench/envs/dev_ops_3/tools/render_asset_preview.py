# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class render_asset_preview(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], asset_id: str) -> str:
        preview_uri = f"https://previews.techcorp.com/{asset_id}_360.mp4"
        return json.dumps({"preview_uri": preview_uri}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return { "type": "function", "function": { "name": "render_asset_preview", "description": "Renders a 360-degree turntable video preview for a given asset.", "parameters": { "type": "object", "properties": { "asset_id": { "type": "string" } }, "required": ["asset_id"] } } }
