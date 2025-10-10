# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAdsetsByCategory(Tool):
    """Finds ad sets targeting a specific product category."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        category = kwargs.get("category")
        adsets = [adset for adset in data.get('adsets', []) if adset.get('category') == category]
        return json.dumps({"adsets": adsets})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_adsets_by_category", "description": "Retrieves a list of ad sets that are targeting a specific product category.", "parameters": {"type": "object", "properties": {"category": {"type": "string"}}, "required": ["category"]}}}
