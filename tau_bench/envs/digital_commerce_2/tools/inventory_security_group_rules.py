from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal

class InventorySecurityGroupRules(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], aws_security_group_rules: list[dict[str, Any]] = None) -> str:
        rules = aws_security_group_rules or []
        payload = {"rule_ids": [r.get("rule_id") for r in rules]}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InventorySecurityGroupRules",
                "description": "List all AWS security group rule IDs.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
