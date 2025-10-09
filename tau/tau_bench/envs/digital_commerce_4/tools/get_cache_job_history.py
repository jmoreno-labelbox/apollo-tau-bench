from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetCacheJobHistory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], org_id: str) -> str:
        org_id = _sid(org_id)
        jobs = data.get("cache_jobs", [])
        result = [j for j in jobs if j.get("org_id") == org_id]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCacheJobHistory",
                "description": "List cache jobs for an org.",
                "parameters": {
                    "type": "object",
                    "properties": {"org_id": {"type": "string"}},
                    "required": ["org_id"],
                },
            },
        }
