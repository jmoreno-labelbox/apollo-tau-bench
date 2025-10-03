from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any

class ListCanonicalCreativeTypes(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        for r in data.get("policy_params", []):
            if r.get("param_name") == "canonical_creative_types":
                payload = _as_list_literal(r.get("param_value", "[]"))
                out = json.dumps(payload)
                return out
        payload = []
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListCanonicalCreativeTypes",
                "description": "Lists allowed creative types from policy.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
