from tau_bench.envs.tool import Tool
import json
from typing import Any

class get_departments(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], departments: list = None) -> str:
        if departments is None:
            departments = []
        payload = departments
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getDepartments",
                "description": "Return a list of all departments.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
