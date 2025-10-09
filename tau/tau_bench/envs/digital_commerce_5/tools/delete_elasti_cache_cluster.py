from tau_bench.envs.tool import Tool
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class DeleteElastiCacheCluster(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cluster_id: Any, deleted_at: Any) -> str:
        cluster_id = _as_id(cluster_id)
        clusters = data.get("aws_elasticache_clusters", {}).values()
        m = next(
            (c for c in clusters.values() if _as_id(c.get("cluster_id")) == cluster_id), None
        )
        if not m:
            return _err("Cluster not found.")
        m["status"] = "Deleted"
        m["deleted_at"] = str(deleted_at)
        m["last_modified_at"] = str(deleted_at)
        payload = {"cluster_id": cluster_id, "status": "Deleted"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeleteElasticacheCluster",
                "description": "Mark an ElastiCache cluster as Deleted.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                        "deleted_at": {"type": "string"},
                    },
                    "required": ["cluster_id", "deleted_at"],
                },
            },
        }
