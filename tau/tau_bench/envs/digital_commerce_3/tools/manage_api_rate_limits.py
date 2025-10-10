# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import FIXED_NOW


class ManageApiRateLimits(Tool):
    """Configure and manage API rate limiting policies."""

    @staticmethod
    def invoke(data: Dict[str, Any], api_endpoint: Any, rate_limit: Any = 100) -> str:
        api_endpoint = api_endpoint
        rate_limit = rate_limit

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

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "manage_api_rate_limits",
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
