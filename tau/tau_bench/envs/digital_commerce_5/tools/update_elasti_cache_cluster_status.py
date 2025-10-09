from tau_bench.envs.tool import Tool
import json
import re
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateElastiCacheClusterStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], cluster_id: Any, status: Any, changed_at: Any
    ) -> str:
        cluster_id = _as_id(cluster_id)
        clusters = data.get("aws_elasticache_clusters", [])
        m = next(
            (c for c in clusters if _as_id(c.get("cluster_id")) == cluster_id), None
        )
        if not m:
            return _err("Cluster not found.")
        m["status"] = str(status)
        m["last_modified_at"] = str(changed_at)
        payload = {
            "cluster_id": cluster_id,
            "status": m["status"],
            "last_modified_at": m["last_modified_at"],
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
                "name": "UpdateElasticacheClusterStatus",
                "description": "Set the lifecycle status on an ElastiCache cluster.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                        "status": {"type": "string"},
                        "changed_at": {"type": "string"},
                    },
                    "required": ["cluster_id", "status", "changed_at"],
                },
            },
        }
