# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTrends(Tool):
    @staticmethod
        # primary execution method
    def invoke(data: Dict[str, Any], min_sample_size = 25, time_windows = []) -> str:
        # return output
        return json.dumps({"trend_analysis": f"trends_min_{min_sample_size}"}, indent=2)

    @staticmethod
        # metadata information
    def get_info() -> Dict[str, Any]:
        # return output
        return {"type": "function", "function": {"name": "findTrends", "description": "Examines performance trends across multiple time windows.", "parameters": {"type": "object", "properties": {"time_windows": {"type": "array", "items": {"type": "integer"}}, "min_sample_size": {"type": "integer"}}, "required": ["time_windows"]}}}
