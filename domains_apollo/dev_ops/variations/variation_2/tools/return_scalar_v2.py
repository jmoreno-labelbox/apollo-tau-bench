from tau_bench.envs.tool import Tool
import json
from typing import Any

class ReturnScalarV2(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], value: str) -> str:
        pass
        return str(value)

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReturnScalarV2",
                "description": "Returns the provided scalar value as-is.",
                "parameters": {
                    "type": "object",
                    "properties": {"value": {"type": "string"}},
                    "required": ["value"],
                },
            },
        }
