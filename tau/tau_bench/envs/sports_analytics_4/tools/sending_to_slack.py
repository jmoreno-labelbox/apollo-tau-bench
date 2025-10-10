# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SendingToSlack(Tool):
    @staticmethod
        # primary execution function
    def invoke(data: Dict[str, Any], channel, report_id, report_link, playlist_links = []) -> str:
        # return outcome
        return json.dumps({"post_status": "posted"}, indent=2)

    @staticmethod
        # metadata information
    def get_info() -> Dict[str, Any]:
        # return outcome
        return {"type": "function", "function": {"name": "postings", "description": "Sends links to Slack and logs workflow run.", "parameters": {"type": "object", "properties": {"channel": {"type": "string"}, "report_link": {"type": "string"}, "playlist_links": {"type": "array", "items": {"type": "string"}}, "report_id": {"type": "string"}}, "required": ["channel", "report_link", "report_id"]}}}
