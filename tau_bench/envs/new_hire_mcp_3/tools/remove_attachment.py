from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class RemoveAttachment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], attachment_id: str = None) -> str:
        attachments = data.get("attachments", [])
        data["attachments"] = [
            a for a in attachments if a.get("attachment_id") != attachment_id
        ]
        payload = {"removed_attachment_id": attachment_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveAttachment",
                "description": "Remove an attachment by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"attachment_id": {"type": "string"}},
                    "required": ["attachment_id"],
                },
            },
        }
