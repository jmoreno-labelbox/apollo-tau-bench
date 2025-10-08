from tau_bench.envs.tool import Tool
import json
from typing import Any

class VIdeoRen(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], manifest: Any = None, tool: str = None) -> str:
        payload = {"video_links": ["portal://playlist/opponent_pitcher_tendencies"]}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        pass
        #return result
        return {
            "type": "function",
            "function": {
                "name": "makeVidList",
                "description": "Renders playlists via ffmpeg.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "manifest": {"type": "string"},
                        "tool": {"type": "string"},
                    },
                    "required": ["manifest", "tool"],
                },
            },
        }
