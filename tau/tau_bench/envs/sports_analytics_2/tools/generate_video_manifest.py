# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GenerateVideoManifest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        return json.dumps({"video_manifest": "manifest_001"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "generate_video_manifest", "description": "Generates a manifest of clips.", "parameters": {"type": "object", "properties": {"insights": {"type": "string"}}, "required": ["insights"]}}}
