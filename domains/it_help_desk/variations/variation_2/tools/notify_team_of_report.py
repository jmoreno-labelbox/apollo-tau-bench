from tau_bench.envs.tool import Tool
import json
from typing import Any

class NotifyTeamOfReport(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], pdf_path: str = None, csv_path: str = None, report_date: Any = None) -> str:
        recipient = "it-management-dl@company.com"
        payload = {
            "status": "notified",
            "recipient": recipient,
            "attachments": [pdf_path, csv_path],
        }
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "NotifyTeamOfReport",
                "description": "Sends an email notification with the generated reports as attachments.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pdf_path": {"type": "string"},
                        "csv_path": {"type": "string"},
                    },
                    "required": ["pdf_path", "csv_path"],
                },
            },
        }
