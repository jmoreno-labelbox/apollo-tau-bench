# Copyright by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogTerminalEventTool(Tool):
    """Append a log entry to terminal_logs (requires explicit log_ts)."""

    @staticmethod
    def invoke(data: Dict[str, Any], log_ts, message) -> str:
        log_ts = _require_str(log_ts, "log_ts")
        message = _require_str(message, "message")
        if not (log_ts and message):
            return json.dumps({"error":"log_ts and message required"})

        logs = _safe_table(data, "terminal_logs")
        log_id = _det_id("log", [log_ts, message[:64]])
        # save as a basic row; deterministic identifier not utilized by the dataset but added as a field
        logs.append({"log_ts": log_ts, "message": message, "log_id": log_id})
        return json.dumps({"success": True, "log_id": log_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"log_terminal_event",
            "description":"Append a new terminal log row (deterministic).",
            "parameters":{"type":"object","properties":{
                "log_ts":{"type":"string"},
                "message":{"type":"string"}
            },"required":["log_ts","message"]}
        }}
