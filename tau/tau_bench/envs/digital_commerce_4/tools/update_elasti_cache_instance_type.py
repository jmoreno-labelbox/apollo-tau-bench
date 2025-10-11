# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _as_id(x: Any) -> str:
    if x is None:
        return x
    if isinstance(x, str):
        return x
    if isinstance(x, int):
        return str(x)
    if isinstance(x, float) and x.is_integer():
        return str(int(x))
    return str(x)

class UpdateElastiCacheInstanceType(Tool):
    """Update only the instance_type on an existing ElastiCache cluster record."""

    @staticmethod
    def invoke(data: Dict[str, Any], cluster_id: Any, instance_type: Any) -> str:
        if not cluster_id or not instance_type:
            return json.dumps({"error": "cluster_id and instance_type are required."}, indent=2)

        cluster_id = _as_id(cluster_id)
        clusters = data.get("aws_elasticache_clusters", [])
        rec = next((c for c in clusters if _as_id(c.get("cluster_id")) == cluster_id), None)
        if not rec:
            return json.dumps({"error": "Cluster not found."}, indent=2)

        rec["instance_type"] = str(instance_type)
        data["aws_elasticache_clusters"] = clusters
        return json.dumps(
            {"cluster_id": cluster_id, "instance_type": rec["instance_type"]}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_elasticache_instance_type",
                "description": "Update the instance_type on an ElastiCache cluster record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {
                            "type": "string",
                            "description": "Target cluster_id from aws_elasticache_clusters.",
                        },
                        "instance_type": {
                            "type": "string",
                            "description": "New instance class, e.g., 'cache.t3.medium'.",
                        },
                    },
                    "required": ["cluster_id", "instance_type"],
                },
            },
        }