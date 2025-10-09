from tau_bench.envs.tool import Tool
import json
from typing import Any

class add_position(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], position_id: str = None,
    position: Any = None,
    ) -> str:
        positions = data.setdefault("positions", [])
        position = {"position_id": position_id}
        data["positions"][position_id] = position
        payload = {"success": True, "position_id": position.get("position_id")}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddPosition",
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
