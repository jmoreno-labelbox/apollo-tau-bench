# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetJobPosting(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        job_id = kwargs.get("job_id")
        postings = data.get("job_postings", [])
        for post in postings:
            if post.get("job_id") == job_id:
                return str(post)
        return f"Job posting with ID {job_id} not found."

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_job_posting",
                "description": "Retrieve details of a specific job posting by job ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "job_id": {
                            "type": "string",
                            "description": "The job ID to retrieve.",
                        }
                    },
                    "required": ["job_id"],
                },
            },
        }
