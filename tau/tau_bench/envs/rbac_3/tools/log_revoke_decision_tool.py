# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogRevokeDecisionTool(Tool):
    """log_revoke_decision
    Exclusively log revoke decisions using deterministic log_id and timestamp.
    - log_id format: LOG-<user_id>-<role_id>-decision
    - action_type: revoke_role
    - target_id: <user_id>:<role_id>
    """

    @staticmethod
    def invoke(data: Dict[str, Any], actor_id, details, revoked, role_id, user_id) -> str:

        if not user_id or not role_id:
            return json.dumps({"error": "user_id and role_id are required"}, indent=2)

        log_id = f"LOG-{user_id}-{role_id}-decision"
        # Obtain default information if not specified.
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
            "action_type": "revoke_role",
            "target_id": f"{user_id}:{role_id}",
            "timestamp": _HARD_TS,
            "details": details,
        }

        logs: List[Dict[str, Any]] = data.setdefault("audit_logs", [])
        existing = next((l for l in logs if l.get("log_id") == log_id), None)
        if existing:
            existing.update(entry)
            out = existing
        else:
            logs.append(entry)
            out = entry
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_revoke_decision",
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
