# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateSubnetGroupDescription(Tool):
    """Replace the description on a subnet group."""

    @staticmethod
    def invoke(data: Dict[str, Any], subnet_group_id: Any, new_description: Any) -> str:
        subnet_group_id = _idstr(subnet_group_id)
        groups = data.get("aws_subnet_groups", [])
        for g in groups:
            if g.get("subnet_group_id") == subnet_group_id:
                g["description"] = new_description
                return json.dumps(g, indent=2)
        return json.dumps({"error": f"No subnet group found with ID '{subnet_group_id}'"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_subnet_group_description",
                "description": "Set the description field on an AWS subnet group record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subnet_group_id": {"type": "string"},
                        "new_description": {"type": "string"},
                    },
                    "required": ["subnet_group_id", "new_description"],
                },
            },
        }
