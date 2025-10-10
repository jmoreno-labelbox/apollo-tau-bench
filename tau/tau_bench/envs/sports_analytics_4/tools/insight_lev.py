# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class InsightLev(Tool):
    @staticmethod
        # main invoke function
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        threshold = kwargs.get("leverage_threshold")
        # return result
        return json.dumps({"filtered": True, "filtered_table": "flags_leverage", "leverage_threshold": threshold}, indent=2)

    @staticmethod
        # info metadata
    def get_info() -> Dict[str, Any]:
        # return result
        return {"type": "function", "function": {"name": "levCut", "description": "Selects insights by leverage threshold.", "parameters": {"type": "object", "properties": {"leverage_threshold": {"type": "number"}}, "required": ["leverage_threshold"]}}}
