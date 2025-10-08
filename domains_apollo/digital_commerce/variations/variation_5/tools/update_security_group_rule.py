from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class UpdateSecurityGroupRule(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], rule_id: Any, cidr: Any, description: Any) -> str:
        # Updates only the rules established through our add_security_group_rule (rule_id = 'SGR_####')
        rule_id = _as_id(rule_id)
        rules = data.get("aws_security_group_rules", [])
        r = next((x for x in rules if _as_id(x.get("rule_id")) == rule_id), None)
        if not r:
            return _err("Rule not found.")
        r["cidr"] = str(cidr)
        r["description"] = str(description)
        payload = {"rule_id": rule_id, "cidr": r["cidr"], "description": r["description"]}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateSecurityGroupRule",
                "description": "Update an existing security group rule's CIDR and description.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rule_id": {"type": "string"},
                        "cidr": {"type": "string"},
                        "description": {"type": "string"},
                    },
                    "required": ["rule_id", "cidr", "description"],
                },
            },
        }
