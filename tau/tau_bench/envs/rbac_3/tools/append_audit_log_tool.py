from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta

class AppendAuditLogTool(Tool):
    """AppendAuditLog"""

    @staticmethod
    def invoke(data: dict[str, Any], access_request: str = None, actor_id: str = None, action_type: str = None, target_id: str = None, log_id: str = None, details: str = "",
    timestamp: Any = None
    ) -> str:
        # Create log_id if it hasn't been supplied
        if log_id is None:
            log_id = f"LOG-{access_request or 'unknown'}-decision"

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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AppendAuditLog",
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
