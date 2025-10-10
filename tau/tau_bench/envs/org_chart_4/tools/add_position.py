# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class add_position(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], position: dict) -> str:
        positions = data.setdefault("positions", [])
        positions.append(position)
        return json.dumps(
            {"success": True, "position_id": position.get("position_id")}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_position",
                "description": "Add a new position record. The position object must contain all required fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "position": {
                            "type": "object",
                            "description": "Position record to add",
                        }
                    },
                    "required": ["position"],
                    "additionalProperties": False,
                },
            },
        }
