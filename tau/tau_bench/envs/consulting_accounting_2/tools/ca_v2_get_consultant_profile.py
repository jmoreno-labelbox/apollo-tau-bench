from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class CaV2GetConsultantProfile(Tool):
    """Fetch consultant profile details."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        consultants = data.get("consultants", [])
        if not consultants:
            return _error("No consultant profile found.")
        payload = consultants[0]
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GetConsultantProfile",
                "description": "Retrieve the consultant's profile information including contact details and GST number.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
