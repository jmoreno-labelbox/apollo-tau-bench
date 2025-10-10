# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class VideoCreation(Tool):
    @staticmethod
        # main invoke function
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # return result
        return json.dumps({"video_manifest": "manifest_001"}, indent=2)

    @staticmethod
        # info metadata
    def get_info() -> Dict[str, Any]:
        # return result
        return {"type": "function", "function": {"name": "vidMani", "description": "Creates a manifest of clips.", "parameters": {"type": "object", "properties": {"insights": {"type": "string"}}, "required": ["insights"]}}}
