# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPolicyParam(Tool):
    """Retrieves a policy parameter value."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        param_name = kwargs.get("param_name")
        policy_params = list(data.get("policy_params", {}).values())
        
        for param in policy_params:
            if param.get("param_name") == param_name:
                return json.dumps({"param_value": param.get("param_value")})
        
        return json.dumps({"error": f"Policy parameter '{param_name}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_policy_param",
                "description": "Retrieves a policy parameter value.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "param_name": {
                            "type": "string",
                            "description": "The name of the policy parameter.",
                        }
                    },
                    "required": ["param_name"],
                },
            },
        }
