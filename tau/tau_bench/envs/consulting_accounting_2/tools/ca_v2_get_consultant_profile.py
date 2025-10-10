# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CaV2GetConsultantProfile(Tool):
    """Retrieve consultant profile information."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        consultants = data.get("consultants", [])
        if not consultants:
            return _error("No consultant profile found.")
        return json.dumps(consultants[0])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_consultant_profile",
                "description": "Retrieve the consultant's profile information including contact details and GST number.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
