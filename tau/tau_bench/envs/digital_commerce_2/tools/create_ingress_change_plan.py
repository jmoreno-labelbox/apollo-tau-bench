# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateIngressChangePlan(Tool):
    name = "create_ingress_change_plan"
    description = "Create a deterministic ingress change plan ap-0001 for a given rule."

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        rule_id: Any,
        target_cidr: Any,
        final_description: Any = None,
        env_tag: Any = None,
    ) -> Dict[str, Any]:
        rules = list(data.get("aws_security_group_rules", {}).values())

        def find_rule(rid):
            if isinstance(rules, dict):
                return rules.get(rid)
            for r in rules:
                if r.get("rule_id") == rid:
                    return r
            return None

        rule = find_rule(rule_id)
        if not rule:
            return {"error": f"Unknown rule_id '{rule_id}'"}
        plan = {
            "plan_id": "ap-0001",
            "type": "ingress",
            "rule_id": rule_id,
            "target_cidr": target_cidr,
            "final_description": final_description,
            "env_tag": env_tag,
            "steps": ["update_rule", "consolidate", "standardize"],
        }
        rule["_pending_ingress_plan"] = plan
        data["_last_ingress_plan_rule_id"] = rule_id
        data["_last_ingress_plan_id"] = "ap-0001"
        return {"plan_id": "ap-0001", "steps": ["update_rule", "consolidate", "standardize"]}

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_ingress_change_plan",
                "description": "Create a plan (update, consolidate, standardize) for a rule_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rule_id": {"type": "string"},
                        "target_cidr": {"type": "string"},
                        "final_description": {"type": "string"},
                        "env_tag": {"type": "string"},
                    },
                    "required": ["rule_id", "target_cidr"],
                },
            },
        }
