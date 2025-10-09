from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ApplyClusterPlanStep(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], plan_id: Any, step_index: Any) -> str:
        pass
        plan_id = _idstr(plan_id)
        step_index = int(step_index)
        # retrieve the plan
        plan = None
        for p in data.get("aws_plans", {}).values():
            if p.get("plan_id") == plan_id and p.get("type") == "cluster":
                plan = p
                break
        if not plan:
            payload = {"error": f"No cluster plan '{plan_id}'"}
            out = json.dumps(payload, indent=2)
            return out
        steps = plan.get("steps", [])
        if step_index < 0 or step_index >= len(steps):
            payload = {"error": f"Invalid step_index {step_index}"}
            out = json.dumps(payload, indent=2)
            return out

        # find the cluster
        cl = None
        for c in data.get("aws_elasticache_clusters", {}).values():
            if c.get("cluster_id") == plan["cluster_id"]:
                cl = c
                break
        if not cl:
            payload = {"error": f"Missing cluster '{plan['cluster_id']}'"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        step = steps[step_index]
        if step == "attach_sg":
            cl["security_group_id"] = plan["security_group_id"]
            payload = cl
            out = json.dumps(payload, indent=2)
            return out

        if step == "set_subnet":
            cl["subnet_group_id"] = plan["subnet_group_id"]
            payload = cl
            out = json.dumps(payload, indent=2)
            return out

        if step == "set_status":
            cl["status"] = plan["new_status"]
            payload = cl
            out = json.dumps(payload, indent=2)
            return out

        if step == "set_name":
            cl["cluster_name"] = plan["new_name"]
            payload = cl
            out = json.dumps(payload, indent=2)
            return out

        if step == "set_note":
            cl["instance_type_note"] = plan["note"]
            payload = cl
            out = json.dumps(payload, indent=2)
            return out

        if step == "standardize_env_on_sg" or step == "consolidate_redis_on_sg":
            # manage rules for this Security Group
            sg_id = plan["security_group_id"]
            rules = data.get("aws_security_group_rules", {}).values()
            if step == "standardize_env_on_sg":
                tag = plan["env_tag"]
                changed = []
                tag_norm = (
                    tag if tag.startswith("[") and tag.endswith("]") else f"[{tag}]"
                )
                for r in rules.values()):
                    if r.get("security_group_id") == sg_id and r.get("port") == 6379:
                        d = r.get("description", "")
                        if tag_norm not in d:
                            r["description"] = (d + " " + tag_norm).strip()
                            changed.append(r)
                payload = {"updated": changed, "count": len(changed)}
                out = json.dumps(payload, indent=2)
                return out

            if step == "consolidate_redis_on_sg":
                keep = None
                removed = []
                remain = []
                for r in rules.values():
                    if r.get("security_group_id") == sg_id and r.get("port") == 6379:
                        if keep is None:
                            keep = r
                        else:
                            removed.append(r)
                            continue
                    remain.append(r)
                data["aws_security_group_rules"] = remain + ([keep] if keep else [])
                if keep is None:
                    new_rule = {
                        "rule_id": f"sgr-auto-{len(data['aws_security_group_rules'])+1:04d}",
                        "security_group_id": sg_id,
                        "port": 6379,
                        "protocol": "TCP",
                        "source_ip": plan["consolidate_cidr"],
                        "description": plan["consolidate_desc"],
                    }
                    data["aws_security_group_rules"].append(new_rule)
                    payload = {"consolidated_rule": new_rule, "removed": removed}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
                else:
                    keep["source_ip"] = plan["consolidate_cidr"]
                    keep["description"] = plan["consolidate_desc"]
                    payload = {"consolidated_rule": keep, "removed": removed}
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out

        if step == "set_endpoint":
            cl["endpoint_url"] = plan["endpoint_url"]
            payload = cl
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
                "name": "ApplyClusterPlanStep",
                "description": "Apply a single step by index for a previously created cluster plan.",
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
