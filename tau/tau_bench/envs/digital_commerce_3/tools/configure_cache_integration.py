# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ConfigureCacheIntegration(Tool):
    """Configure external cache integration for an organization."""

    @staticmethod
    def invoke(data: Dict[str, Any], cluster_id: Any, elasticache_config=None) -> str:
        if elasticache_config is None:
            elasticache_config = {}
        cluster_id = _idstr(cluster_id)

        if not elasticache_config.get("engine"):
            elasticache_config["engine"] = "redis"

        if not cluster_id:
            return _error("cluster_id is required.")

        clusters = data.setdefault("aws_elasticache_clusters", [])
        cluster = _find_one(clusters, "cluster_id", cluster_id)

        if not cluster:
            cluster = {
                "cluster_id": cluster_id,
                "node_type": elasticache_config.get("node_type", "cache.t3.micro"),
                "num_cache_nodes": elasticache_config.get("num_cache_nodes", 1),
                "engine": elasticache_config.get("engine", "redis"),
                "status": "available",
                "endpoint_url": f"redis://{cluster_id}.cache.amazonaws.com:6379",
            }
            clusters.append(cluster)
        else:
            cluster.update(
                {
                    "node_type": elasticache_config.get("node_type", cluster.get("node_type")),
                    "num_cache_nodes": elasticache_config.get(
                        "num_cache_nodes", cluster.get("num_cache_nodes")
                    ),
                    "engine": elasticache_config.get("engine", cluster.get("engine")),
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
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "configure_cache_integration",
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
