from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SetElastiCacheClusterStatus(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], cluster_id: Any, new_status: Any) -> str:
        cluster_id = _idstr(cluster_id)
        clusters = data.get("aws_elasticache_clusters", [])
        for c in clusters:
            if c.get("cluster_id") == cluster_id:
                c["status"] = new_status
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
                "name": "setElasticacheClusterStatus",
                "description": "Set the status field for an ElastiCache cluster.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                        "new_status": {"type": "string"},
                    },
                    "required": ["cluster_id", "new_status"],
                },
            },
        }
