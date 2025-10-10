# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class generate_unique_goal_id(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, prefix: str) -> str:
        unique_id = f"{prefix}-001"
        return json.dumps({"generated_goal_id": unique_id}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "generate_unique_goal_id",
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
