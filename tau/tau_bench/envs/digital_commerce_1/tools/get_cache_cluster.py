# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCacheCluster(Tool):
    @staticmethod
    def invoke(data, cluster_id: str) -> str:
        rows = data.setdefault("aws_elasticache_clusters", [])
        row = next((r for r in rows if str(r.get("cluster_id")) == cluster_id), None)
        if not row:
            raise ValueError(f"cache cluster not found: {cluster_id}")
        return json.dumps(
            {
                "cluster_id": row["cluster_id"],
                "endpoint_url": row["endpoint_url"],
                "instance_type": row["instance_type"],
                "security_group_id": row["security_group_id"],
                "status": row["status"],
            }
        )

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_cache_cluster",
                "description": "Read existing ElastiCache cluster by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"cluster_id": {"type": "string"}},
                    "required": ["cluster_id"],
                },
            },
        }
