# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_position(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], position_id: str) -> str:
        positions = data.get("positions", [])
        for p in positions:
            if p["position_id"] == position_id:
                return json.dumps(p, indent=2)
        return json.dumps({"error": f"position_id {position_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_position",
                "description": "Return the position record for the given position_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "position_id": {
                            "type": "string",
                            "description": "Unique ID of the position to fetch",
                        }
                    },
                    "required": ["position_id"],
                    "additionalProperties": False,
                },
            },
        }
