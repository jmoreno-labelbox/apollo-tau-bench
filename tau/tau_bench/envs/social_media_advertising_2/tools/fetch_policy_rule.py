# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchPolicyRule(Tool):
    """Look up a business rule parameter by name (supports policy_params and policy_rules)."""

    @staticmethod
    def invoke(data: Dict[str, Any], rule_name) -> str:
        target = rule_name
        sources = []
        if isinstance(data.get("policy_params"), list):
            sources.extend(data["policy_params"])
        if isinstance(data.get("policy_rules"), list):
            sources.extend(data["policy_rules"])

        for row in sources:
            key = row.get("param_name")
            if key == target:
                val = (
                    row.get("value")
                    if "value" in row
                    else row.get("param_value", None)
                )
                return json.dumps({"name": key, "value": val})
        return json.dumps({"error": f"Policy rule {target} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_policy_rule",
                "description": "Look up a business rule parameter by name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rule_name": {"type": "string"},
                    },
                    "required": ["rule_name"],
                },
            },
        }
