# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateElastiCacheClusterStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cluster_id: str, status: str, changed_at: Any) -> str:
        cluster_id = _as_id(cluster_id)
        clusters = data.get("aws_elasticache_clusters", [])
        m = next((c for c in clusters if _as_id(c.get("cluster_id")) == cluster_id), None)
        if not m:
            return _err("Cluster not found.")
        m["status"] = str(status)
        m["last_modified_at"] = str(changed_at)
        return json.dumps(
            {
                "cluster_id": cluster_id,
                "status": m["status"],
                "last_modified_at": m["last_modified_at"],
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_elasticache_cluster_status",
                "description": "Set the lifecycle status on an ElastiCache cluster. Use the current time per policy. Do not invent timestamps.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                        "status": {"type": "string"},
                        "changed_at": {"type": "string"},
                    },
                    "required": ["cluster_id", "status", "changed_at"],
                },
            },
        }
