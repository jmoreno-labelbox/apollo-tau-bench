from tau_bench.envs.tool import Tool
import json
from typing import Any

class PostToSlack(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        kwargs.get("channel")
        kwargs.get("report_link")
        kwargs.get("playlist_links", [])
        kwargs.get("report_id")
        payload = {"post_status": "posted"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PostToSlack",
                "description": "Posts links to Slack and logs workflow run.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel": {"type": "string"},
                        "report_link": {"type": "string"},
                        "playlist_links": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "report_id": {"type": "string"},
                    },
                    "required": ["channel", "report_link", "report_id"],
                },
            },
        }
