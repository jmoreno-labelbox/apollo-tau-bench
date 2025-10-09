from tau_bench.envs.tool import Tool
import json
from typing import Any

class AppendTerminalLog(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        log_type: str = None,
        message: str = None,
        type: Any = None
    ) -> str:
        logs = data.setdefault("terminal_log", [])
        if log_type == "completed":
            entry = {"event_id": "APPEND_002", "message": message}
        else:
            entry = {"event_id": "APPEND_001", "message": message}
        logs.append(entry)
        payload = entry
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "appendTerminalLog",
                "parameters": {
                    "type": "object",
                    "properties": {"message": {"type": "string"}},
                    "required": ["message"],
                },
            },
        }
