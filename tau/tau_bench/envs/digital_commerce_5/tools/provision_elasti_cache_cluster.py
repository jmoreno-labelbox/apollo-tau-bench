from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class ProvisionElastiCacheCluster(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        cluster_id: Any,
        engine: Any,
        node_type: Any,
        num_nodes: Any,
        subnet_group_id: Any,
        security_group_id: Any,
        auth_token_enabled: Any,
        transit_encryption_enabled: Any,
        at_rest_encryption_enabled: Any,
        endpoint: Any,
        port: Any,
        created_at: Any,
    ) -> str:
        cluster_id = _as_id(cluster_id)
        clusters = data.setdefault("aws_elasticache_clusters", [])
        existing = next(
            (c for c in clusters if _as_id(c.get("cluster_id")) == cluster_id), None
        )
        if existing:
            payload = existing
            out = json.dumps(payload, indent=2)
            return out

        rec = {
            "cluster_id": cluster_id,
            "engine": str(engine),
            "node_type": str(node_type),
            "num_nodes": int(num_nodes),
            "subnet_group_id": _as_id(subnet_group_id),
            "security_group_id": _as_id(security_group_id),
            "auth_token_enabled": bool(auth_token_enabled),
            "transit_encryption_enabled": bool(transit_encryption_enabled),
            "at_rest_encryption_enabled": bool(at_rest_encryption_enabled),
            "endpoint": str(endpoint),
            "port": int(port),
            "status": "Provisioning",
            "created_at": str(created_at),
            "last_modified_at": str(created_at),
        }
        clusters.append(rec)
        payload = rec
        out = json.dumps(payload, indent=2)
        return out
        

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ProvisionElasticacheCluster",
                "description": "Create a new ElastiCache cluster record with configuration.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                        "engine": {"type": "string"},
                        "node_type": {"type": "string"},
                        "num_nodes": {"type": "integer"},
                        "subnet_group_id": {"type": "string"},
                        "security_group_id": {"type": "string"},
                        "auth_token_enabled": {"type": "boolean"},
                        "transit_encryption_enabled": {"type": "boolean"},
                        "at_rest_encryption_enabled": {"type": "boolean"},
                        "endpoint": {"type": "string"},
                        "port": {"type": "integer"},
                        "created_at": {"type": "string"},
                    },
                    "required": [
                        "cluster_id",
                        "engine",
                        "node_type",
                        "num_nodes",
                        "subnet_group_id",
                        "security_group_id",
                        "auth_token_enabled",
                        "transit_encryption_enabled",
                        "at_rest_encryption_enabled",
                        "endpoint",
                        "port",
                        "created_at",
                    ],
                },
            },
        }
