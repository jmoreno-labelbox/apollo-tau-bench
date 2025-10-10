# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReturnScalar(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], value: str) -> str:
        return str(value)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "return_scalar", "description": "Returns the provided scalar value as-is.", "parameters": {"type": "object", "properties": {"value": {"type": "string"}}, "required": ["value"]}}}
