from tau_bench.envs.tool import Tool
import json
from typing import Any

class ConfigureCacheIntegration(Tool):
    """Set up external cache integration for a company."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        cluster_id: Any,
        elasticache_config: Any = None,
        engine: str = "redis",
        node_type: str = "cache.t3.micro",
        num_cache_nodes: int = 1
    ) -> str:
        if cluster_id is None:
            return _error("cluster_id is required.")

        cluster_id = _idstr(cluster_id)
        clusters = data.setdefault("aws_elasticache_clusters", [])
        cluster = _find_one(clusters, "cluster_id", cluster_id)

        if not cluster:
            cluster = {
                "cluster_id": cluster_id,
                "node_type": node_type,
                "num_cache_nodes": num_cache_nodes,
                "engine": engine,
                "status": "available",
                "endpoint_url": f"redis://{cluster_id}.cache.amazonaws.com:6379",
            }
            clusters.append(cluster)
        else:
            cluster.update(
                {
                    "node_type": node_type or cluster.get("node_type"),
                    "num_cache_nodes": num_cache_nodes or cluster.get("num_cache_nodes"),
                    "engine": engine or cluster.get("engine"),
                    "status": "available",
                }
            )

        result = {
            "cluster_id": cluster_id,
            "node_type": cluster.get("node_type"),
            "num_cache_nodes": cluster.get("num_cache_nodes"),
            "engine": cluster.get("engine"),
            "endpoint_url": cluster.get("endpoint_url"),
            "configuration_status": "completed",
        }
        _append_audit(
            data,
            "cache_configured",
            cluster_id,
            {
                "cluster_id": cluster_id,
                "config": {
                    "node_type": node_type,
                    "num_cache_nodes": num_cache_nodes,
                    "engine": engine,
                },
            },
        )
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ConfigureCacheIntegration",
                "description": "Configure external cache integration with ElastiCache cluster.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                        "elasticache_config": {
                            "type": "object",
                            "properties": {
                                "node_type": {"type": "string"},
                                "num_cache_nodes": {"type": "integer"},
                                "engine": {"type": "string"},
                            },
                        },
                    },
                    "required": ["cluster_id"],
                },
            },
        }
