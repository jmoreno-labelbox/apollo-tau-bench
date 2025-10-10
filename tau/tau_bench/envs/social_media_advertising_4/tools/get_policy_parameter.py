# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPolicyParameter(Tool):
    """Retrieves the value of a specific business rule."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        param_name = kwargs.get("param_name")
        for param in data.get('policy_params', []):
            if param.get('param_name') == param_name:
                return json.dumps(param)
        return json.dumps({"error": f"Policy parameter '{param_name}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_policy_parameter", "description": "Retrieves the value of a specific business rule, like 'max_bid_amount'.", "parameters": {"type": "object", "properties": {"param_name": {"type": "string", "description": "The name of the policy parameter to retrieve."}}, "required": ["param_name"]}}}
