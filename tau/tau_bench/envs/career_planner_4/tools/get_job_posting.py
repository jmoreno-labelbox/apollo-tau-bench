# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_job_posting(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], job_id: str) -> str:
        job_postings = data.get("job_postings", [])
        job = next((j for j in job_postings if j.get("job_id") == job_id), None)
        return (
            json.dumps(job, indent=2)
            if job
            else json.dumps({"error": "Job posting not found"}, indent=2)
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_job_posting",
                "description": "Get job posting details by job ID",
                "parameters": {
                    "type": "object",
                    "properties": {"job_id": {"type": "string"}},
                    "required": ["job_id"],
                },
            },
        }
