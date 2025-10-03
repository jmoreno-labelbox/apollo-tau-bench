from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetCacheClusterInfo(Tool):
    """Obtain ElastiCache cluster information using cluster_id."""

    @staticmethod
    def invoke(data: dict[str, Any], cluster_id: Any) -> str:
        cluster_id = _idstr(cluster_id)
        if not cluster_id:
            return _error("cluster_id is required.")
        clusters = data.get("aws_elasticache_clusters", [])
        cluster = _find_one(clusters, "cluster_id", cluster_id)
        if not cluster:
            return _error(f"Cluster '{cluster_id}' not found.")
        payload = cluster
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCacheClusterInfo",
                "description": "Fetch ElastiCache cluster details by cluster_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"cluster_id": {"type": "string"}},
                    "required": ["cluster_id"],
                },
            },
        }
