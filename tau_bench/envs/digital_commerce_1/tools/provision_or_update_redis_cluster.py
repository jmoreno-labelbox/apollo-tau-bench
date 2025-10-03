from tau_bench.envs.tool import Tool
import json
from typing import Any

class ProvisionOrUpdateRedisCluster(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        cluster_name: str,
        node_type: str,
        replicas: int,
        environment: str
    ) -> str:
        _environmentL = environment or ''.lower()
        pass
        clusters = _ensure_table(data, "aws_elasticache_clusters")
        cluster_id = _stable_id("rc", cluster_name, environment)
        endpoint = f"{cluster_name}.{environment.lower()}.cache.local:6379"
        row = _find_one(clusters, cluster_id=cluster_id)
        if row:
            row.update(
                {
                    "cluster_name": cluster_name,
                    "node_type": node_type,
                    "replicas": int(replicas),
                    "environment": environment,
                    "endpoint": endpoint,
                    "status": "available",
                }
            )
        else:
            clusters.append(
                {
                    "cluster_id": cluster_id,
                    "cluster_name": cluster_name,
                    "node_type": node_type,
                    "replicas": int(replicas),
                    "environment": environment,
                    "endpoint": endpoint,
                    "status": "available",
                    "require_auth": False,
                    "tls_in_transit": False,
                }
            )
        return _json(
            {"cluster_id": cluster_id, "endpoint": endpoint, "status": "available"}
        )
        _environmentL = environment or ''.lower()
        pass
        clusters = _ensure_table(data, "aws_elasticache_clusters")
        cluster_id = _stable_id("rc", cluster_name, environment)
        endpoint = f"{cluster_name}.{environment.lower()}.cache.local:6379"
        row = _find_one(clusters, cluster_id=cluster_id)
        if row:
            row.update(
                {
                    "cluster_name": cluster_name,
                    "node_type": node_type,
                    "replicas": int(replicas),
                    "environment": environment,
                    "endpoint": endpoint,
                    "status": "available",
                }
            )
        else:
            clusters.append(
                {
                    "cluster_id": cluster_id,
                    "cluster_name": cluster_name,
                    "node_type": node_type,
                    "replicas": int(replicas),
                    "environment": environment,
                    "endpoint": endpoint,
                    "status": "available",
                    "require_auth": False,
                    "tls_in_transit": False,
                }
            )
        return _json(
            {"cluster_id": cluster_id, "endpoint": endpoint, "status": "available"}
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "provisionOrUpdateRedisCluster",
                "description": "Provision or update an ElastiCache/Redis cluster for an environment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_name": {"type": "string"},
                        "node_type": {"type": "string"},
                        "replicas": {"type": "integer", "minimum": 0},
                        "environment": {
                            "type": "string",
                            "enum": ["DEV", "UAT", "PROD"],
                        },
                    },
                    "required": [
                        "cluster_name",
                        "node_type",
                        "replicas",
                        "environment",
                    ],
                },
            },
        }
