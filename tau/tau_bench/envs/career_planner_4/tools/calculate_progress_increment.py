# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class calculate_progress_increment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], current_progress: Any, increment: int) -> str:
        if current_progress == "get_from_goal":
            # This will be calculated dynamically according to the objective.
            calculated_value = min(100, increment)  # Streamlined
        else:
            calculated_value = min(100, current_progress + increment)

        return json.dumps({"calculated_value": calculated_value}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "calculate_progress_increment",
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
