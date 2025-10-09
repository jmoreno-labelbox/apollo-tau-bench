from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetPolicyParam(Tool):
    """Fetches the value of a policy parameter."""

    @staticmethod
    def invoke(data: dict[str, Any], param_name: str = None) -> str:
        policy_params = data.get("policy_params", [])

        for param in policy_params:
            if param.get("param_name") == param_name:
                payload = {"param_value": param.get("param_value")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Policy parameter '{param_name}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPolicyParam",
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
