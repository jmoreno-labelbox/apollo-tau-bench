from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal

class GetSecurityGroupRuleById(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], rule_id: Any, aws_security_group_rules: list = None) -> str:
        rule_id = _idstr(rule_id)
        rules = aws_security_group_rules if aws_security_group_rules is not None else []
        for r in rules:
            if r.get("rule_id") == rule_id:
                payload = r
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No security group rule found with ID '{rule_id}'"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSecurityGroupRuleById",
                "description": "Fetch a single AWS security group rule by rule_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rule_id": {
                            "type": "string",
                            "description": "Exact security group rule_id.",
                        }
                    },
                    "required": ["rule_id"],
                },
            },
        }
