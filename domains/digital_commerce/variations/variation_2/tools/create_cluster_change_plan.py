from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal

class CreateClusterChangePlan(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
        cluster_id: Any,
        reference_rule_id: Any,
        subnet_group_id: Any,
        new_status: Any,
        new_name: Any,
        note: Any,
        env_tag: Any,
        consolidate_cidr: Any,
        consolidate_desc: Any,
        endpoint_url: Any,
    ) -> str:
        cluster_id = _idstr(cluster_id)
        reference_rule_id = _idstr(reference_rule_id)
        subnet_group_id = _idstr(subnet_group_id)
        # does the cluster exist?
        cluster = None
        for c in data.get("aws_elasticache_clusters", []):
            if c.get("cluster_id") == cluster_id:
                cluster = c
                break
        if not cluster:
            payload = {"error": f"No ElastiCache cluster '{cluster_id}'"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        # does the rule exist?
        sg_id = None
        proto = None
        port = None
        for r in data.get("aws_security_group_rules", []):
            if r.get("rule_id") == reference_rule_id:
                sg_id = r.get("security_group_id")
                proto = r.get("protocol")
                port = r.get("port")
                break
        if sg_id is None:
            payload = {"error": f"No security group rule '{reference_rule_id}'"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        # is the subnet group present?
        ok = False
        for g in data.get("aws_subnet_groups", []):
            if g.get("subnet_group_id") == subnet_group_id:
                ok = True
                break
        if not ok:
            payload = {"error": f"No subnet group '{subnet_group_id}'"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        plan = {
            "plan_id": _next_aws_plan_id(data),
            "type": "cluster",
            "cluster_id": cluster_id,
            "security_group_id": sg_id,
            "subnet_group_id": subnet_group_id,
            "new_status": str(new_status),
            "new_name": str(new_name),
            "note": str(note),
            "env_tag": str(env_tag),
            "consolidate_cidr": str(consolidate_cidr),
            "consolidate_desc": str(consolidate_desc),
            "endpoint_url": str(endpoint_url),
            "steps": [
                "attach_sg",
                "set_subnet",
                "set_status",
                "set_name",
                "set_note",
                "standardize_env_on_sg",
                "consolidate_redis_on_sg",
                "set_endpoint",
            ],
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
                "name": "CreateClusterChangePlan",
                "description": "Create a cluster hardening plan using a reference rule to derive SG.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cluster_id": {"type": "string"},
                        "reference_rule_id": {"type": "string"},
                        "subnet_group_id": {"type": "string"},
                        "new_status": {"type": "string"},
                        "new_name": {"type": "string"},
                        "note": {"type": "string"},
                        "env_tag": {"type": "string"},
                        "consolidate_cidr": {"type": "string"},
                        "consolidate_desc": {"type": "string"},
                        "endpoint_url": {"type": "string"},
                    },
                    "required": [
                        "cluster_id",
                        "reference_rule_id",
                        "subnet_group_id",
                        "new_status",
                        "new_name",
                        "note",
                        "env_tag",
                        "consolidate_cidr",
                        "consolidate_desc",
                        "endpoint_url",
                    ],
                },
            },
        }
