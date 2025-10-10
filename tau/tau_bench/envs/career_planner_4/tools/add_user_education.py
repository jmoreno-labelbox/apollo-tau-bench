# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class add_user_education(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, education: dict) -> str:
        education["user_id"] = user_id
        data.setdefault("user_education", []).append(education)
        return json.dumps(
            {"success": f"Education record added for user {user_id}"}, indent=2
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "add_user_education",
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
