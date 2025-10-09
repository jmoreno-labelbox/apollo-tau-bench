from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class GetSubnetGroup(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], subnet_group_id: Any, aws_subnet_groups: list = None) -> str:
        subnet_group_id = _as_id(subnet_group_id)
        groups = aws_subnet_groups or []
        g = next(
            (x for x in groups if _as_id(x.get("subnet_group_id")) == subnet_group_id),
            None,
        )
        payload = g or {}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSubnetGroup",
                "description": "Get a single ElastiCache subnet group by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"subnet_group_id": {"type": "string"}},
                    "required": ["subnet_group_id"],
                },
            },
        }
