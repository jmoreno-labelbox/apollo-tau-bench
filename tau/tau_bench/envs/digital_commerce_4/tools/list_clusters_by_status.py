from tau_bench.envs.tool import Tool
import json
from typing import Any

class ListClustersByStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], status: str) -> str:
        clusters = data.get("aws_elasticache_clusters", [])
        result = [c for c in clusters if c.get("status") == status]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listClustersByStatus",
                "description": "List ElastiCache clusters by status.",
                "parameters": {
                    "type": "object",
                    "properties": {"status": {"type": "string"}},
                    "required": ["status"],
                },
            },
        }
