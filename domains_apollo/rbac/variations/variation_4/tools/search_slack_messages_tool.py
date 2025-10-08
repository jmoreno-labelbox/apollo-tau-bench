from tau_bench.envs.tool import Tool
import json
from typing import Any

class SearchSlackMessagesTool(Tool):
    """Query Slack messages based on channel, user, time range, keywords, regex, or thread context."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        channel: str = None,
        username: str = None,
        start_time: str = None,
        end_time: str = None,
        keywords: list[str] = None,
        regex: str = None,
        thread_id: str = None
    ) -> str:
        messages = data.get("slack_messages", [])
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
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchSlackMessages",
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
                        "thread_id": {"type": "string"},
                    },
                },
            },
        }
