# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListUsersByMfaTool(Tool):
    """list_users_by_mfa"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        enabled = kwargs.get("enabled")
        status = kwargs.get("status")

        users: List[Dict[str, Any]] = list(data.get("users", {}).values())
        out: List[Dict[str, Any]] = []

        def _effective_enabled_and_source(
            u: Dict[str, Any],
        ) -> Tuple[Optional[bool], str]:
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
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_users_by_mfa",
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
