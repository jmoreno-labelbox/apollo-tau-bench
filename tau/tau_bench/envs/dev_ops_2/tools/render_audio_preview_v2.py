# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RenderAudioPreviewV2(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], files: List[str]) -> str:
        # Deterministic audio preview package: URI based on count.
        return json.dumps({"audio_preview_uri": f"artifact://audio_preview/{len(files)}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "render_audio_preview_v2", "description": "Creates deterministic audio preview URI for audio assets.", "parameters": {"type": "object", "properties": {"files": {"type": "array", "items": {"type": "string"}}}, "required": ["files"]}}}
