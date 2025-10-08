from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class ListApplications(Tool):
    @staticmethod
    def invoke(
        data,
        job_applications: list = None,
        candidate_id: str = None
    ) -> str:
        apps = [
            app
            for app in (job_applications or [])
            if app.get("candidate_id") == candidate_id
        ]
        payload = {"applications": apps}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "listApplications",
                "description": "List all job applications for a given candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {"candidate_id": {"type": "string"}},
                    "required": ["candidate_id"],
                },
            },
        }
