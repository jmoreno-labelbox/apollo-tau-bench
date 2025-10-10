# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class add_job_application(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
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
        return json.dumps(
            {"success": f"Application {application_id} created for user {user_id}"},
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "add_job_application",
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
