from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetJobPosting(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], job_id: str = None) -> str:
        postings = data.get("job_postings", {}).values()
        for post in postings.values():
            if post.get("job_id") == job_id:
                return str(post)
        return f"Job posting with ID {job_id} not found."
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetJobPosting",
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
