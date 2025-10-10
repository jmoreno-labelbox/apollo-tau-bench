# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetConsultantProfile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Returns consultant_id(s) (usually only one profile exists).
        """
        for c in data["consultants"]:
            if c["name"] == kwargs.get("name"):
                return json.dumps(c['consultant_id'])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetConsultantProfile",
                "description": "Retrieve consultant_id(s) from consultants.json.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                },
            },
        }
