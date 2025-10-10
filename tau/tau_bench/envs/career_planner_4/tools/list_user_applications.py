# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class list_user_applications(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str) -> str:
        applications = [
            app
            for app in data.get("job_applications", [])
            if app.get("user_id") == user_id
        ]
        return json.dumps({"applications": applications}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "list_user_applications",
                "description": "List all job applications for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
