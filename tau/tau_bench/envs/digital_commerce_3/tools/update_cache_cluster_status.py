# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _idstr(v):
    """Coerce numeric IDs to strings; leave None/strings unchanged."""
    return str(v) if isinstance(v, int) else v

class UpdateCacheClusterStatus(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        cluster_id: Any,
        endpoint_url: Any = None,
        status: Any = None,
        security_group_id: Any = None,
    ) -> str:
        cluster_id = _idstr(cluster_id)
        endpoint_url = f"{endpoint_url}" if endpoint_url is not None else None
        status = f"{status}" if status is not None else None
        security_group_id = _idstr(security_group_id) if security_group_id is not None else None

        cluster = next(
            (
                c
                for c in data.get("aws_elasticache_clusters", [])
                if f"{c.get('cluster_id')}" == f"{cluster_id}"
            ),
            None,
        )
        if not cluster:
            return json.dumps({"error": "Cluster not found."}, indent=2)
        if status is not None:
            cluster["status"] = status
        if endpoint_url is not None:
            cluster["endpoint_url"] = endpoint_url
        if security_group_id is not None:
            cluster["security_group_id"] = security_group_id
        return json.dumps(cluster, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_cache_cluster_status",
                "description": "Updates selected fields of an ElastiCache cluster.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                        "status": {"type": "string"},
                        "endpoint_url": {"type": "string"},
                        "security_group_id": {"type": "string"},
                    },
                    "required": ["cluster_id"],
                },
            },
        }