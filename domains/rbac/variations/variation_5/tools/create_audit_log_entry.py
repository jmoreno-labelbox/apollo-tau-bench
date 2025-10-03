from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any

class CreateAuditLogEntry(Tool):
    """
    Create a consistent audit log entry.

    kwargs:
      action_type: str (mandatory)
      actor_id: str (mandatory)
      target_id: str (mandatory)
      details: str (mandatory)
      timestamp: str ISO (defaults to now)
    """

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        action_type: str = "", 
        actor_id: str = "", 
        target_id: str = "", 
        details: str = "", 
        timestamp: str = None
    ) -> str:
        if timestamp is None:
            timestamp = get_current_timestamp()

        log = {
            "log_id": _next_id(data, "audit_logs", "L"),
            "timestamp": timestamp,
            "action_type": action_type,
            "actor_id": actor_id,
            "target_id": target_id,
            "details": details,
        }

        data.setdefault("audit_logs", []).append(log)
        payload = {"ok": True, "audit_log": log}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAuditLogEntry",
                "description": "Append an audit log entry with deterministic timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action_type": {
                            "type": "string",
                            "description": "Audit action type.",
                        },
                        "actor_id": {
                            "type": "string",
                            "description": "User performing the action.",
                        },
                        "target_id": {
                            "type": "string",
                            "description": "Target entity id (request, user, resource, etc.).",
                        },
                        "details": {
                            "type": "string",
                            "description": "Deterministic details string.",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "ISO timestamp (optional).",
                        },
                    },
                    "required": ["action_type", "actor_id", "target_id", "details"],
                    "additionalProperties": False,
                },
            },
        }
