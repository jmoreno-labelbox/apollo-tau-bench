from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta

class ListSlackMessagesTool(Tool):
    """list_slack_messages"""

    @staticmethod
    def invoke(data: dict[str, Any], channel: str = None, date_from: str = None, date_to: str = None) -> str:
        dt_from = _parse_iso(date_from)
        dt_to = _parse_iso(date_to)

        msgs: list[dict[str, Any]] = data.get("slack_messages", [])
        out: list[dict[str, Any]] = []
        for m in msgs:
            if channel and not _eq(m.get("channel"), channel):
                continue
            if dt_from or dt_to:
                ts = _parse_iso(m.get("timestamp"))
                if dt_from and (not ts or ts < dt_from):
                    continue
                if dt_to and (not ts or ts > dt_to):
                    continue
            out.append(m)

        out.sort(
            key=lambda r: ((r.get("timestamp") or ""), (r.get("message_id") or ""))
        )
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listSlackMessages",
                "description": (
                    "List Slack messages with optional channel and time filters."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel": {
                            "type": "string",
                            "description": "e.g., #access-requests",
                        },
                        "date_from": {
                            "type": "string",
                            "description": "ISO 8601 lower bound",
                        },
                        "date_to": {
                            "type": "string",
                            "description": "ISO 8601 upper bound",
                        },
                    },
                    "required": [],
                },
            },
        }
