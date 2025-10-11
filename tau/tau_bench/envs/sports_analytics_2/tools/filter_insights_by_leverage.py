# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FilterInsightsByLeverage(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], leverage_threshold) -> str:
        threshold = leverage_threshold
        return json.dumps({"filtered": True, "filtered_table": "flags_leverage", "leverage_threshold": threshold}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "filter_insights_by_leverage", "description": "Filters insights by leverage threshold.", "parameters": {"type": "object", "properties": {"leverage_threshold": {"type": "number"}}, "required": ["leverage_threshold"]}}}
