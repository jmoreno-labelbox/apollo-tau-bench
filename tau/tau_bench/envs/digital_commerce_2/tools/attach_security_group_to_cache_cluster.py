from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AttachSecurityGroupToCacheCluster(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], cluster_id: Any, security_group_id: Any) -> str:
        cluster_id = _idstr(cluster_id)
        security_group_id = _idstr(security_group_id)
        clusters = data.get("aws_elasticache_clusters", [])
        for c in clusters:
            if c.get("cluster_id") == cluster_id:
                c["security_group_id"] = security_group_id
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
                "name": "attachSecurityGroupToCacheCluster",
                "description": "Set the security_group_id for an ElastiCache cluster.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                        "security_group_id": {"type": "string"},
                    },
                    "required": ["cluster_id", "security_group_id"],
                },
            },
        }
