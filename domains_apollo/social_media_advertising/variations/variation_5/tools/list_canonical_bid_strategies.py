from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any

class ListCanonicalBidStrategies(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        for r in data.get("policy_params", []):
            if r.get("param_name") == "canonical_bid_strategies":
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
                "name": "ListCanonicalBidStrategies",
                "description": "Lists allowed bid strategies from policy.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
