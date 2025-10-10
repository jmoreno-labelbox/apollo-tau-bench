# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchSlackMessagesTool(Tool):
    """Search Slack messages by channel, user, time range, keywords, regex, or thread context."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        messages = data.get("slack_messages", [])
        channel = kwargs.get("channel")
        username = kwargs.get("username")
        start_time = kwargs.get("start_time")
        end_time = kwargs.get("end_time")
        keywords = kwargs.get("keywords", [])
        regex = kwargs.get("regex")
        thread_id = kwargs.get("thread_id")
        import re

        results = []
        for msg in messages:
            if channel and msg["channel"] != channel:
                continue
            if username and msg["username"] != username:
                continue
            if start_time and msg["timestamp"] < start_time:
                continue
            if end_time and msg["timestamp"] > end_time:
                continue
            if keywords and not any(kw in msg["message"] for kw in keywords):
                continue
            if regex and not re.search(regex, msg["message"]):
                continue
            if thread_id and msg.get("thread_id") != thread_id:
                continue
            results.append(msg)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_slack_messages",
                "description": "Search Slack messages and retrieve analytics by channel, user, keywords, regex, or time interval.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel": {"type": "string"},
                        "username": {"type": "string"},
                        "start_time": {"type": "string"},
                        "end_time": {"type": "string"},
                        "keywords": {"type": "array", "items": {"type": "string"}},
                        "regex": {"type": "string"},
                        "thread_id": {"type": "string"}
                    }
                }
            }
        }
