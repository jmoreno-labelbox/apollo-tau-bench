# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ApplyClusterPlanStep(Tool):
    name = "apply_cluster_plan_step"
    description = "Apply a single step of the most recent cluster plan."

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        plan_id: Any,
        step_index: Any,
    ) -> Dict[str, Any]:
        clusters = data.get("aws_clusters", [])
        rules = data.get("aws_security_group_rules", [])

        def find_cluster(cid):
            if isinstance(clusters, dict):
                return clusters.get(cid)
            for c in clusters:
                if c.get("cluster_id") == cid:
                    return c
            return None

        def find_rule(rid):
            if isinstance(rules, dict):
                return rules.get(rid)
            for r in rules:
                if r.get("rule_id") == rid:
                    return r
            return None

        def iter_rules():
            if isinstance(rules, dict):
                return list(rules.values())
            return list(rules)

        def remove_rules(ids):
            if isinstance(rules, dict):
                for rid in ids:
                    rules.pop(rid, None)
            else:
                idxs = [i for i, r in enumerate(rules) if r.get("rule_id") in ids]
                for i in sorted(idxs, reverse=True):
                    rules.pop(i)

        last_cid = data.get("_last_cluster_plan_cluster_id")
        if not last_cid:
            return {"error": f"No cluster plan '{plan_id}'"}
        cluster = find_cluster(last_cid)
        if not cluster:
            return {"error": f"No cluster plan '{plan_id}'"}
        plan = cluster.get("_pending_cluster_plan")
        if not plan or plan.get("plan_id") != plan_id:
            return {"error": f"No cluster plan '{plan_id}'"}
        i = int(step_index)
        steps = plan.get("steps", [])
        if i < 0 or i >= len(steps):
            return {"error": f"Invalid step_index '{step_index}'"}
        action = steps[i]
        if action == "attach_sg":
            rule = find_rule(plan["reference_rule_id"])
            if rule:
                cluster["security_group_id"] = rule["security_group_id"]
            return {
                "cluster_id": cluster["cluster_id"],
                "security_group_id": cluster.get("security_group_id"),
            }
        if action == "attach_subnet_group":
            cluster["subnet_group_id"] = plan["subnet_group_id"]
            return {
                "cluster_id": cluster["cluster_id"],
                "subnet_group_id": cluster["subnet_group_id"],
            }
        if action == "set_status":
            cluster["status"] = plan["new_status"]
            return {"cluster_id": cluster["cluster_id"], "status": cluster["status"]}
        if action == "set_name":
            cluster["name"] = plan["new_name"]
            return {"cluster_id": cluster["cluster_id"], "name": cluster["name"]}
        if action == "set_note":
            cluster["note"] = plan["note"]
            return {"cluster_id": cluster["cluster_id"], "note": cluster["note"]}
        if action == "consolidate_ingress":
            sg_id = cluster.get("security_group_id")
            port = 6379
            proto = "TCP"
            same = [
                r
                for r in iter_rules()
                if r.get("security_group_id") == sg_id
                and r.get("port", 6379) == port
                and r.get("protocol", "TCP") == proto
            ]
            keep = same[0] if same else None
            removed = [r["rule_id"] for r in same[1:]] if len(same) > 1 else []
            if removed:
                remove_rules(removed)
            if keep:
                if plan.get("consolidate_cidr") is not None:
                    keep["source_ip"] = plan["consolidate_cidr"]
                if plan.get("consolidate_desc") is not None:
                    keep["description"] = plan["consolidate_desc"]
            return {"security_group_id": sg_id, "port": port}
        if action == "standardize_env_on_sg":
            tag = plan.get("env_tag")
            updated = 0
            if tag:
                sg_id = cluster.get("security_group_id")
                for r in iter_rules():
                    if r.get("security_group_id") != sg_id:
                        continue
                    if not str(r.get("description", "")).endswith(f" [{tag}]"):
                        r["description"] = f"{r['description']} [{tag}]"
                        updated += 1
            return {"updated": updated}
        if action == "set_endpoint":
            ep = plan.get("endpoint_url")
            if ep == "NULL":
                cluster["endpoint_url"] = None
            elif ep and ep != "NOCHANGE":
                cluster["endpoint_url"] = ep
            return {
                "cluster_id": cluster["cluster_id"],
                "endpoint_url": cluster.get("endpoint_url"),
            }
        return {"error": f"Unknown step '{action}'"}

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "apply_cluster_plan_step",
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
