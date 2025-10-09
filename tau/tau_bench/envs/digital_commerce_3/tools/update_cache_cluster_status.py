from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateCacheClusterStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        cluster_id: Any,
        endpoint_url: Any = None,
        status: Any = None,
        security_group_id: Any = None
    ) -> str:
        cluster_id = _idstr(cluster_id)
        endpoint_url = f"{endpoint_url}" if endpoint_url is not None else None
        status = f"{status}" if status is not None else None
        security_group_id = (
            _idstr(security_group_id) if security_group_id is not None else None
        )

        cluster = next(
            (
                c
                for c in data.get("aws_elasticache_clusters", [])
                if f"{c.get('cluster_id')}" == f"{cluster_id}"
            ),
            None,
        )
        if not cluster:
            payload = {"error": "Cluster not found."}
            out = json.dumps(payload, indent=2)
            return out
        if status is not None:
            cluster["status"] = status
        if endpoint_url is not None:
            cluster["endpoint_url"] = endpoint_url
        if security_group_id is not None:
            cluster["security_group_id"] = security_group_id
        payload = cluster
        out = json.dumps(payload, indent=2)
        return out
        pass
        cluster_id = _idstr(cluster_id)
        endpoint_url = f"{endpoint_url}" if endpoint_url is not None else None
        status = f"{status}" if status is not None else None
        security_group_id = (
            _idstr(security_group_id) if security_group_id is not None else None
        )

        cluster = next(
            (
                c
                for c in data.get("aws_elasticache_clusters", [])
                if f"{c.get('cluster_id')}" == f"{cluster_id}"
            ),
            None,
        )
        if not cluster:
            payload = {"error": "Cluster not found."}
            out = json.dumps(payload, indent=2)
            return out
        if status is not None:
            cluster["status"] = status
        if endpoint_url is not None:
            cluster["endpoint_url"] = endpoint_url
        if security_group_id is not None:
            cluster["security_group_id"] = security_group_id
        payload = cluster
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCacheClusterStatus",
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
