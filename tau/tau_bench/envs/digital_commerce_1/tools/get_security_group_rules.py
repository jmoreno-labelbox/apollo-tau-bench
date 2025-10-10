# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSecurityGroupRules(Tool):
    @staticmethod
    def invoke(data, security_group_id: str) -> str:
        rows = data.setdefault("aws_security_group_rules", [])
        rules = [r for r in rows if str(r.get("security_group_id")) == security_group_id]
        return json.dumps({"security_group_id": security_group_id, "rules": rules})

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_security_group_rules",
                "description": "Read all rules for a given security group.",
                "parameters": {
                    "type": "object",
                    "properties": {"security_group_id": {"type": "string"}},
                    "required": ["security_group_id"],
                },
            },
        }
