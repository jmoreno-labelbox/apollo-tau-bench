from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class Notify(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], recipient_ids: list = None, summary: str = None) -> str:
        if recipient_ids is None:
            recipient_ids = []

        if len(recipient_ids) == 0 or summary is None:
            payload = {
                "status": "error",
                "reason": "The recipient_ids and summary fields are required.",
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {"status": "ok", "recipients": recipient_ids, "summary": summary}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "notify",
                "description": "Notifies employees in recipient_ids with the contents of summary.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipient_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "The ids of the recipients to notify.",
                        },
                        "summary": {
                            "type": "string",
                            "description": "The summary to send to each recipient.",
                        },
                    },
                    "required": ["recipient_ids", "summary"],
                },
            },
        }
