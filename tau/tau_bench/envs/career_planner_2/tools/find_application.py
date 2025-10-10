from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class FindApplication(Tool):
    """Locate a job application ID using the user ID and job ID."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, job_id: str = None) -> str:
        for a in data.get("job_applications", {}).values():
            if a.get("applicant_id") == user_id and a.get("job_id") == job_id:
                payload = {"application_id": a.get("application_id")}
                out = json.dumps(payload)
                return out
        payload = {"error": "Application not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindApplication",
                "description": "Find a job application ID by user and job ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "job_id": {"type": "string"},
                    },
                    "required": ["user_id", "job_id"],
                },
            },
        }
