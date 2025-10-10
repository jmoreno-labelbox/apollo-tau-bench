# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListCanonicalCreativeTypes(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        for r in data.get("policy_params", []):
            if r.get("param_name") == "canonical_creative_types":
                return json.dumps(_as_list_literal(r.get("param_value", "[]")))
        return json.dumps([])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "list_canonical_creative_types",
                                                 "description": "Lists allowed creative types from policy.",
                                                 "parameters": {"type": "object", "properties": {}, "required": []}}}
