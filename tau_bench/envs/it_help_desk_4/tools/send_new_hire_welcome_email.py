from tau_bench.envs.tool import Tool
import json
from typing import Any

class SendNewHireWelcomeEmail(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], upn: str = None, personal_email: str = None, pickup_code: str = None) -> str:
        payload = {
            "status": "sent",
            "recipients": [upn, personal_email],
            "pickup_code": pickup_code,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "sendNewHireWelcomeEmail",
                "description": "Sends a welcome email to the new hire's company and personal addresses with device pickup information.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "upn": {"type": "string"},
                        "personal_email": {"type": "string"},
                        "pickup_code": {"type": "string"},
                    },
                    "required": ["upn", "personal_email", "pickup_code"],
                },
            },
        }
