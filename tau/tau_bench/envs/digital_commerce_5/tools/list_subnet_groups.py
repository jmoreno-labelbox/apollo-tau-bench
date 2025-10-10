# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListSubnetGroups(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        groups = data.get("aws_subnet_groups", [])
        return json.dumps({"subnet_groups": groups}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_subnet_groups",
                "description": "List all ElastiCache subnet groups.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
