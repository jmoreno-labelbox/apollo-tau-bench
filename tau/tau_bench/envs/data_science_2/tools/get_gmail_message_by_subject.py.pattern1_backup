# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetGmailMessageBySubject(Tool):
    """
    Retrieves a gmail_messages record by exact subject.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], subject: str) -> str:
        rows = data.get("gmail_messages", [])
        for row in rows:
            if row.get("subject") == subject:
                return json.dumps(row)
        return json.dumps({"error": "gmail message not found", "subject": subject})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_gmail_message_by_subject",
                "description": "Retrieves a gmail_messages record by exact subject.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject": {"type": "string"}
                    },
                    "required": ["subject"]
                }
            }
        }
