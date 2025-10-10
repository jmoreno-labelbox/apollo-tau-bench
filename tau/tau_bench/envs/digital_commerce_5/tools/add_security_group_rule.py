# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddSecurityGroupRule(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        group_id: Any,
        direction: Any,
        protocol: Any,
        port: Any,
        cidr: Any,
        description: Any,
    ) -> str:
        rules = data.setdefault("aws_security_group_rules", [])
        rid = f"SGR_{len(rules)+1:04d}"
        rec = {
            "rule_id": rid,
            "group_id": _as_id(group_id),
            "direction": str(direction),  # "entry" | "exit"
            "protocol": str(protocol),  # for example, "tcp"
            "port": int(port),
            "cidr": str(cidr),
            "description": str(description),
        }
        rules.append(rec)
        return json.dumps(rec, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_security_group_rule",
                "description": "Authorize a CIDR rule on a security group.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "group_id": {"type": "string"},
                        "direction": {"type": "string"},
                        "protocol": {"type": "string"},
                        "port": {"type": "integer"},
                        "cidr": {"type": "string"},
                        "description": {"type": "string"},
                    },
                    "required": [
                        "group_id",
                        "direction",
                        "protocol",
                        "port",
                        "cidr",
                        "description",
                    ],
                },
            },
        }
