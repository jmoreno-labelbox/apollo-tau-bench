# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetApiRateLimitConfig(Tool):
    """Fetch rate limit configuration for a given API endpoint."""

    @staticmethod
    def invoke(data: Dict[str, Any], api_endpoint: Any) -> str:
        api_endpoint = api_endpoint
        if not api_endpoint:
            return _error("api_endpoint is required.")

        rate_limits = data.get("api_rate_limits", [])
        configs = [rl for rl in rate_limits if rl.get("api_endpoint") == api_endpoint]
        if not configs:
            return _error(f"Rate limit for '{api_endpoint}' not found.")
        latest = configs[-1]
        return json.dumps(latest, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_api_rate_limit_config",
                "description": "Fetch rate limit configuration for a given API endpoint.",
                "parameters": {
                    "type": "object",
                    "properties": {"api_endpoint": {"type": "string"}},
                    "required": ["api_endpoint"],
                },
            },
        }
