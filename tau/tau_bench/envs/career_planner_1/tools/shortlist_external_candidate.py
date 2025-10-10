# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ShortlistExternalCandidate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        candidate_id = kwargs.get("candidate_id")
        job_id = kwargs.get("job_id")
        recruiter_id = kwargs.get("recruiter_id")

        # Assign recruiter deterministically if not provided
        if not recruiter_id:
            if job_id in ["J001", "J002"]:
                recruiter_id = "U301"
            elif job_id in ["J003", "J004"]:
                recruiter_id = "U304"
            else:
                recruiter_id = "U312"

        # Create shortlist entry with only essential data
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
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "shortlist_external_candidate",
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
