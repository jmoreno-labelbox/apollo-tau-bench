from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class ScheduleTechnicalInterview(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], application_id: str) -> str:
        # Generate an interview record containing only vital data
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
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ScheduleTechnicalInterview",
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
