# Copyright held by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReadAuditEvents(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], event_type) -> str:
        logs = list(data.get("terminal_log", {}).values()) or []
        rows = [l for l in logs if (not event_type or l.get("event_type") == event_type)]
        return json.dumps({"logs": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "read_audit_events",
            "description": "List audit/terminal log entries (filter by event).",
            "parameters": {"type": "object", "properties": {
                "event_type": {"type": "string"}
            }, "required": []}
        }}
