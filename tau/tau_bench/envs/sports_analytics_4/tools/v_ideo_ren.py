# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class VIdeoRen(Tool):
    @staticmethod
        # primary execution function
    def invoke(data: Dict[str, Any], ) -> str:
        # return output
        return json.dumps({"video_links": ["portal://playlist/opponent_pitcher_tendencies"]}, indent=2)

    @staticmethod
        # metadata information
    def get_info() -> Dict[str, Any]:
        # return output
        return {"type": "function", "function": {"name": "makeVidList", "description": "Renders playlists via ffmpeg.", "parameters": {"type": "object", "properties": {"manifest": {"type": "string"}, "tool": {"type": "string"}}, "required": ["manifest", "tool"]}}}
