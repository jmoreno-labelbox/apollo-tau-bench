from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class CreateSubnetGroup(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        subnet_group_id: Any,
        name: Any,
        description: Any,
        subnet_ids: Any,
        vpc_id: Any,
    ) -> str:
        subnet_group_id = _as_id(subnet_group_id)
        groups = data.setdefault("aws_subnet_groups", [])
        existing = next(
            (g for g in groups if _as_id(g.get("subnet_group_id")) == subnet_group_id),
            None,
        )
        if existing:
            payload = existing
            out = json.dumps(payload, indent=2)
            return out
        rec = {
            "subnet_group_id": subnet_group_id,
            "name": str(name),
            "description": str(description),
            "subnet_ids": [str(s) for s in (subnet_ids or [])],
            "vpc_id": _as_id(vpc_id),
        }
        groups.append(rec)
        payload = rec
        out = json.dumps(payload, indent=2)
        return out
        

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateSubnetGroup",
                "description": "Create an ElastiCache subnet group.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subnet_group_id": {"type": "string"},
                        "name": {"type": "string"},
                        "description": {"type": "string"},
                        "subnet_ids": {"type": "array", "items": {"type": "string"}},
                        "vpc_id": {"type": "string"},
                    },
                    "required": [
                        "subnet_group_id",
                        "name",
                        "description",
                        "subnet_ids",
                        "vpc_id",
                    ],
                },
            },
        }
