from tau_bench.envs.tool import Tool
import json
from typing import Any

class SendingToSlack(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], channel: str = None, report_link: str = None, playlist_links: list = None, report_id: str = None) -> str:
        if playlist_links is None:
            playlist_links = []
        payload = {"post_status": "posted"}
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
                "name": "postings",
                "description": "Sends links to Slack and logs workflow run.",
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
