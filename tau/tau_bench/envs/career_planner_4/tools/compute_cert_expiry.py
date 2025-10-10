# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class compute_cert_expiry(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, cert_id: str) -> str:
        # Stub implementation - in a real system, it would verify actual expiration dates.
        return json.dumps(
            {"expiry_date": "2026-03-12", "days_until_expiry": 251}, indent=2
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "compute_cert_expiry",
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
