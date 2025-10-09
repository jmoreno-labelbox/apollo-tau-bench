from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class ComputeCertExpiry(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, cert_id: str) -> str:
        payload = {"expiry_date": "2026-03-12", "days_until_expiry": 251}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "computeCertExpiry",
                "description": "Compute certification expiry date",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "cert_id": {"type": "string"},
                    },
                    "required": ["user_id", "cert_id"],
                },
            },
        }
