# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListElastiCacheClusters(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        clusters = data.get("aws_elasticache_clusters", [])
        return json.dumps({"clusters": clusters}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_elasticache_clusters",
                "description": "List all ElastiCache clusters.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
