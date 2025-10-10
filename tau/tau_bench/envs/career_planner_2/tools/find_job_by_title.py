from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class FindJobByTitle(Tool):
    """Determine a job posting's ID using its title."""

    @staticmethod
    def invoke(data: dict[str, Any], title: str = None) -> str:
        for j in data.get("job_postings", {}).values():
            if j.get("title").lower() == title.lower():
                payload = {"job_id": j.get("job_id")}
                out = json.dumps(payload)
                return out
        payload = {"error": "Job not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindJobByTitle",
                "description": "Find a job posting's ID by its title.",
                "parameters": {
                    "type": "object",
                    "properties": {"title": {"type": "string"}},
                    "required": ["title"],
                },
            },
        }
