# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class OptimizeSecurityGroupRules(Tool):
    """Optimize security group rules by removing overly permissive access and adding specific rules."""

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        security_group_id: Any,
        allowed_cidr: Any = None,
        target_port: Any = 6379,
    ) -> str:
        security_group_id = _idstr(security_group_id)
        allowed_cidr = f"{allowed_cidr}" if allowed_cidr is not None else None
        target_port = int(target_port)

        if not security_group_id:
            return _error("security_group_id is required.")

        allowed_cidrs = [allowed_cidr] if allowed_cidr else []
        rules = data.get("aws_security_group_rules", [])
        changes = []

        rules_to_remove = []
        for rule in rules:
            if (
                f"{rule.get('security_group_id')}" == f"{security_group_id}"
                and int(rule.get("port")) == target_port
                and rule.get("protocol") == "TCP"
                and rule.get("source_ip") == "0.0.0.0/0"
            ):
                rules_to_remove.append(rule)
                changes.append(f"Removed overly permissive rule: {rule.get('rule_id')}")

        for rule in rules_to_remove:
            rules.remove(rule)

        existing_cidrs = {
            r.get("source_ip")
            for r in rules
            if f"{r.get('security_group_id')}" == f"{security_group_id}"
            and int(r.get("port")) == target_port
        }

        for cidr in allowed_cidrs:
            if cidr not in existing_cidrs:
                new_rule_id = f"sgr-{security_group_id}-{cidr.replace('/', '_')}-{target_port}"
                rules.append(
                    {
                        "rule_id": new_rule_id,
                        "security_group_id": security_group_id,
                        "port": target_port,
                        "protocol": "TCP",
                        "source_ip": cidr,
                        "description": f"Allow {target_port} access from approved CIDR {cidr}",
                    }
                )
                changes.append(f"Added rule for CIDR: {cidr}")

        result = {
            "security_group_id": security_group_id,
            "target_port": target_port,
            "changes": changes,
            "allowed_cidrs": allowed_cidrs,
        }
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "optimize_security_group_rules",
                "description": "Optimize security group rules by removing overly permissive access and adding specific rules.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "security_group_id": {"type": "string"},
                        "allowed_cidr": {"type": "string"},
                        "target_port": {"type": "integer"},
                    },
                    "required": ["security_group_id"],
                },
            },
        }
