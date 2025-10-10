# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetUserMfaTool(Tool):
    """set_user_mfa
    Updates users[].mfa.enabled and users[].mfa.method; keeps legacy users[].mfa_enabled in sync.
    Idempotent: no-op if state already matches.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        enabled = kwargs.get("enabled")
        method = kwargs.get("method")

        if user_id is None or enabled is None:
            return json.dumps({"error": "user_id and enabled are required"}, indent=2)

        users: List[Dict[str, Any]] = data.setdefault("users", [])
        u = next((x for x in users if x.get("user_id") == user_id), None)
        if not u:
            return json.dumps({"error": f"User {user_id} not found"}, indent=2)

        mfa = u.get("mfa") or {}
        current_enabled = (
            bool(mfa.get("enabled")) if "enabled" in mfa else u.get("mfa_enabled")
        )

        if current_enabled == bool(enabled):
            return json.dumps(
                {
                    "user_id": user_id,
                    "mfa_enabled": bool(enabled),
                    "updated_at": _HARD_TS,
                },
                indent=2,
            )

        mfa["enabled"] = bool(enabled)
        u["mfa"] = mfa
        u["mfa_enabled"] = bool(enabled)

        return json.dumps(
            {
                "user_id": user_id,
                "mfa": {"enabled": mfa.get("enabled")},
                "mfa_enabled": u.get("mfa_enabled"),
                "updated_at": _HARD_TS,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "set_user_mfa",
                "description": (
                    "Update a user's MFA state and method; idempotent and back-compatible."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "enabled": {"type": "boolean"},
                    },
                    "required": ["user_id", "enabled"],
                },
            },
        }
