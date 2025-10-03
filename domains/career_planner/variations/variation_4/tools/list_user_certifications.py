from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class ListUserCertifications(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        user_certification = data.get("user_certification", [])
        certs = [
            c for c in user_certification if c.get("user_id") == user_id
        ]
        payload = {"certifications": certs}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "listUserCertifications",
                "description": "List certifications for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
