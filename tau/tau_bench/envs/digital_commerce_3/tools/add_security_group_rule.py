# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _next_numeric_id(existing: List[Dict[str, Any]], field: str) -> str:
    max_id = 0
    for row in existing:
        try:
            max_id = max(max_id, int(row.get(field)))
        except (TypeError, ValueError):
            continue
    return str(max_id + 1)

def _idstr(v):
    """Coerce numeric IDs to strings; leave None/strings unchanged."""
    return str(v) if isinstance(v, int) else v

class AddSecurityGroupRule(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], security_group_id: Any, port: Any, protocol: Any, source_ip: Any
    ) -> str:
        security_group_id = _idstr(security_group_id)
        port = int(port)
        protocol = f"{protocol}"
        source_ip = f"{source_ip}"
        rules = data.get("aws_security_group_rules", [])
        new_id = f"sgr-{_next_numeric_id(rules, 'rule_seq')}"
        rules.append(
            {
                "rule_id": new_id,
                "security_group_id": security_group_id,
                "port": port,
                "protocol": protocol,
                "source_ip": source_ip,
                "description": "Added via API",
                "rule_seq": new_id.split("-")[1],
            }
        )
        return json.dumps({"rule_id": new_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_security_group_rule",
                "description": "Appends a security group rule entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "security_group_id": {"type": "string"},
                        "port": {"type": "integer"},
                        "protocol": {"type": "string"},
                        "source_ip": {"type": "string"},
                    },
                    "required": ["security_group_id", "port", "protocol", "source_ip"],
                },
            },
        }