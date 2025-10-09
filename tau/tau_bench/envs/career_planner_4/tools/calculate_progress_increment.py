from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class CalculateProgressIncrement(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], current_progress: Any, increment: int) -> str:
        if current_progress == "get_from_goal":
            # This will be calculated dynamically according to the goal
            calculated_value = min(100, increment)  # Streamlined
        else:
            calculated_value = min(100, current_progress + increment)
        payload = {"calculated_value": calculated_value}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "calculateProgressIncrement",
                "description": "Calculate progress increment automatically",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "current_progress": {"type": ["integer", "string"]},
                        "increment": {"type": "integer"},
                    },
                    "required": ["current_progress", "increment"],
                },
            },
        }
