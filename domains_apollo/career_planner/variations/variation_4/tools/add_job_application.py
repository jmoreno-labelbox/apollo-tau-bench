from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class AddJobApplication(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        application_id: str,
        user_id: str,
        job_id: str,
        apply_date: str,
    ) -> str:
        application = {
            "application_id": application_id,
            "user_id": user_id,
            "job_id": job_id,
            "apply_date": apply_date,
            "status": "Applied",
        }
        data.setdefault("job_applications", []).append(application)
        payload = {"success": f"Application {application_id} created for user {user_id}"}
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
                "name": "addJobApplication",
                "description": "Add a job application record",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "application_id": {"type": "string"},
                        "user_id": {"type": "string"},
                        "job_id": {"type": "string"},
                        "apply_date": {"type": "string"},
                    },
                    "required": ["application_id", "user_id", "job_id", "apply_date"],
                },
            },
        }
