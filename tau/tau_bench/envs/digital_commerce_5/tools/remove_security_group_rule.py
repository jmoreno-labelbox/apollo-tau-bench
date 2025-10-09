from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class RemoveSecurityGroupRule(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], aws_security_group_rules: list = None, rule_id: Any = None) -> str:
        rule_id = _as_id(rule_id)
        rules = aws_security_group_rules or []
        before = len(rules)
        data["aws_security_group_rules"] = [
            r for r in rules if _as_id(r.get("rule_id")) != rule_id
        ]
        if len(data["aws_security_group_rules"]) == before:
            return _err("Rule not found.")
        payload = {"deleted_rule_id": rule_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "removeSecurityGroupRule",
                "description": "Revoke a security group rule by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"rule_id": {"type": "string"}},
                    "required": ["rule_id"],
                },
            },
        }
