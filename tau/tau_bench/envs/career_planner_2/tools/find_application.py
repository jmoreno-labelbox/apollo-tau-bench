# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindApplication(Tool):
    """Find a job application ID by user ID and job ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("user_id")
        jid = kwargs.get("job_id")
        for a in data.get("job_applications", []):
            if a.get("applicant_id") == uid and a.get("job_id") == jid:
                return json.dumps({"application_id": a.get("application_id")})
        return json.dumps({"error": "Application not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_application",
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
