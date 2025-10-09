from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateIngressChangePlan(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        rule_id: Any,
        target_cidr: Any,
        final_description: Any,
        env_tag: Any,
    ) -> str:
        rule_id = _idstr(rule_id)
        target_cidr = str(target_cidr)
        final_description = str(final_description)
        env_tag = str(env_tag)
        # locate the rule
        rule = None
        for r in data.get("aws_security_group_rules", []):
            if r.get("rule_id") == rule_id:
                rule = r
                break
        if not rule:
            payload = {"error": f"No security group rule found with ID '{rule_id}'"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        plan = {
            "plan_id": _next_aws_plan_id(data),
            "type": "ingress",
            "rule_id": rule_id,
            "security_group_id": rule["security_group_id"],
            "port": rule["port"],
            "protocol": rule["protocol"],
            "target_cidr": target_cidr,
            "final_description": final_description,
            "env_tag": env_tag,
            "steps": ["update_rule", "consolidate", "standardize"],
        }
        data.setdefault("aws_plans", []).append(plan)
        payload = {"plan_id": plan["plan_id"], "steps": plan["steps"]}
        out = json.dumps(
            payload, indent=2
        )
        return out
           

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateIngressChangePlan",
                "description": "Create a plan (update, consolidate, standardize) for a rule_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rule_id": {"type": "string"},
                        "target_cidr": {"type": "string"},
                        "final_description": {"type": "string"},
                        "env_tag": {"type": "string"},
                    },
                    "required": [
                        "rule_id",
                        "target_cidr",
                        "final_description",
                        "env_tag",
                    ],
                },
            },
        }
