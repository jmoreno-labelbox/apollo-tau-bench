# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FliteringSamples(Tool):
    @staticmethod
        # main invoke function
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        min_sample_size = kwargs.get("min_sample_size", 25)
        source_table = kwargs.get("source_table", "")
        # return result
        return json.dumps({"filtered_insights": "flags_filtered_sample"}, indent=2)

    @staticmethod
        # info metadata
    def get_info() -> Dict[str, Any]:
        # return result
        return {"type": "function", "function": {"name": "sizes", "description": "Selects insights by minimum sample size.", "parameters": {"type": "object", "properties": {"min_sample_size": {"type": "integer"}, "source_table": {"type": "string"}}, "required": ["min_sample_size"]}}}
