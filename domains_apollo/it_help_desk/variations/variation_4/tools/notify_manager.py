from tau_bench.envs.tool import Tool
import json
from typing import Any

class NotifyManager(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], manager_id: str = None, subject: str = None, body: str = None) -> str:
        payload = {"status": "sent", "recipient_manager_id": manager_id, "subject": subject}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "notifyManager",
                "description": "Sends a notification email to a manager for onboarding or offboarding events.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "manager_id": {"type": "string"},
                        "subject": {"type": "string"},
                        "body": {"type": "string"},
                    },
                    "required": ["manager_id", "subject", "body"],
                },
            },
        }
