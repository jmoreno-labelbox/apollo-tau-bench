# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class list_user_education(Tool):
    @staticmethod
    def invoke(data, user_id: str) -> str:
        edu = [e for e in data.get("user_education", []) if e.get("user_id") == user_id]
        return json.dumps({"education": edu}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_user_education",
                "description": "List all education records for a specific user.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
