# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ProvisionElastiCacheCluster(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        cluster_id: Any,
        cluster_name: Any,
        endpoint_url: Any,
        status: Any,
        instance_type: Any,
        security_group_id: Any,
    ) -> str:
        cluster_id = _as_id(cluster_id)
        clusters = data.get("aws_elasticache_clusters", [])
        existing = next((c for c in clusters if _as_id(c.get("cluster_id")) == cluster_id), None)
        if existing:
            return json.dumps(existing, indent=2)

        rec = {
            "cluster_id": cluster_id,
            "cluster_name": str(cluster_name),
            "endpoint_url": str(endpoint_url),
            "status": str(status),
            "instance_type": str(instance_type),
            "security_group_id": _as_id(security_group_id),
        }
        clusters.append(rec)
        data["aws_elasticache_clusters"] = clusters
        return json.dumps(rec, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "provision_elasticache_cluster",
                "description": "Create an ElastiCache cluster record with required fields only.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string", "description": "New cluster_id string."},
                        "cluster_name": {"type": "string", "description": "Human-readable name."},
                        "endpoint_url": {
                            "type": "string",
                            "description": "Hostname:port or 'NULL' if failed.",
                        },
                        "status": {
                            "type": "string",
                            "description": "e.g., 'available', 'provisioning', 'failed'.",
                        },
                        "instance_type": {
                            "type": "string",
                            "description": "e.g., 'cache.t3.medium'.",
                        },
                        "security_group_id": {
                            "type": "string",
                            "description": "Security group that protects the cluster.",
                        },
                    },
                    "required": [
                        "cluster_id",
                        "cluster_name",
                        "endpoint_url",
                        "status",
                        "instance_type",
                        "security_group_id",
                    ],
                },
            },
        }
