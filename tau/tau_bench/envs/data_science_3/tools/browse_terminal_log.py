# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class BrowseTerminalLog(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], event_type) -> str:
        logs = data.get("terminal_log", []) or []
        rows = [l for l in logs if (not event_type or l.get("event_type")==event_type)]
        return json.dumps({"logs": rows}, indent=2)
    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"list_terminal_log",
            "description":"List terminal log entries (optionally filter by event_type).",
            "parameters":{"type":"object","properties":{"event_type":{"type":"string"}},"required":[]}
        }}
