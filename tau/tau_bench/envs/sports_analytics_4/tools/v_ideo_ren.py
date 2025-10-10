# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class VIdeoRen(Tool):
    @staticmethod
        # main invoke function
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # return result
        return json.dumps({"video_links": ["portal://playlist/opponent_pitcher_tendencies"]}, indent=2)

    @staticmethod
        # info metadata
    def get_info() -> Dict[str, Any]:
        # return result
        return {"type": "function", "function": {"name": "makeVidList", "description": "Renders playlists via ffmpeg.", "parameters": {"type": "object", "properties": {"manifest": {"type": "string"}, "tool": {"type": "string"}}, "required": ["manifest", "tool"]}}}
