# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class schedule_interview(Tool):
    @staticmethod
    def invoke(
        data, candidate_id: str, application_id: str, interview_date: str
    ) -> str:
        record = {
            "candidate_id": candidate_id,
            "application_id": application_id,
            "interview_date": interview_date,
        }
        data.setdefault("interview_schedule", []).append(record)
        return json.dumps(
            {
                "success": f"Interview scheduled for application {application_id} on {interview_date}"
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "schedule_interview",
                "description": "Schedule an interview for a candidate by updating the job application record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "candidate_id": {"type": "string"},
                        "application_id": {"type": "string"},
                        "interview_date": {"type": "string"},
                    },
                    "required": ["candidate_id", "application_id", "interview_date"],
                },
            },
        }
