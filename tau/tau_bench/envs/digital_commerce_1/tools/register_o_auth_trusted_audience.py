# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RegisterOAuthTrustedAudience(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], app_name_hint: Any, audiences: Any) -> str:
        app = str(app_name_hint)
        h = hashlib.sha256((app + "|" + "|".join(sorted(audiences))).encode("utf-8")).hexdigest()[
            :10
        ]
        policy_id = f"aud-{h}"
        table = data.setdefault("oauth_trusted_audiences", {})
        table[app] = {"audiences": list(dict.fromkeys(audiences)), "policy_id": policy_id}
        return json.dumps(
            {"app_name_hint": app, "audiences": table[app]["audiences"], "policy_id": policy_id},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "register_oauth_trusted_audience",
                "description": "Register allowed token audiences (aud) for a connected app to prevent token reuse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "app_name_hint": {"type": "string"},
                        "audiences": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["app_name_hint", "audiences"],
                },
            },
        }
