from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class ListSubnetGroups(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], aws_subnet_groups: list = None) -> str:
        groups = aws_subnet_groups if aws_subnet_groups is not None else []
        payload = {"subnet_groups": groups}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListSubnetGroups",
                "description": "List all ElastiCache subnet groups.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
