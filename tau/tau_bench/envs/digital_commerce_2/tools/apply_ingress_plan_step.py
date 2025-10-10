# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ApplyIngressPlanStep(Tool):
    name = "apply_ingress_plan_step"
    description = "Apply a single step of the most recent ingress plan."

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        plan_id: Any,
        step_index: Any,
    ) -> Dict[str, Any]:
        rules = list(data.get("aws_security_group_rules", {}).values())

        def find_rule(rid):
            if isinstance(rules, dict):
                return rules.get(rid)
            for r in rules:
                if r.get("rule_id") == rid:
                    return r
            return None

        def remove_rules(ids):
            if isinstance(rules, dict):
                for rid in ids:
                    rules.pop(rid, None)
            else:
                idxs = [i for i, r in enumerate(rules) if r.get("rule_id") in ids]
                for i in sorted(idxs, reverse=True):
                    rules.pop(i)

        last_rule_id = data.get("_last_ingress_plan_rule_id")
        if not last_rule_id:
            return {"error": f"No ingress plan '{plan_id}'"}
        rule = find_rule(last_rule_id)
        if not rule:
            return {"error": f"No ingress plan '{plan_id}'"}
        plan = rule.get("_pending_ingress_plan")
        if not plan or plan.get("plan_id") != plan_id:
            return {"error": f"No ingress plan '{plan_id}'"}
        steps = plan.get("steps", [])
        i = int(step_index)
        if i < 0 or i >= len(steps):
            return {"error": f"Invalid step_index '{step_index}'"}
        action = steps[i]
        if action == "update_rule":
            rule["source_ip"] = plan["target_cidr"]
            rule["description"] = plan["final_description"]
            return {
                "rule_id": rule["rule_id"],
                "security_group_id": rule["security_group_id"],
                "protocol": rule.get("protocol", "TCP"),
                "port": rule.get("port", 6379),
                "source_ip": rule["source_ip"],
                "description": rule["description"],
            }
        if action == "consolidate":
            sg_id = rule["security_group_id"]
            port = rule.get("port", 6379)
            proto = rule.get("protocol", "TCP")
            same = []
            if isinstance(rules, dict):
                same = [
                    r
                    for r in rules.values()
                    if r.get("security_group_id") == sg_id
                    and r.get("port", 6379) == port
                    and r.get("protocol", "TCP") == proto
                ]
            else:
                same = [
                    r
                    for r in rules
                    if r.get("security_group_id") == sg_id
                    and r.get("port", 6379) == port
                    and r.get("protocol", "TCP") == proto
                ]
            keep_id = rule["rule_id"]
            removed = [r["rule_id"] for r in same if r.get("rule_id") != keep_id]
            remove_rules(removed)
            return {
                "consolidated_rule": {
                    "rule_id": rule["rule_id"],
                    "security_group_id": rule["security_group_id"],
                    "protocol": proto,
                    "port": port,
                    "source_ip": rule["source_ip"],
                    "description": rule["description"],
                },
                "removed": removed,
            }
        if action == "standardize":
            tag = plan.get("env_tag")
            updated = []
            if tag:
                if not str(rule.get("description", "")).endswith(f" [{tag}]"):
                    rule["description"] = f"{rule['description']} [{tag}]"
                updated.append(
                    {
                        "rule_id": rule["rule_id"],
                        "security_group_id": rule["security_group_id"],
                        "protocol": rule.get("protocol", "TCP"),
                        "port": rule.get("port", 6379),
                        "source_ip": rule["source_ip"],
                        "description": rule["description"],
                    }
                )
            return {"updated": updated, "count": len(updated)}
        return {"error": f"Unknown step '{action}'"}

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "apply_ingress_plan_step",
                "description": "Apply a single step by index for a previously created ingress plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "step_index": {"type": "integer"},
                    },
                    "required": ["plan_id", "step_index"],
                },
            },
        }
