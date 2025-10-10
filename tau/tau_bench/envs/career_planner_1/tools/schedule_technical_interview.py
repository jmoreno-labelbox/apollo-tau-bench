# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ScheduleTechnicalInterview(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        application_id = kwargs.get("application_id")

        # Create interview record with only essential data
        interview = {
            "application_id": application_id,
            "status": "scheduled",
            "created_at": datetime.now().isoformat(),
        }

        if "technical_interviews" not in data:
            data["technical_interviews"] = []
        data["technical_interviews"].append(interview)
        return f"Technical interview scheduled for application {application_id}."

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "schedule_technical_interview",
                "description": "Schedules a technical interview for a job application.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "application_id": {
                            "type": "string",
                            "description": "ID of the job application",
                        }
                    },
                    "required": ["application_id"],
                },
            },
        }
