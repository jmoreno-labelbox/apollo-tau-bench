# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPolicyParameter(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], param_name) -> str:
        n = param_name
        for r in list(data.get("policy_params", {}).values()):
            if r.get("param_name") == n:
                return json.dumps(r)
        return json.dumps({"error": f"policy {n} not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_policy_parameter", "description": "Gets a single policy parameter.",
                             "parameters": {"type": "object", "properties": {"param_name": {"type": "string"}},
                                            "required": ["param_name"]}}}
