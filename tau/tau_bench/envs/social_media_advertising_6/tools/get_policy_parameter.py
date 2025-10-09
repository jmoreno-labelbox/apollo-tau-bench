from tau_bench.envs.tool import Tool
import copy
import json
from typing import Any

class GetPolicyParameter(Tool):
    """Provide a policy parameter by name (exact match on 'param_name')."""

    @staticmethod
    def invoke(data: dict[str, Any], param_name: str) -> str:
        err = _require({"param_name": param_name}, ["param_name"])
        if err:
            return _fail(err)
        tbl = _assert_table(data, "policy_params")
        for r in tbl:
            if r.get("param_name") == param_name:
                payload = {
                    "param_name": r.get("param_name"),
                    "param_value": r.get("param_value"),
                }
                out = json.dumps(payload)
                return out
        return _fail("param_not_found")
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPolicyParameter",
                "description": "Get a value from policy_params by name.",
                "parameters": {
                    "type": "object",
                    "properties": {"param_name": {"type": "string"}},
                    "required": ["param_name"],
                },
            },
        }
