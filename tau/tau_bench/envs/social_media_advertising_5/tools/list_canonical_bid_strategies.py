# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _as_list_literal(v: str) -> List[str]:
    try:
        x = ast.literal_eval(v)
        return list(x) if isinstance(x, (list, tuple)) else []
    except Exception:
        return []

class ListCanonicalBidStrategies(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        for r in list(data.get("policy_params", {}).values()):
            if r.get("param_name") == "canonical_bid_strategies":
                return json.dumps(_as_list_literal(r.get("param_value", "[]")))
        return json.dumps([])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "list_canonical_bid_strategies",
                                                 "description": "Lists allowed bid strategies from policy.",
                                                 "parameters": {"type": "object", "properties": {}, "required": []}}}