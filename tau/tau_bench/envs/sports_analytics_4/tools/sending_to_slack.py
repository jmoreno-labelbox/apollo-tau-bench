# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SendingToSlack(Tool):
    @staticmethod
        # main invoke function
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        channel = kwargs.get("channel")
        report_link = kwargs.get("report_link")
        playlist_links = kwargs.get("playlist_links", [])
        report_id = kwargs.get("report_id")
        # return result
        return json.dumps({"post_status": "posted"}, indent=2)

    @staticmethod
        # info metadata
    def get_info() -> Dict[str, Any]:
        # return result
        return {"type": "function", "function": {"name": "postings", "description": "Sends links to Slack and logs workflow run.", "parameters": {"type": "object", "properties": {"channel": {"type": "string"}, "report_link": {"type": "string"}, "playlist_links": {"type": "array", "items": {"type": "string"}}, "report_id": {"type": "string"}}, "required": ["channel", "report_link", "report_id"]}}}
