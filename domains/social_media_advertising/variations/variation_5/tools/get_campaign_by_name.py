from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any

class GetCampaignByName(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        for c in data.get("campaigns", []):
            if c.get("name") == name:
                payload = c
                out = json.dumps(payload)
                return out
        payload = {"error": f"campaign {name} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCampaignByName",
                "description": "Retrieves a campaign by name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }
