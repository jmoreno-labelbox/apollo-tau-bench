# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateSubnetGroupDescription(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], subnet_group_id: Any, name: Any, description: Any) -> str:
        subnet_group_id = _as_id(subnet_group_id)
        groups = data.get("aws_subnet_groups", [])
        g = next((x for x in groups if _as_id(x.get("subnet_group_id")) == subnet_group_id), None)
        if not g:
            return _err("Subnet group not found.")
        g["name"] = str(name)
        g["description"] = str(description)
        return json.dumps(
            {
                "subnet_group_id": subnet_group_id,
                "name": g["name"],
                "description": g["description"],
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_subnet_group_description",
                "description": "Rename a subnet group and update its description.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subnet_group_id": {"type": "string"},
                        "name": {"type": "string"},
                        "description": {"type": "string"},
                    },
                    "required": ["subnet_group_id", "name", "description"],
                },
            },
        }
