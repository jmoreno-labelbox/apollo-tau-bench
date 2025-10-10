# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_departments(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        departments = list(data.get("departments", {}).values())
        return json.dumps(departments, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_departments",
                "description": "Return a list of all departments.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
