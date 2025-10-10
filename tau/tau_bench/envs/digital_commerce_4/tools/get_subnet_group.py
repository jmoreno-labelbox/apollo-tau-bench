# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSubnetGroup(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], subnet_group_id: Any) -> str:
        subnet_group_id = _as_id(subnet_group_id)
        groups = data.get("aws_subnet_groups", [])
        g = next((x for x in groups if _as_id(x.get("subnet_group_id")) == subnet_group_id), None)
        return json.dumps(g or {}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_subnet_group",
                "description": "Get a single ElastiCache subnet group by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"subnet_group_id": {"type": "string"}},
                    "required": ["subnet_group_id"],
                },
            },
        }
