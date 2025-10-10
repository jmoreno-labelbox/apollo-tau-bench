# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class search_job_postings(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], filters: dict) -> str:
        job_postings = data.get("job_postings", [])
        if "job_id" in filters:
            job = next(
                (j for j in job_postings if j.get("job_id") == filters["job_id"]), None
            )
            return (
                json.dumps(job, indent=2)
                if job
                else json.dumps({"error": "Job not found"}, indent=2)
            )
        return json.dumps({"job_postings": job_postings}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "search_job_postings",
                "description": "Search for job postings by filters",
                "parameters": {
                    "type": "object",
                    "properties": {"filters": {"type": "object"}},
                    "required": ["filters"],
                },
            },
        }
