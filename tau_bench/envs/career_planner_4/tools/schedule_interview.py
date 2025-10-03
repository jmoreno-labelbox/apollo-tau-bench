from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class ScheduleInterview(Tool):
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
        payload = {
            "success": f"Interview scheduled for application {application_id} on {interview_date}"
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        return out

    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "scheduleInterview",
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
