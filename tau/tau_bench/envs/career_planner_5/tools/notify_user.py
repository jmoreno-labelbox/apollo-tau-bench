# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class notify_user(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, message: str) -> str:
        data.setdefault("user_notifications", []).append(
            {"user_id": user_id, "message": message}
        )
        return json.dumps({"notified_user": user_id})

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "notify_user",
                "description": "Push a notification message to an individual user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "message": {"type": "string"},
                    },
                    "required": ["user_id", "message"],
                },
            },
        }
