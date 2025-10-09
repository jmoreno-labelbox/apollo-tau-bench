from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SetElastiCacheEndpointUrl(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], cluster_id: Any, endpoint_url: Any) -> str:
        cluster_id = _idstr(cluster_id)
        clusters = data.get("aws_elasticache_clusters", {}).values()
        for c in clusters.values():
            if c.get("cluster_id") == cluster_id:
                c["endpoint_url"] = endpoint_url
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
                "name": "setElasticacheEndpointUrl",
                "description": "Set or clear the endpoint_url for an ElastiCache cluster.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                        "endpoint_url": {
                            "type": "string",
                            "description": "Endpoint (or 'NULL' to clear).",
                        },
                    },
                    "required": ["cluster_id", "endpoint_url"],
                },
            },
        }
