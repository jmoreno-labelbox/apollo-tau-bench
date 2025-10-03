from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta

class ListUsersByMfaTool(Tool):
    """ListUsersByMfa"""

    @staticmethod
    def invoke(data: dict[str, Any], enabled: bool = None, status: str = None,
    user_id: Any = None,
    ) -> str:
        users: list[dict[str, Any]] = data.get("users", [])
        out: list[dict[str, Any]] = []

        def _effective_enabled_and_source(
            u: dict[str, Any],
        ) -> tuple[bool | None, str]:
            mfa = u.get("mfa")
            if isinstance(mfa, dict) and "enabled" in mfa:
                return bool(mfa.get("enabled")), "new"
            if "mfa_enabled" in u:
                return bool(u.get("mfa_enabled")), "legacy"
            return None, "unknown"

        for u in users:
            if status and not _eq(u.get("status"), status):
                continue

            eff, source = _effective_enabled_and_source(u)
            if enabled is not None:
                if eff is None or bool(eff) != bool(enabled):
                    continue

            rec = dict(u)
            rec.setdefault("mfa", {})
            rec["mfa"] = dict(rec["mfa"]) if isinstance(rec["mfa"], dict) else {}
            if eff is not None:
                rec["mfa"]["enabled"] = bool(eff)
            rec["mfa"]["source"] = source
            out.append(rec)

        out.sort(key=lambda r: (r.get("user_id") or ""))
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListUsersByMfa",
                "description": "Find users by MFA state and optional account status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "enabled": {"type": "boolean"},
                    },
                    "required": ["enabled"],
                },
            },
        }
