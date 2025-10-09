from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class GenerateUniqueGoalId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, prefix: str) -> str:
        unique_id = f"{prefix}-001"
        payload = {"generated_goal_id": unique_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "generateUniqueGoalId",
                "description": "Generate a unique goal ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "prefix": {"type": "string"},
                    },
                    "required": ["user_id", "prefix"],
                },
            },
        }
