# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FilterInsightsBySampleSize(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], min_sample_size = 25, source_table = "") -> str:
        return json.dumps({"filtered_insights": "flags_filtered_sample"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "filter_insights_by_sample_size", "description": "Filters insights by minimum sample size.", "parameters": {"type": "object", "properties": {"min_sample_size": {"type": "integer"}, "source_table": {"type": "string"}}, "required": ["min_sample_size"]}}}
