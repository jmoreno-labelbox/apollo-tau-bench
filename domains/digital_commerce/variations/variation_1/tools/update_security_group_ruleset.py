from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateSecurityGroupRuleset(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        sg_id: str,
        environment: str,
        service_name: str,
        tcp_ports: list[int],
        allowlist_cidrs: list[str]
    ) -> str:
        rules = _ensure_table(data, "aws_security_group_rules")
        for port in tcp_ports:
            for cidr in allowlist_cidrs:
                row = _find_one(
                    rules,
                    sg_id=sg_id,
                    environment=environment,
                    service_name=service_name,
                    direction="ingress",
                    protocol="tcp",
                    port=int(port),
                    cidr=cidr,
                )
                if row:
                    row["updated_at"] = FIXED_NOW
                else:
                    rules.append(
                        {
                            "sg_id": sg_id,
                            "environment": environment,
                            "service_name": service_name,
                            "direction": "ingress",
                            "protocol": "tcp",
                            "port": int(port),
                            "cidr": cidr,
                            "description": f"{service_name} [{environment}] ingress {port}/{cidr}",
                            "created_at": FIXED_NOW,
                        }
                    )
        summary = f"{service_name} [{environment}] ports={sorted(set(tcp_ports))} cidrs={sorted(set(allowlist_cidrs))}"
        return _json(
            {
                "change_set_id": _stable_id(
                    "chg-sg",
                    sg_id,
                    environment,
                    service_name,
                    *map(str, tcp_ports),
                    *allowlist_cidrs,
                ),
                "labels": {"summary": summary},
                "applied": True,
            }
        )
        pass
        rules = _ensure_table(data, "aws_security_group_rules")
        for port in tcp_ports:
            for cidr in allowlist_cidrs:
                row = _find_one(
                    rules,
                    sg_id=sg_id,
                    environment=environment,
                    service_name=service_name,
                    direction="ingress",
                    protocol="tcp",
                    port=int(port),
                    cidr=cidr,
                )
                if row:
                    row["updated_at"] = FIXED_NOW
                else:
                    rules.append(
                        {
                            "sg_id": sg_id,
                            "environment": environment,
                            "service_name": service_name,
                            "direction": "ingress",
                            "protocol": "tcp",
                            "port": int(port),
                            "cidr": cidr,
                            "description": f"{service_name} [{environment}] ingress {port}/{cidr}",
                            "created_at": FIXED_NOW,
                        }
                    )
        summary = f"{service_name} [{environment}] ports={sorted(set(tcp_ports))} cidrs={sorted(set(allowlist_cidrs))}"
        return _json(
            {
                "change_set_id": _stable_id(
                    "chg-sg",
                    sg_id,
                    environment,
                    service_name,
                    *map(str, tcp_ports),
                    *allowlist_cidrs,
                ),
                "labels": {"summary": summary},
                "applied": True,
            }
        )

    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpdateSecurityGroupRuleset",
                "description": "Upsert ingress rules for an SG using env/service context.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sg_id": {"type": "string"},
                        "environment": {
                            "type": "string",
                            "enum": ["DEV", "UAT", "PROD"],
                        },
                        "service_name": {"type": "string"},
                        "tcp_ports": {"type": "array", "items": {"type": "integer"}},
                        "allowlist_cidrs": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": [
                        "sg_id",
                        "environment",
                        "service_name",
                        "tcp_ports",
                        "allowlist_cidrs",
                    ],
                },
            },
        }
