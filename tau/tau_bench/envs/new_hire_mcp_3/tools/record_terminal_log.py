from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class RecordTerminalLog(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], event_type: str = None, message: str = None, candidate_id: str = None) -> str:
        terminal_logs = data.setdefault("terminal_logs", [])
        log_entry = {
            "event_type": event_type,
            "message": message,
            "candidate_id": candidate_id,
            "timestamp": _fixed_now_iso(),
        }
        terminal_logs.append(log_entry)
        payload = {"logged_event": log_entry}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordTerminalLog",
                "description": "Logs a terminal event for audit/debug purposes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "event_type": {"type": "string"},
                        "message": {"type": "string"},
                        "candidate_id": {"type": "string"},
                    },
                    "required": ["event_type", "message"],
                },
            },
        }
