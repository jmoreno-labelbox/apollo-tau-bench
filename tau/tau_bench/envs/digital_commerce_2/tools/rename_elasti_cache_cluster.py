from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RenameElastiCacheCluster(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], cluster_id: Any, new_cluster_name: Any) -> str:
        cluster_id = _idstr(cluster_id)
        clusters = data.get("aws_elasticache_clusters", {}).values()
        for c in clusters.values():
            if c.get("cluster_id") == cluster_id:
                c["cluster_name"] = new_cluster_name
                payload = c
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No ElastiCache cluster found with ID '{cluster_id}'"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "renameElasticacheCluster",
                "description": "Rename an ElastiCache cluster.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                        "new_cluster_name": {"type": "string"},
                    },
                    "required": ["cluster_id", "new_cluster_name"],
                },
            },
        }
