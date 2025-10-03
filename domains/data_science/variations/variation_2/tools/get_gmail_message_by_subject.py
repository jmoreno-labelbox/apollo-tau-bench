from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetGmailMessageBySubject(Tool):
    """Fetches a gmail_messages record using the precise subject."""

    @staticmethod
    def invoke(data: dict[str, Any], subject: str) -> str:
        rows = data.get("gmail_messages", [])
        for row in rows:
            if row.get("subject") == subject:
                payload = row
                out = json.dumps(payload)
                return out
        payload = {"error": "gmail message not found", "subject": subject}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetGmailMessageBySubject",
                "description": "Retrieves a gmail_messages record by exact subject.",
                "parameters": {
                    "type": "object",
                    "properties": {"subject": {"type": "string"}},
                    "required": ["subject"],
                },
            },
        }
