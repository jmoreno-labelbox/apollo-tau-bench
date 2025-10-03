from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetUserCertification(Tool):
    """Retrieve certifications held by a user."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        uid = user_id
        certs = [
            c for c in data.get("user_certifications", []) if c.get("user_id") == uid
        ]
        payload = certs
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserCertification",
                "description": "Get user certifications.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
