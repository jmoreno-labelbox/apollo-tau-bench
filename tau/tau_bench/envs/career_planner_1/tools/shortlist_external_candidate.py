from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class ShortlistExternalCandidate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], candidate_id: str = None, job_id: str = None, recruiter_id: str = None) -> str:
        # Assign a recruiter in a deterministic manner if not specified
        if not recruiter_id:
            if job_id in ["J001", "J002"]:
                recruiter_id = "U301"
            elif job_id in ["J003", "J004"]:
                recruiter_id = "U304"
            else:
                recruiter_id = "U312"

        # Generate a shortlist entry containing only necessary data
        entry = {
            "candidate_id": candidate_id,
            "recruiter_id": recruiter_id,
            "job_id": job_id,
            "timestamp": datetime.now().isoformat(),
        }

        if "shortlisted_candidates" not in data:
            data["shortlisted_candidates"] = []
        data["shortlisted_candidates"].append(entry)
        return f"External candidate {candidate_id} shortlisted for job {job_id}."
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ShortlistExternalCandidate",
                "description": "Add external candidate to shortlist for a given job. Recruiter is assigned deterministically based on job_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {
                            "type": "string",
                            "description": "ID of the external candidate",
                        },
                        "job_id": {
                            "type": "string",
                            "description": "ID of the job posting",
                        },
                    },
                    "required": ["candidate_id", "job_id"],
                },
            },
        }
