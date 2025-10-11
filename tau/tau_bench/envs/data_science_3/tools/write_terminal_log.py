# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _fixed_now_iso


class WriteTerminalLog(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], event_type, message) -> str:
        logs = data.get("terminal_log", [])
        max_id = 0
        for l in logs:
            try:
                lid = int(l.get("log_id", 0))
                if lid > max_id: max_id = lid
            except (ValueError, TypeError):
                continue
        new_id = max_id + 1
        row = {
            "log_id": new_id,
            "event_type": event_type,
            "message": message,
            "created_at": _fixed_now_iso()
        }
        logs.append(row)
        return json.dumps(row, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"record_terminal_log",
            "description":"Append a terminal log entry.",
            "parameters":{"type":"object","properties":{
                "event_type":{"type":"string"},
                "message":{"type":"string"}
            },"required":["event_type","message"]}
        }}
