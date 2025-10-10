# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetJobIdByTitle(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], job_title: str) -> str:
        postings = data.get("job_postings", [])
        # Use a case-insensitive partial match for robustness
        posting = next(
            (p for p in postings if job_title.lower() in p.get("title", "").lower()),
            None,
        )
        if posting:
            return json.dumps({"job_id": posting["job_id"]}, indent=2)
        return json.dumps(
            {"error": f"Job posting with title containing '{job_title}' not found"},
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_job_id_by_title",
                "description": "Find a job ID by its title.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "job_title": {
                            "type": "string",
                            "description": "The title of the job to find.",
                        }
                    },
                    "required": ["job_title"],
                },
            },
        }
