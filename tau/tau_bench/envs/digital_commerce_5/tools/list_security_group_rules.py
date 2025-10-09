from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class ListSecurityGroupRules(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], group_id: Any, aws_security_group_rules: list = None) -> str:
        group_id = _as_id(group_id)
        rules = aws_security_group_rules if aws_security_group_rules is not None else []
        rows = [r for r in rules.values() if _as_id(r.get("group_id")) == group_id]
        payload = {"group_id": group_id, "rules": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListSecurityGroupRules",
                "description": "List ingress/egress rules for a security group.",
                "parameters": {
                    "type": "object",
                    "properties": {"group_id": {"type": "string"}},
                    "required": ["group_id"],
                },
            },
        }
