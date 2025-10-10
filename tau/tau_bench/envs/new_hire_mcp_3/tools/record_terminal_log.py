# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _fixed_now_iso


class RecordTerminalLog(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        event_type = kwargs.get("event_type")
        message = kwargs.get("message")
        candidate_id = kwargs.get("candidate_id")
        terminal_logs = data.setdefault("terminal_logs", [])
        log_entry = {
            "event_type": event_type,
            "message": message,
            "candidate_id": candidate_id,
            "timestamp": _fixed_now_iso()
        }
        terminal_logs.append(log_entry)
        return json.dumps({"logged_event": log_entry}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "record_terminal_log",
                "description": "Logs a terminal event for audit/debug purposes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "event_type": {"type": "string"},
                        "message": {"type": "string"},
                        "candidate_id": {"type": "string"}
                    },
                    "required": ["event_type", "message"]
                }
            }
        }
