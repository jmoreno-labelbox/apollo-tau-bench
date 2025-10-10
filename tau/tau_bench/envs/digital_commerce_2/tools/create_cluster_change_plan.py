# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateClusterChangePlan(Tool):
    name = "create_cluster_change_plan"
    description = "Create a deterministic cluster change plan ap-0001 for a given cluster."

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        cluster_id: Any,
        reference_rule_id: Any,
        subnet_group_id: Any,
        new_status: Any,
        new_name: Any,
        note: Any,
        env_tag: Any = None,
        consolidate_cidr: Any = None,
        consolidate_desc: Any = None,
        endpoint_url: Any = None,
    ) -> str:
        clusters = data.get("aws_clusters", {})
        cluster = clusters.get(cluster_id)
        if not cluster:
            return {"error": f"Unknown cluster_id '{cluster_id}'"}
        plan = {
            "plan_id": "ap-0001",
            "type": "cluster",
            "cluster_id": cluster_id,
            "reference_rule_id": reference_rule_id,
            "subnet_group_id": subnet_group_id,
            "new_status": new_status,
            "new_name": new_name,
            "note": note,
            "env_tag": env_tag,
            "consolidate_cidr": consolidate_cidr,
            "consolidate_desc": consolidate_desc,
            "endpoint_url": endpoint_url,
            "steps": [
                "attach_sg",
                "attach_subnet_group",
                "set_status",
                "set_name",
                "set_note",
                "consolidate_ingress",
                "standardize_env_on_sg",
                "set_endpoint",
            ],
        }
        cluster["_pending_cluster_plan"] = plan
        data["_last_cluster_plan_cluster_id"] = cluster_id
        data["_last_cluster_plan_id"] = "ap-0001"
        return {"plan_id": "ap-0001"}

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_cluster_change_plan",
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
                        "consolidate_cidr",
                        "consolidate_desc",
                        "endpoint_url",
                    ],
                },
            },
        }
