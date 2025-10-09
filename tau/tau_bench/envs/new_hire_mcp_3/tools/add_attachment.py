from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class AddAttachment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], attachment: dict = None) -> str:
        new_attach = attachment or {}
        attachments = data.get("attachments", [])
        attachments.append(new_attach)
        data["attachments"] = attachments
        payload = {"added_attachment": new_attach}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddAttachment",
                "description": "Add a new attachment.",
                "parameters": {
                    "type": "object",
                    "properties": {"attachment": {"type": "object"}},
                    "required": ["attachment"],
                },
            },
        }
