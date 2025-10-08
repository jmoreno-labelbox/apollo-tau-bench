from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta

class SetUserMfaTool(Tool):
    """set_user_mfa
    Modifies users[].mfa.enabled and users[].mfa.method; synchronizes legacy users[].mfa_enabled.
    Idempotent: does nothing if the state already aligns.
    """

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, enabled: bool = None, method: Any = None) -> str:
        if user_id is None or enabled is None:
            payload = {"error": "user_id and enabled are required"}
            out = json.dumps(payload, indent=2)
            return out

        users: list[dict[str, Any]] = data.setdefault("users", [])
        u = next((x for x in users if x.get("user_id") == user_id), None)
        if not u:
            payload = {"error": f"User {user_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        mfa = u.get("mfa") or {}
        current_enabled = (
            bool(mfa.get("enabled")) if "enabled" in mfa else u.get("mfa_enabled")
        )

        if current_enabled == bool(enabled):
            payload = {
                    "user_id": user_id,
                    "mfa_enabled": bool(enabled),
                    "updated_at": _HARD_TS,
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        mfa["enabled"] = bool(enabled)
        u["mfa"] = mfa
        u["mfa_enabled"] = bool(enabled)
        payload = {
                "user_id": user_id,
                "mfa": {"enabled": mfa.get("enabled")},
                "mfa_enabled": u.get("mfa_enabled"),
                "updated_at": _HARD_TS,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetUserMfa",
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
