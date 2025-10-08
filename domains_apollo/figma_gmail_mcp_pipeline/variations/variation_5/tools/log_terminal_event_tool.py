from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class LogTerminalEventTool(Tool):
    """Add a log entry to terminal_logs (requires a specific log_ts)."""

    @staticmethod
    def invoke(data: dict[str, Any], log_ts: str = None, message: str = None) -> str:
        log_ts = _require_str(log_ts, "log_ts")
        message = _require_str(message, "message")
        if not (log_ts and message):
            payload = {"error": "log_ts and message required"}
            out = json.dumps(payload)
            return out

        logs = _safe_table(data, "terminal_logs")
        log_id = _det_id("log", [log_ts, message[:64]])
        logs.append({"log_ts": log_ts, "message": message, "log_id": log_id})
        payload = {"success": True, "log_id": log_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogTerminalEvent",
                "description": "Append a new terminal log row (deterministic).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_ts": {"type": "string"},
                        "message": {"type": "string"},
                    },
                    "required": ["log_ts", "message"],
                },
            },
        }
