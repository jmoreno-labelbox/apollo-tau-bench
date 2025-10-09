from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class ListUserApplications(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        applications = [
            app
            for app in data.get("job_applications", [])
            if app.get("user_id") == user_id
        ]
        payload = {"applications": applications}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "listUserApplications",
                "description": "List all job applications for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
