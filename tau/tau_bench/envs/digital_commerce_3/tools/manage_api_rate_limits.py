from tau_bench.envs.tool import Tool
import json
from typing import Any

class ManageApiRateLimits(Tool):
    """Establish and oversee API rate limiting rules."""

    @staticmethod
    def invoke(data: dict[str, Any], api_endpoint: Any, rate_limit: Any = 100) -> str:
        if not api_endpoint:
            return _error("api_endpoint is required.")

        rate_limits = data.setdefault("api_rate_limits", [])
        limit_id = f"RATE_{len(rate_limits) + 1:03d}"

        rate_limit_config = {
            "limit_id": limit_id,
            "api_endpoint": api_endpoint,
            "rate_limit": rate_limit,
            "configured_at": FIXED_NOW,
            "status": "active",
        }
        rate_limits.append(rate_limit_config)

        result = {
            "limit_id": limit_id,
            "api_endpoint": api_endpoint,
            "rate_limit": rate_limit,
            "status": "configured",
        }

        _append_audit(
            data, "rate_limit_configured", limit_id, {"api_endpoint": api_endpoint}
        )
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ManageApiRateLimits",
                "description": "Configure and manage API rate limiting policies.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "api_endpoint": {"type": "string"},
                        "rate_limit": {"type": "integer"},
                    },
                    "required": ["api_endpoint"],
                },
            },
        }
