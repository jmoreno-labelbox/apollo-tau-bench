from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetApiRateLimitConfig(Tool):
    """Retrieve rate limit settings for a specified API endpoint."""

    @staticmethod
    def invoke(data: dict[str, Any], api_endpoint: Any) -> str:
        if not api_endpoint:
            return _error("api_endpoint is required.")

        rate_limits = data.get("api_rate_limits", {}).values()
        configs = [rl for rl in rate_limits.values() if rl.get("api_endpoint") == api_endpoint]
        if not configs:
            return _error(f"Rate limit for '{api_endpoint}' not found.")
        latest = configs[-1]
        payload = latest
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetApiRateLimitConfig",
                "description": "Fetch rate limit configuration for a given API endpoint.",
                "parameters": {
                    "type": "object",
                    "properties": {"api_endpoint": {"type": "string"}},
                    "required": ["api_endpoint"],
                },
            },
        }
