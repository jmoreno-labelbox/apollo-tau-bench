# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _find_one








def _idstr(v):
    """Coerce numeric IDs to strings; leave None/strings unchanged."""
    return str(v) if isinstance(v, int) else v

def _find_one(lst: List[Dict[str, Any]], key: str, value: Any) -> Dict[str, Any] | None:
    for x in lst or []:
        if x.get(key) == value:
            return x
    return None

def _error(msg: str) -> str:
    return json.dumps({"error": msg})

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