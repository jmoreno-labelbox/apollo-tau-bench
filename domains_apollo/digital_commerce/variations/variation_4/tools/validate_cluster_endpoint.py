from tau_bench.envs.tool import Tool
import json
from typing import Any

class ValidateClusterEndpoint(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], cluster_id: str) -> str:
        cluster_id = _sid(cluster_id)
        clusters = data.get("aws_elasticache_clusters", [])
        cl = next((c for c in clusters if c.get("cluster_id") == cluster_id), None)
        if not cl:
            payload = {"error": f"cluster {cluster_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        ok = cl.get("status") == "available" and cl.get("endpoint_url") not in (
            None,
            "NULL",
            "",
        )
        payload = {
            "cluster_id": cluster_id,
            "valid": ok,
            "endpoint_url": cl.get("endpoint_url"),
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
                "name": "ValidateClusterEndpoint",
                "description": "Validate cluster is available and has a usable endpoint.",
                "parameters": {
                    "type": "object",
                    "properties": {"cluster_id": {"type": "string"}},
                    "required": ["cluster_id"],
                },
            },
        }
