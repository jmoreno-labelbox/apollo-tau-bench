from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetJobByTitle(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], job_title: str = "", keywords: str = "") -> str:
        _keywordsL = keywords or ''.lower()
        pass
        jobs = data.get("job_postings", {}).values()

        search_term = job_title or keywords
        if not search_term:
            payload = {"error": "Either job_title or keywords must be provided"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        # Attempt an exact match initially
        job = next(
            (j for j in jobs.values() if j.get("title", "").lower() == search_term.lower()), None
        )

        # If an exact match is not found, attempt a partial match
        if not job:
            job = next(
                (j for j in jobs.values() if search_term.lower() in j.get("title", "").lower()),
                None,
            )

        # If no match is found, attempt to match keywords in the job title
        if not job and keywords:
            keyword_list = keywords.lower().split()
            job = next(
                (
                    j
                    for j in jobs.values() if any(
                        keyword in j.get("title", "").lower()
                        for keyword in keyword_list
                    )
                ),
                None,
            )

        if job:
            payload = {
                "job_found": True,
                "job_id": job.get("job_id"),
                "job_title": job.get("title"),
                "department": job.get("department"),
                "location": job.get("location"),
                "experience_level": job.get("experience_level"),
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = {
                "job_found": False,
                "error": f"Job with title/keywords '{search_term}' not found",
                "suggestion": "Try using different keywords or check job postings",
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getJobByTitle",
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
