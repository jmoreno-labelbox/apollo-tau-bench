from tau_bench.envs.tool import Tool
import json
from typing import Any

class RenderVideoPlaylists(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        payload = {"video_links": ["portal://playlist/opponent_pitcher_tendencies"]}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RenderVideoPlaylists",
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
