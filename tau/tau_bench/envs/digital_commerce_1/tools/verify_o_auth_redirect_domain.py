# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class VerifyOAuthRedirectDomain(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], callback_url: Any, expected_domain: Any) -> str:
        parsed = urlparse(str(callback_url))
        domain = (parsed.hostname or "").lower()
        exp = str(expected_domain).lower()
        status = "verified" if domain == exp else "mismatch"
        return json.dumps(status, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "verify_oauth_redirect_domain",
                "description": "Verify that an OAuth callback URL's host matches an approved domain.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "callback_url": {"type": "string"},
                        "expected_domain": {"type": "string"},
                    },
                    "required": ["callback_url", "expected_domain"],
                },
            },
        }
