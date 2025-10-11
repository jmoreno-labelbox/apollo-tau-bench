# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _err(msg: str) -> str:
    return json.dumps({"error": msg}, indent=2)

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

class UpdateElastiCacheClusterConfig(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], cluster_id: Any, node_type: Any, num_nodes: Any, changed_at: Any
    ) -> str:
        cluster_id = _as_id(cluster_id)
        clusters = data.get("aws_elasticache_clusters", [])
        c = next((x for x in clusters if _as_id(x.get("cluster_id")) == cluster_id), None)
        if not c:
            return _err("Cluster not found.")
        c["node_type"] = str(node_type)
        c["num_nodes"] = int(num_nodes)
        c["last_modified_at"] = str(changed_at)
        return json.dumps(
            {
                "cluster_id": cluster_id,
                "node_type": c["node_type"],
                "num_nodes": c["num_nodes"],
                "last_modified_at": c["last_modified_at"],
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_elasticache_cluster_config",
                "description": "Resize an ElastiCache cluster (node_type / num_nodes).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                        "node_type": {"type": "string"},
                        "num_nodes": {"type": "integer"},
                        "changed_at": {"type": "string"},
                    },
                    "required": ["cluster_id", "node_type", "num_nodes", "changed_at"],
                },
            },
        }