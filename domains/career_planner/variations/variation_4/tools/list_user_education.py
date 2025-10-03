from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class ListUserEducation(Tool):
    @staticmethod
    def invoke(data, user_id: str) -> str:
        edu = [e for e in data.get("user_education", []) if e.get("user_id") == user_id]
        payload = {"education": edu}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "listUserEducation",
                "description": "List all education records for a specific user.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
