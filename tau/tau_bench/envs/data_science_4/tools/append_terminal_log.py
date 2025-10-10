# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AppendTerminalLog(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        msg = kwargs.get("message")
        log_type = kwargs.get("type")
        logs = data.setdefault("terminal_log", [])
        if log_type == "completed":
            entry = {"event_id": f"APPEND_002", "message": msg}
        else:
            entry = {"event_id": f"APPEND_001", "message": msg}
        logs.append(entry)
        return json.dumps(entry)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AppendTerminalLog",
                "parameters": {
                    "type": "object",
                    "properties": {"message": {"type": "string"}},
                    "required": ["message"],
                },
            },
        }
