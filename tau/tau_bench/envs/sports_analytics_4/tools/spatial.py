# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class Spatial(Tool):
    @staticmethod
        # primary execution function
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # return output
        return json.dumps({"grid": "12x12_catcher_view"}, indent=2)

    @staticmethod
        # metadata information
    def get_info() -> Dict[str, Any]:
        # return output
        return {"type": "function", "function": {"name": "norming", "description": "Standardizes spatial pitch/location data.", "parameters": {"type": "object", "properties": {"source_table": {"type": "string"}}}, "required": []}}
