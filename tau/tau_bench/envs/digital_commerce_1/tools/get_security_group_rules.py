from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetSecurityGroupRules(Tool):
    @staticmethod
    def invoke(data, security_group_id: str) -> str:
        rows = data.setdefault("aws_security_group_rules", [])
        rules = [
            r for r in rows if str(r.get("security_group_id")) == security_group_id
        ]
        payload = {"security_group_id": security_group_id, "rules": rules}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "getSecurityGroupRules",
                "description": "Read all rules for a given security group.",
                "parameters": {
                    "type": "object",
                    "properties": {"security_group_id": {"type": "string"}},
                    "required": ["security_group_id"],
                },
            },
        }
