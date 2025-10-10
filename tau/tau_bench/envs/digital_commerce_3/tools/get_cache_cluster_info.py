# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCacheClusterInfo(Tool):
    """Fetch ElastiCache cluster details by cluster_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], cluster_id: Any) -> str:
        cluster_id = _idstr(cluster_id)
        if not cluster_id:
            return _error("cluster_id is required.")
        clusters = data.get("aws_elasticache_clusters", [])
        cluster = _find_one(clusters, "cluster_id", cluster_id)
        if not cluster:
            return _error(f"Cluster '{cluster_id}' not found.")
        return json.dumps(cluster, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_cache_cluster_info",
                "description": "Fetch ElastiCache cluster details by cluster_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"cluster_id": {"type": "string"}},
                    "required": ["cluster_id"],
                },
            },
        }
