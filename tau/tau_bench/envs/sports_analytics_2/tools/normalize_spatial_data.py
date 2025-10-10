# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class NormalizeSpatialData(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return json.dumps({"grid": "12x12_catcher_view"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "normalize_spatial_data", "description": "Normalizes spatial pitch/location data.", "parameters": {"type": "object", "properties": {"source_table": {"type": "string"}}}, "required": []}}
