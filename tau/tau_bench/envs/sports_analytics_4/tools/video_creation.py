# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class VideoCreation(Tool):
    @staticmethod
        # primary execution function
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # return outcome
        return json.dumps({"video_manifest": "manifest_001"}, indent=2)

    @staticmethod
        # metadata information
    def get_info() -> Dict[str, Any]:
        # return outcome
        return {"type": "function", "function": {"name": "vidMani", "description": "Creates a manifest of clips.", "parameters": {"type": "object", "properties": {"insights": {"type": "string"}}, "required": ["insights"]}}}
