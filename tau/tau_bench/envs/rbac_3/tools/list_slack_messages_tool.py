# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _parse_iso(ts: Optional[str]) -> Optional[datetime]:
    """Robust ISO8601 parse: supports 'Z' and offsets; returns None if missing."""
    if not ts:
        return None
    ts = ts.replace("Z", "+00:00")
    return datetime.fromisoformat(ts)

def _eq(a: Optional[str], b: Optional[str]) -> bool:
    return (a or "") == (b or "")

class ListSlackMessagesTool(Tool):
    """list_slack_messages"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        channel = kwargs.get("channel")
        date_from = kwargs.get("date_from")
        date_to = kwargs.get("date_to")

        dt_from = _parse_iso(date_from)
        dt_to = _parse_iso(date_to)

        msgs: List[Dict[str, Any]] = data.get("slack_messages", [])
        out: List[Dict[str, Any]] = []
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
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_slack_messages",
                "description": (
                    "List Slack messages with optional channel and time filters."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "channel": {
                            "type": "string",
"description": "e.g., # \"access-requests\"",
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