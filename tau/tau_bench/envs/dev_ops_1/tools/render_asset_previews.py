# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RenderAssetPreviews(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], files: List[str]) -> str:
        previews = {"turntable_uri": f"artifact://turntable/{len(files)}", "stills_uris": [f"artifact://still/{i}" for i, _ in enumerate(files, start=1)]}
        return json.dumps(previews, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "render_asset_previews", "description": "Creates deterministic preview URIs for assets.", "parameters": {"type": "object", "properties": {"files": {"type": "array", "items": {"type": "string"}}}, "required": ["files"]}}}
