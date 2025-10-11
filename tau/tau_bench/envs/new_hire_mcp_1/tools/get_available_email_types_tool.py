# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAvailableEmailTypesTool(Tool):
    """Returns a list of valid email types that can be used with the check_email_communication_gaps tool."""

    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        email_types = [
            "welcome",
            "asset provisioning request",
            "onboarding reminder",
            "orientation invitation",
            "introduction"
        ]
        return json.dumps(email_types, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_available_email_types",
                "description": "Returns a list of valid email types for checking communication gaps.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
            },
        }
