# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteElastiCacheCluster(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cluster_id: Any) -> str:
        cluster_id = _as_id(cluster_id)
        clusters = data.get("aws_elasticache_clusters", [])
        m = next((c for c in clusters if _as_id(c.get("cluster_id")) == cluster_id), None)
        if not m:
            return _err("Cluster not found.")
        m["status"] = "Deleted"
        deleted_at = FIXED_NOW
        m["deleted_at"] = str(deleted_at)
        m["last_modified_at"] = str(deleted_at)
        return json.dumps({"cluster_id": cluster_id, "status": "Deleted"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_elasticache_cluster",
                "description": "Mark an ElastiCache cluster as Deleted.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                    },
                    "required": ["cluster_id"],
                },
            },
        }
