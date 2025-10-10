# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class Spatial(Tool):
    @staticmethod
        # main invoke function
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # return result
        return json.dumps({"grid": "12x12_catcher_view"}, indent=2)

    @staticmethod
        # info metadata
    def get_info() -> Dict[str, Any]:
        # return result
        return {"type": "function", "function": {"name": "norming", "description": "Standardizes spatial pitch/location data.", "parameters": {"type": "object", "properties": {"source_table": {"type": "string"}}}, "required": []}}
