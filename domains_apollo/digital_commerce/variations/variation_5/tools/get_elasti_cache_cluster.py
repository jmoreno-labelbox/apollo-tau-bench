from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class GetElastiCacheCluster(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cluster_id: Any, aws_elasticache_clusters: list = None) -> str:
        cluster_id = _as_id(cluster_id)
        clusters = aws_elasticache_clusters or []
        m = next(
            (c for c in clusters if _as_id(c.get("cluster_id")) == cluster_id), None
        )
        payload = m or {}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetElasticacheCluster",
                "description": "Return a single ElastiCache cluster by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"cluster_id": {"type": "string"}},
                    "required": ["cluster_id"],
                },
            },
        }
