from tau_bench.envs.tool import Tool
import json
from typing import Any

class NotifyManagementTeam(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], report_path: str = None, recipient_group: str = None, subject: str = None) -> str:
        pass
        payload = {
            "status": "notified",
            "recipient_group": recipient_group,
            "subject": subject,
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
                "name": "notifyManagementTeam",
                "description": "Send notification to management team with report.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_path": {"type": "string"},
                        "recipient_group": {"type": "string"},
                        "subject": {"type": "string"},
                    },
                    "required": ["report_path", "recipient_group", "subject"],
                },
            },
        }
