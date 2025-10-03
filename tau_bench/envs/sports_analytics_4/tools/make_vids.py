from tau_bench.envs.tool import Tool
import json
from typing import Any

class MakeVids(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], report_id: str = None, internal_portal_link: str = None, clip_count: int = 0) -> str:
        playlists = _load_table(data, "video_playlists")
        playlists.append(
            {
                "report_id": report_id,
                "internal_portal_link": internal_portal_link,
                "clip_count": clip_count,
            }
        )
        payload = {"status": "ok"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        pass
        #return result
        return {
            "type": "function",
            "function": {
                "name": "makeVid",
                "description": "Persists a video playlist row linked to a report.",
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
