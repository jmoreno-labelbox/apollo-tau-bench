from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class UpdatePolicyParam(Tool):
    """Modifies the value of a policy parameter."""

    @staticmethod
    def invoke(data: dict[str, Any], param_name: str = None, param_value: Any = None, updated_at: str = None) -> str:
        policy_params = data.get("policy_params", [])
        for param in policy_params:
            if param.get("param_name") == param_name:
                old_value = param["param_value"]
                param["param_value"] = param_value
                param["updated_at"] = updated_at
                payload = {
                    "status": "success",
                    "message": f"Policy parameter '{param_name}' updated from '{old_value}' to '{param_value}'",
                }
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
                "name": "UpdatePolicyParam",
                "description": "Updates a policy parameter value.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "param_name": {"type": "string"},
                        "param_value": {"type": "string"},
                        "updated_at": {"type": "string"},
                    },
                    "required": ["param_name", "param_value", "updated_at"],
                },
            },
        }
