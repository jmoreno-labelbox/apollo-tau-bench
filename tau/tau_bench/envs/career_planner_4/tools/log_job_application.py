# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class log_job_application(Tool):
    @staticmethod
    def invoke(
        data,
        candidate_id: str,
        job_id: str,
        apply_date: str,
        skill_match_score: int,
        application_id: Optional[str] = None,
    ) -> str:
        application = {
            "application_id": application_id or "APP001",
            "candidate_id": candidate_id,
            "job_id": job_id,
            "apply_date": apply_date,
            "skill_match_score": skill_match_score,
        }
        data.setdefault("job_applications", []).append(application)
        return json.dumps(
            {
                "success": f"Application {application['application_id']} logged for candidate {candidate_id}"
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "log_job_application",
                "description": "Log a new job application record for an external candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "job_id": {"type": "string"},
                        "apply_date": {"type": "string"},
                        "skill_match_score": {"type": "integer"},
                        "application_id": {"type": "string"},
                    },
                    "required": [
                        "candidate_id",
                        "job_id",
                        "apply_date",
                        "skill_match_score",
                    ],
                },
            },
        }
