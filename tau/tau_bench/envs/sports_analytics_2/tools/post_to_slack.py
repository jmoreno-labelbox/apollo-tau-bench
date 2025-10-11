# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class PostToSlack(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], channel, report_id, report_link, playlist_links = []) -> str:
        return json.dumps({"post_status": "posted"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "post_to_slack", "description": "Posts links to Slack and logs workflow run.", "parameters": {"type": "object", "properties": {"channel": {"type": "string"}, "report_link": {"type": "string"}, "playlist_links": {"type": "array", "items": {"type": "string"}}, "report_id": {"type": "string"}}, "required": ["channel", "report_link", "report_id"]}}}
