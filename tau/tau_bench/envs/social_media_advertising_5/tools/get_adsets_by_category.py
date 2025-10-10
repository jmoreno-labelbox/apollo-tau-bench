# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAdsetsByCategory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        c = kwargs.get("category")
        rows = [r for r in list(data.get("adsets", {}).values()) if r.get("category") == c]
        return json.dumps({"adsets": rows})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_adsets_by_category", "description": "Lists ad sets by category.",
                             "parameters": {"type": "object", "properties": {"category": {"type": "string"}},
                                            "required": ["category"]}}}
