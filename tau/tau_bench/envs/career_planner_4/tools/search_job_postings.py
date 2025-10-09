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

class SearchJobPostings(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        filters: Any = None,
        job_id: str = None
    ) -> str:
        job_postings = data.get("job_postings", {}).values()
        if job_id is not None:
            job = next(
                (j for j in job_postings.values() if j.get("job_id") == job_id), None
            )
            return (
                json.dumps(job, indent=2)
                if job
                else json.dumps({"error": "Job not found"}, indent=2)
            )
        payload = {"job_postings": job_postings}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "searchJobPostings",
                "description": "Search for job postings by filters",
                "parameters": {
                    "type": "object",
                    "properties": {"filters": {"type": "object"}},
                    "required": ["filters"],
                },
            },
        }
