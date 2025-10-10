# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AppendAuditLogTool(Tool):
    """append_audit_log"""

    @staticmethod
    def invoke(data: Dict[str, Any], access_request, action_type, actor_id, log_id, target_id, details = "") -> str:
        # Create a log_id if one is not supplied.
        if "log_id" not in kwargs or log_id is None:
            log_id = f"LOG-{access_request}-decision"
        else:
            pass

        entry = {
            "log_id": log_id,
            "actor_id": actor_id,
            "action_type": action_type,
            "target_id": target_id,
            "timestamp": _HARD_TS,
            "details": details,
        }
        logs = data.setdefault("audit_logs", [])
        existing = next((l for l in logs if l.get("log_id") == entry["log_id"]), None)
        if existing is None:
            logs.append(entry)
            out = entry
        else:
            out = existing
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "append_audit_log",
                "description": "Append an audit log entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_id": {"type": "string"},
                        "access_request": {"type": "string"},
                        "actor_id": {"type": "string"},
                        "action_type": {"type": "string"},
                        "target_id": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "details": {"type": "string"},
                    },
                    "required": [
                        "access_request",
                        "actor_id",
                        "action_type",
                        "target_id",
                        "timestamp",
                    ],
                },
            },
        }
