# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetJobApplication(Tool):
    """Fetch a job application record by ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        aid = kwargs.get("application_id")
        for a in data.get("job_applications", []):
            if a.get("application_id") == aid:
                return json.dumps(a, indent=2)
        return json.dumps({"error": "Application not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_job_application",
                "description": "Get job application.",
                "parameters": {
                    "type": "object",
                    "properties": {"application_id": {"type": "string"}},
                    "required": ["application_id"],
                },
            },
        }
