from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal

class ApplyIngressPlanStep(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], plan_id: Any, step_index: Any) -> str:
        pass
        plan_id = _idstr(plan_id)
        step_index = int(step_index)
        #retrieve plan
        plan = None
        for p in data.get("aws_plans", []):
            if p.get("plan_id") == plan_id and p.get("type") == "ingress":
                plan = p
                break
        if not plan:
            payload = {"error": f"No ingress plan '{plan_id}'"}
            out = json.dumps(payload, indent=2)
            return out
        steps = plan.get("steps", [])
        if step_index < 0 or step_index >= len(steps):
            payload = {"error": f"Invalid step_index {step_index}"}
            out = json.dumps(payload, indent=2)
            return out

        sg_id = plan["security_group_id"]
        rules = data.get("aws_security_group_rules", [])
        step = steps[step_index]

        def _append_tag(desc: str, tag: str) -> str:
            pass
            tag = tag if tag.startswith("[") and tag.endswith("]") else f"[{tag}]"
            if tag in desc:  #prevent duplicates
                return desc
            return f"{desc} {tag}".strip()

        if step == "update_rule":
            #assign source and description to the original rule
            for r in rules:
                if r.get("rule_id") == plan["rule_id"]:
                    r["source_ip"] = plan["target_cidr"]
                    r["description"] = plan["final_description"]
                    payload = r
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Missing rule '{plan['rule_id']}'"}
            out = json.dumps(payload, indent=2)
            return out

        if step == "consolidate":
            #confirm there is precisely one 6379/TCP rule in this Security Group
            keep = None
            removed = []
            remain = []
            for r in rules:
                if r.get("security_group_id") == sg_id and r.get("port") == 6379:
                    if keep is None:
                        keep = r
                    else:
                        removed.append(r)
                        continue
                remain.append(r)
            data["aws_security_group_rules"] = remain + ([keep] if keep else [])
            if keep is None:
                #generate one
                new_rule = {
                    "rule_id": f"sgr-auto-{len(data['aws_security_group_rules'])+1:04d}",
                    "security_group_id": sg_id,
                    "port": 6379,
                    "protocol": "TCP",
                    "source_ip": plan["target_cidr"],
                    "description": plan["final_description"],
                }
                data["aws_security_group_rules"].append(new_rule)
                payload = {"consolidated_rule": new_rule, "removed": removed}
                out = json.dumps(
                    payload, indent=2
                )
                return out
            else:
                keep["source_ip"] = plan["target_cidr"]
                keep["description"] = plan["final_description"]
                payload = {"consolidated_rule": keep, "removed": removed}
                out = json.dumps(
                    payload, indent=2
                )
                return out

        if step == "standardize":
            #add environment tag to every 6379 rule in this Security Group
            updated = []
            tag = plan["env_tag"]
            for r in rules:
                if r.get("security_group_id") == sg_id and r.get("port") == 6379:
                    before = r.get("description", "")
                    after = _append_tag(before, tag)
                    if after != before:
                        r["description"] = after
                        updated.append(r)
            payload = {"updated": updated, "count": len(updated)}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": f"Unsupported step '{step}'"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ApplyIngressPlanStep",
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
