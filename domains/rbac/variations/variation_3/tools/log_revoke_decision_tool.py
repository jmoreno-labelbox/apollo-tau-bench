from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta

class LogRevokeDecisionTool(Tool):
    """log_revoke_decision
    Solely log revoke decisions using a deterministic log_id and timestamp.
    - log_id format: LOG-<user_id>-<role_id>-decision
    - action_type: revoke_role
    - target_id: <user_id>:<role_id>
    """

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, role_id: str = None, actor_id: str = None, details: str = None, revoked: bool = None) -> str:
        if not user_id or not role_id:
            payload = {"error": "user_id and role_id are required"}
            out = json.dumps(payload, indent=2)
            return out

        log_id = f"LOG-{user_id}-{role_id}-decision"
        # Extract default information if not specifically given
        if details is None:
            if revoked is True:
                details = "REMOVED"
            elif revoked is False:
                details = "NOOP"
            else:
                details = ""

        entry = {
            "log_id": log_id,
            "actor_id": actor_id,
            "action_type": "RevokeRole",
            "target_id": f"{user_id}:{role_id}",
            "timestamp": _HARD_TS,
            "details": details,
        }

        logs: list[dict[str, Any]] = data.setdefault("audit_logs", [])
        existing = next((l for l in logs if l.get("log_id") == log_id), None)
        if existing:
            existing.update(entry)
            out = existing
        else:
            logs.append(entry)
            out = entry
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogRevokeDecision",
                "description": (
                    "Append an audit log entry for a revoke decision with deterministic id and timestamp."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "role_id": {"type": "string"},
                        "actor_id": {"type": "string"},
                        "details": {"type": "string"},
                        "revoked": {
                            "type": "boolean",
                            "description": (
                                "If provided and details omitted, sets details to REMOVED/NOOP accordingly."
                            ),
                        },
                    },
                    "required": ["user_id", "role_id"],
                },
            },
        }
