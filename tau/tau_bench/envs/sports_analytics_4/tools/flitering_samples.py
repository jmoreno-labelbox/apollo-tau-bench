# Sierra copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FliteringSamples(Tool):
    @staticmethod
        # primary execution method
    def invoke(data: Dict[str, Any], min_sample_size = 25, source_table = "") -> str:
        # return outcome
        return json.dumps({"filtered_insights": "flags_filtered_sample"}, indent=2)

    @staticmethod
        # metadata information
    def get_info() -> Dict[str, Any]:
        # return outcome
        return {"type": "function", "function": {"name": "sizes", "description": "Selects insights by minimum sample size.", "parameters": {"type": "object", "properties": {"min_sample_size": {"type": "integer"}, "source_table": {"type": "string"}}, "required": ["min_sample_size"]}}}
