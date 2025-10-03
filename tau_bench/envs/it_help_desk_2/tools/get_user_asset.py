from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetUserAsset(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None) -> str:
        assets = data.get("it_assets", [])
        asset = next((a for a in assets if a.get("assigned_to") == employee_id), None)
        if not asset:
            payload = {"employee_id": employee_id, "asset": None}
            out = json.dumps(payload, indent=2)
            return out
        payload = asset
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetUserAsset",
                "description": "Find an IT asset assigned to a specific employee.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                },
            },
        }
