# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _as_id(x: Any) -> str:
    if x is None:
        return x
    if isinstance(x, str):
        return x
    if isinstance(x, int):
        return str(x)
    if isinstance(x, float) and x.is_integer():
        return str(int(x))
    return str(x)

class ListSecurityGroupRules(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], group_id: Any) -> str:
        group_id = _as_id(group_id)
        rules = data.get("aws_security_group_rules", [])
        rows = [r for r in rules if _as_id(r.get("group_id")) == group_id]
        return json.dumps({"group_id": group_id, "rules": rows}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_security_group_rules",
                "description": "List ingress/egress rules for a security group.",
                "parameters": {
                    "type": "object",
                    "properties": {"group_id": {"type": "string"}},
                    "required": ["group_id"],
                },
            },
        }