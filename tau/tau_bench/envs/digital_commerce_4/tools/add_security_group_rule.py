# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _next_sgr_id(data: Dict[str, Any]) -> str:
    n = len(data.get("aws_security_group_rules", [])) + 1
    return "sgr-" + f"{n:016x}"

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

class AddSecurityGroupRule(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        security_group_id: Any,
        protocol: Any,
        port: Any,
        source_ip: Any,
    ) -> str:
        rid = _next_sgr_id(data)
        rules = data.get("aws_security_group_rules", [])
        rec = {
            "rule_id": rid,
            "security_group_id": _as_id(security_group_id),
            "protocol": str(protocol).upper(),
            "port": int(port),
            "source_ip": str(source_ip),
        }
        rules.append(rec)
        data["aws_security_group_rules"] = rules
        return json.dumps(rec, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_security_group_rule",
                "description": "Add a rule to a security group (rule_id format: sgr- + 16 lowercase hex).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "security_group_id": {
                            "type": "string",
                            "description": "Target security group (sg-...).",
                        },
                        "protocol": {"type": "string", "description": "Protocol, e.g., 'TCP'."},
                        "port": {"type": "integer", "description": "Port number, e.g., 6379."},
                        "source_ip": {
                            "type": "string",
                            "description": "CIDR, e.g., '10.0.0.0/16'.",
                        },
                    },
                    "required": [
                        "security_group_id",
                        "protocol",
                        "port",
                        "source_ip",
                    ],
                },
            },
        }