from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any

class GetAvailableEmailTypesTool(Tool):
    """Provides a list of acceptable email types for use with the check_email_communication_gaps tool."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        email_types = [
            "welcome",
            "asset provisioning request",
            "onboarding reminder",
            "orientation invitation",
            "introduction",
        ]
        payload = email_types
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAvailableEmailTypes",
                "description": "Returns a list of valid email types for checking communication gaps.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
            },
        }
