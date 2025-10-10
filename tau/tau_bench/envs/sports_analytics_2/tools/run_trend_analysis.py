# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RunTrendAnalysis(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        time_windows = kwargs.get("time_windows", [])
        min_sample_size = kwargs.get("min_sample_size", 25)
        return json.dumps({"trend_analysis": f"trends_min_{min_sample_size}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "run_trend_analysis", "description": "Analyzes performance trends across multiple time windows.", "parameters": {"type": "object", "properties": {"time_windows": {"type": "array", "items": {"type": "integer"}}, "min_sample_size": {"type": "integer"}}, "required": ["time_windows"]}}}
