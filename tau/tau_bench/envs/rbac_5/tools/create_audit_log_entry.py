# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateAuditLogEntry(Tool):
    """
    Write a deterministic audit log entry.

    kwargs:
      action_type: str (required)
      actor_id: str (required)
      target_id: str (required)
      details: str (required)
      timestamp: str ISO (defaults now)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], timestamp, action_type = "", actor_id = "", details = "", target_id = "") -> str:
        timestamp = timestamp or get_current_timestamp()

        log = {
            "log_id": _next_id(data, "audit_logs", "L"),
            "timestamp": timestamp,
            "action_type": action_type,
            "actor_id": actor_id,
            "target_id": target_id,
            "details": details,
        }

        data.setdefault("audit_logs", []).append(log)
        return json.dumps({"ok": True, "audit_log": log})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_audit_log_entry",
                "description": "Append an audit log entry with deterministic timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action_type": {"type": "string", "description": "Audit action type."},
                        "actor_id": {"type": "string", "description": "User performing the action."},
                        "target_id": {"type": "string", "description": "Target entity id (request, user, resource, etc.)."},
                        "details": {"type": "string", "description": "Deterministic details string."},
                        "timestamp": {"type": "string", "description": "ISO timestamp (optional)."}
                    },
                    "required": ["action_type", "actor_id", "target_id", "details"],
                    "additionalProperties": False
                }
            }
        }
