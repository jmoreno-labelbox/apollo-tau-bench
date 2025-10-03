from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class AddUserEducation(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, education: dict) -> str:
        education["user_id"] = user_id
        data.setdefault("user_education", []).append(education)
        payload = {"success": f"Education record added for user {user_id}"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "addUserEducation",
                "description": "Add education record for a user",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "education": {"type": "object"},
                    },
                    "required": ["user_id", "education"],
                },
            },
        }
