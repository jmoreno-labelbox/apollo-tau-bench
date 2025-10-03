from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class GetConsultantProfile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], name: str = None) -> str:
        """
        Returns consultant_id(s) (usually only one profile exists).
        """
        for c in data["consultants"]:
            if c["name"] == name:
                return json.dumps(c['consultant_id'])
        return json.dumps(None)
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
