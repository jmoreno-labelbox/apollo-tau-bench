from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class HardenRedisSecurityGroup(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], security_group_id: str, allowed_cidr_list: list[str]
    ) -> str:
        security_group_id = _sid(security_group_id)
        rules = data.get("aws_security_group_rules", [])
        changed = []
        for r in list(rules):
            if (
                r.get("security_group_id") == security_group_id
                and r.get("port") == 6379
                and r.get("protocol") == "TCP"
                and r.get("source_ip") == "0.0.0.0/0"
            ):
                rules.remove(r)
                changed.append(r.get("rule_id"))
        existing = {
            (x.get("port"), x.get("protocol"), x.get("source_ip"))
            for x in rules
            if x.get("security_group_id") == security_group_id
        }
        for cidr in allowed_cidr_list:
            key = (6379, "TCP", cidr)
            if key not in existing:
                new_rule_id = f"sgr-{security_group_id}-{cidr.replace('/', '_')}"
                rules.append(
                    {
                        "rule_id": new_rule_id,
                        "security_group_id": security_group_id,
                        "port": 6379,
                        "protocol": "TCP",
                        "source_ip": cidr,
                        "description": "Allow Redis access from approved CIDR",
                    }
                )
                changed.append(new_rule_id)
        payload = {"security_group_id": security_group_id, "changed": changed}
        out = json.dumps(
            payload, indent=2
        )
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "HardenRedisSecurityGroup",
                "description": "Remove 0.0.0.0/0 Redis access and add approved CIDRs for port 6379/TCP.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "security_group_id": {"type": "string"},
                        "allowed_cidr_list": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["security_group_id", "allowed_cidr_list"],
                },
            },
        }
