from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetServiceSecurityGroup(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], environment: str, service_name: str) -> str:
        rules = _ensure_table(data, "aws_security_group_rules")
        # Gather all rules that correspond to environment and service
        matches = _find_all(rules, environment=environment, service_name=service_name)
        if matches:
            sg_id = matches[0]["sg_id"]
            ingress = [
                {"port": r["port"], "cidr": r["cidr"]}
                for r in matches
                if r.get("direction") == "ingress"
            ]
            egress = [
                {"port": r["port"], "cidr": r["cidr"]}
                for r in matches
                if r.get("direction") == "egress"
            ]
        else:
            # fixed sg id (not saved until an update applies rules)
            sg_id = _stable_id("sg", environment, service_name)
            ingress, egress = [], []
        return _json(
            {
                "environment": environment,
                "service_name": service_name,
                "sg_id": sg_id,
                "name": f"{service_name} [{environment}]",
                "ingress_rules": ingress,
                "egress_rules": egress,
            }
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetServiceSecurityGroup",
                "description": "Find the security group for a service in an environment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "environment": {
                            "type": "string",
                            "enum": ["DEV", "UAT", "PROD"],
                        },
                        "service_name": {"type": "string"},
                    },
                    "required": ["environment", "service_name"],
                },
            },
        }
