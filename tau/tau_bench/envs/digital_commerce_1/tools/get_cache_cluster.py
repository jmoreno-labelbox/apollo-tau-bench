from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetCacheCluster(Tool):
    @staticmethod
    def invoke(data, cluster_id: str, endpoint_url: str = None, instance_type: str = None, security_group_id: str = None, status: str = None) -> str:
        rows = data.setdefault("aws_elasticache_clusters", [])
        row = next((r for r in rows if str(r.get("cluster_id")) == cluster_id), None)
        if not row:
            raise ValueError(f"cache cluster not found: {cluster_id}")
        payload = {
            "cluster_id": row["cluster_id"],
            "endpoint_url": row["endpoint_url"],
            "instance_type": row["instance_type"],
            "security_group_id": row["security_group_id"],
            "status": row["status"],
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetCacheCluster",
                "description": "Read existing ElastiCache cluster by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"cluster_id": {"type": "string"}},
                    "required": ["cluster_id"],
                },
            },
        }
