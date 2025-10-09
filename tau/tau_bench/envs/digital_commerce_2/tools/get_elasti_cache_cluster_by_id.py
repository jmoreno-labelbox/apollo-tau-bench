from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetElastiCacheClusterById(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], cluster_id: Any) -> str:
        cluster_id = _idstr(cluster_id)
        for c in data.get("aws_elasticache_clusters", {}).values():
            if c.get("cluster_id") == cluster_id:
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
                "name": "getElasticacheClusterById",
                "description": "Fetch an ElastiCache cluster by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"cluster_id": {"type": "string"}},
                    "required": ["cluster_id"],
                },
            },
        }
