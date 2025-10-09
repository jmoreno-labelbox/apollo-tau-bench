from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class DeleteSubnetGroup(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], subnet_group_id: Any, aws_subnet_groups: list = None) -> str:
        subnet_group_id = _as_id(subnet_group_id)
        groups = aws_subnet_groups if aws_subnet_groups is not None else data.get("aws_subnet_groups", [])
        before = len(groups)
        data["aws_subnet_groups"] = [
            g for g in groups if _as_id(g.get("subnet_group_id")) != subnet_group_id
        ]
        if len(data["aws_subnet_groups"]) == before:
            return _err("Subnet group not found.")
        payload = {"deleted_subnet_group_id": subnet_group_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteSubnetGroup",
                "description": "Delete an ElastiCache subnet group.",
                "parameters": {
                    "type": "object",
                    "properties": {"subnet_group_id": {"type": "string"}},
                    "required": ["subnet_group_id"],
                },
            },
        }
