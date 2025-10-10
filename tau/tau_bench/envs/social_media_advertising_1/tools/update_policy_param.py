# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdatePolicyParam(Tool):
    """Updates a policy parameter value."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        param_name = kwargs.get("param_name")
        param_value = kwargs.get("param_value")
        updated_at = kwargs.get("updated_at")
        
        policy_params = data.get("policy_params", [])
        for param in policy_params:
            if param.get("param_name") == param_name:
                old_value = param['param_value']
                param['param_value'] = param_value
                param['updated_at'] = updated_at
                return json.dumps({
                    "status": "success",
                    "message": f"Policy parameter '{param_name}' updated from '{old_value}' to '{param_value}'"
                })

        return json.dumps({"error": f"Policy parameter '{param_name}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_policy_param",
                "description": "Updates a policy parameter value.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "param_name": {"type": "string"},
                        "param_value": {"type": "string"},
                        "updated_at": {"type": "string"}
                    },
                    "required": ["param_name", "param_value", "updated_at"]
                }
            }
        }
