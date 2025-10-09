from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AddSecurityGroupRule(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        security_group_id: Any,
        port: Any,
        protocol: Any,
        source_ip: Any
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
        payload = {"rule_id": new_id}
        out = json.dumps(payload, indent=2)
        return out
        pass
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
        payload = {"rule_id": new_id}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddSecurityGroupRule",
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
