from tau_bench.envs.tool import Tool
import json
from typing import Any

class WriteTerminalLog(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], event_type: str = None, message: str = None) -> str:
        logs = data.get("terminal_log", [])
        max_id = 0
        for l in logs:
            try:
                lid = int(l.get("log_id", 0))
                if lid > max_id:
                    max_id = lid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "log_id": new_id,
            "event_type": event_type,
            "message": message,
            "created_at": _fixed_now_iso(),
        }
        logs.append(row)
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordTerminalLog",
                "description": "Append a terminal log entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "event_type": {"type": "string"},
                        "message": {"type": "string"},
                    },
                    "required": ["event_type", "message"],
                },
            },
        }
