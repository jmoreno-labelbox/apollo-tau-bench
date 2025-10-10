# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CaptureLocContext(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], keys: List[str]) -> str:
        context = {k: f"artifact://context/{k}" for k in keys}
        return json.dumps({"context_uris": context}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "capture_loc_context", "description": "Returns deterministic context media URIs per string key.", "parameters": {"type": "object", "properties": {"keys": {"type": "array", "items": {"type": "string"}}}, "required": ["keys"]}}}
