# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_positions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], department_id: str = None) -> str:
        positions = list(data.get("positions", {}).values())
        filtered = [
            p
            for p in positions
            if (not department_id or p.get("department_id") == department_id)
        ]
        return json.dumps(filtered, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_positions",
                "description": "Return a list of all positions, optionally filtered by department_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department_id": {
                            "type": "string",
                            "description": "Department ID to filter positions",
                        }
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
