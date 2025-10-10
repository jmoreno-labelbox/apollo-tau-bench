# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class InsightLev(Tool):
    @staticmethod
        # primary execution function
    def invoke(data: Dict[str, Any], leverage_threshold) -> str:
        threshold = leverage_threshold
        # return outcome
        return json.dumps({"filtered": True, "filtered_table": "flags_leverage", "leverage_threshold": threshold}, indent=2)

    @staticmethod
        # information metadata
    def get_info() -> Dict[str, Any]:
        # output result
        return {"type": "function", "function": {"name": "levCut", "description": "Selects insights by leverage threshold.", "parameters": {"type": "object", "properties": {"leverage_threshold": {"type": "number"}}, "required": ["leverage_threshold"]}}}
