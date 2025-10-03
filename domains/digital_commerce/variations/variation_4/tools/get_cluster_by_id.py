from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetClusterById(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cluster_id: str) -> str:
        cluster_id = _sid(cluster_id)
        clusters = data.get("aws_elasticache_clusters", [])
        cluster = next((c for c in clusters if c.get("cluster_id") == cluster_id), None)
        payload = cluster or {"error": f"cluster {cluster_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetClusterById",
                "description": "Retrieve ElastiCache cluster by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"cluster_id": {"type": "string"}},
                    "required": ["cluster_id"],
                },
            },
        }
