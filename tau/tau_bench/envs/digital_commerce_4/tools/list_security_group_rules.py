from tau_bench.envs.tool import Tool
import json
from typing import Any

class ListSecurityGroupRules(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], security_group_id: str) -> str:
        security_group_id = _sid(security_group_id)
        rules = data.get("aws_security_group_rules", [])
        result = [r for r in rules if r.get("security_group_id") == security_group_id]
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListSecurityGroupRules",
                "description": "List SG rules for a given security group.",
                "parameters": {
                    "type": "object",
                    "properties": {"security_group_id": {"type": "string"}},
                    "required": ["security_group_id"],
                },
            },
        }
