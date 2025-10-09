from tau_bench.envs.tool import Tool
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateElastiCacheClusterConfig(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        cluster_id: Any,
        node_type: Any,
        num_nodes: Any,
        changed_at: Any,
    ) -> str:
        cluster_id = _as_id(cluster_id)
        clusters = data.get("aws_elasticache_clusters", [])
        c = next(
            (x for x in clusters if _as_id(x.get("cluster_id")) == cluster_id), None
        )
        if not c:
            return _err("Cluster not found.")
        c["node_type"] = str(node_type)
        c["num_nodes"] = int(num_nodes)
        c["last_modified_at"] = str(changed_at)
        payload = {
            "cluster_id": cluster_id,
            "node_type": c["node_type"],
            "num_nodes": c["num_nodes"],
            "last_modified_at": c["last_modified_at"],
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateElasticacheClusterConfig",
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
