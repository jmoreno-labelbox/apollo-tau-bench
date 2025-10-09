from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class ListElastiCacheClusters(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], aws_elasticache_clusters: list = None) -> str:
        clusters = aws_elasticache_clusters if aws_elasticache_clusters is not None else []
        payload = {"clusters": clusters}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListElasticacheClusters",
                "description": "List all ElastiCache clusters.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
