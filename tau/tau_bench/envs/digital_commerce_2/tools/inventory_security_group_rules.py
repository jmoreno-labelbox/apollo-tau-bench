# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class InventorySecurityGroupRules(Tool):
    """Return a compact inventory of all security group rule IDs."""

    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        rules = list(data.get("aws_security_group_rules", {}).values())
        return json.dumps({"rule_ids": [r.get("rule_id") for r in rules]}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "inventory_security_group_rules",
                "description": "List all AWS security group rule IDs.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
