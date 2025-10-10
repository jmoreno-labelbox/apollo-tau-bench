# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPolicyParameter(Tool):
    """Return a policy parameter by name (exact match on 'param_name')."""

    @staticmethod
    def invoke(data: Dict[str, Any], param_name) -> str:
        err = _require(kwargs, ["param_name"])
        if err: return _fail(err)
        tbl = _assert_table(data, "policy_params")
        for r in tbl:
            if r.get("param_name") == param_name:
                return json.dumps({"param_name": r.get("param_name"), "param_value": r.get("param_value")})
        return _fail("param_not_found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_policy_parameter", "description": "Get a value from policy_params by name.",
                             "parameters": {"type": "object", "properties": {"param_name": {"type": "string"}},
                                            "required": ["param_name"]}}}
