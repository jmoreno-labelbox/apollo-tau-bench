from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetJobPosting(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], job_id: str) -> str:
        job_postings = data.get("job_postings", [])
        job = next((j for j in job_postings if j.get("job_id") == job_id), None)
        return (
            json.dumps(job, indent=2)
            if job
            else json.dumps({"error": "Job posting not found"}, indent=2)
        )
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "getJobPosting",
                "description": "Get job posting details by job ID",
                "parameters": {
                    "type": "object",
                    "properties": {"job_id": {"type": "string"}},
                    "required": ["job_id"],
                },
            },
        }
