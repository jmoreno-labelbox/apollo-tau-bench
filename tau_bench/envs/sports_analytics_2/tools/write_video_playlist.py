from tau_bench.envs.tool import Tool
import json
from typing import Any

class WriteVideoPlaylist(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        playlists = _load_table(data, "video_playlists")
        playlists.append(
            {
                "report_id": kwargs.get("report_id"),
                "internal_portal_link": kwargs.get("internal_portal_link"),
                "clip_count": kwargs.get("clip_count", 0),
            }
        )
        payload = {"status": "ok"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "WriteVideoPlaylist",
                "description": "Writes a video playlist row linked to a report.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_id": {"type": "string"},
                        "internal_portal_link": {"type": "string"},
                        "clip_count": {"type": "integer"},
                    },
                    "required": ["internal_portal_link"],
                },
            },
        }
