from tau_bench.envs.tool import Tool
import json
from typing import Any

class BrowseTerminalLog(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], event_type: str = None) -> str:
        logs = data.get("terminal_log", []) or []
        rows = [
            l for l in logs if (not event_type or l.get("event_type") == event_type)
        ]
        payload = {"logs": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListTerminalLog",
                "description": "List terminal log entries (optionally filter by event_type).",
                "parameters": {
                    "type": "object",
                    "properties": {"event_type": {"type": "string"}},
                    "required": [],
                },
            },
        }
