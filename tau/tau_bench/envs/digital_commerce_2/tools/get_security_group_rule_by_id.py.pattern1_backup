# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSecurityGroupRuleById(Tool):
    """Fetch a security group rule by rule_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], rule_id: Any) -> str:
        rule_id = _idstr(rule_id)
        rules = data.get("aws_security_group_rules", [])
        for r in rules:
            if r.get("rule_id") == rule_id:
                return json.dumps(r, indent=2)
        return json.dumps({"error": f"No security group rule found with ID '{rule_id}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_security_group_rule_by_id",
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
