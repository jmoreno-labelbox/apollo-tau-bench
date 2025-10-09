from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class AddSecurityGroupRule(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
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
            "direction": str(direction),  #"ingress" or "egress"
            "protocol": str(protocol),  #for example, "tcp"
            "port": int(port),
            "cidr": str(cidr),
            "description": str(description),
        }
        rules.append(rec)
        payload = rec
        out = json.dumps(payload, indent=2)
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddSecurityGroupRule",
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
