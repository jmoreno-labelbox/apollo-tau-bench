# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindJobByTitle(Tool):
    """Find a job posting's ID by its title."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        title = kwargs.get("title")
        for j in data.get("job_postings", []):
            if j.get("title").lower() == title.lower():
                return json.dumps({"job_id": j.get("job_id")})
        return json.dumps({"error": "Job not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_job_by_title",
                "description": "Find a job posting's ID by its title.",
                "parameters": {
                    "type": "object",
                    "properties": {"title": {"type": "string"}},
                    "required": ["title"],
                },
            },
        }
