# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_job_by_title(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], job_title: str = "", keywords: str = "") -> str:
        jobs = data.get("job_postings", [])

        search_term = job_title or keywords
        if not search_term:
            return json.dumps(
                {"error": "Either job_title or keywords must be provided"}, indent=2
            )

        # Attempt an exact match initially.
        job = next(
            (j for j in jobs if j.get("title", "").lower() == search_term.lower()), None
        )

        # If an exact match is unavailable, attempt a partial match.
        if not job:
            job = next(
                (j for j in jobs if search_term.lower() in j.get("title", "").lower()),
                None,
            )

        # If there is still no match, attempt to match keywords from the job title.
        if not job and keywords:
            keyword_list = keywords.lower().split()
            job = next(
                (
                    j
                    for j in jobs
                    if any(
                        keyword in j.get("title", "").lower()
                        for keyword in keyword_list
                    )
                ),
                None,
            )

        if job:
            return json.dumps(
                {
                    "job_found": True,
                    "job_id": job.get("job_id"),
                    "job_title": job.get("title"),
                    "department": job.get("department"),
                    "location": job.get("location"),
                    "experience_level": job.get("experience_level"),
                },
                indent=2,
            )
        else:
            return json.dumps(
                {
                    "job_found": False,
                    "error": f"Job with title/keywords '{search_term}' not found",
                    "suggestion": "Try using different keywords or check job postings",
                },
                indent=2,
            )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_job_by_title",
                "description": "Find job ID by job title or keywords (exact or partial match)",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "job_title": {
                            "type": "string",
                            "description": "Full or partial job title to search for",
                        },
                        "keywords": {
                            "type": "string",
                            "description": "Keywords to search in job titles (space-separated)",
                        },
                    },
                    "required": [],
                },
            },
        }
