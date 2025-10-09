from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal

class SetElastiCacheSubnetGroup(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], cluster_id: Any, subnet_group_id: Any, aws_subnet_groups: list = None, aws_elasticache_clusters: list = None) -> str:
        cluster_id = _idstr(cluster_id)
        subnet_group_id = _idstr(subnet_group_id)

        # Check if the subnet group is present
        groups = aws_subnet_groups or []
        if not any(g.get("subnet_group_id") == subnet_group_id for g in groups):
            payload = {"error": f"No subnet group found with ID '{subnet_group_id}'"}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        clusters = aws_elasticache_clusters or []
        for c in clusters:
            if c.get("cluster_id") == cluster_id:
                c["subnet_group_id"] = subnet_group_id
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
                "name": "setElasticacheSubnetGroup",
                "description": "Set the subnet_group_id for an ElastiCache cluster.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                        "subnet_group_id": {"type": "string"},
                    },
                    "required": ["cluster_id", "subnet_group_id"],
                },
            },
        }
