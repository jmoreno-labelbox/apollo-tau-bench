from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any

class GetAdsetDetailsByID(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None) -> str:
        aid = adset_id
        for a in data.get("adsets", []):
            if a.get("adset_id") == aid:
                payload = a
                out = json.dumps(payload)
                return out
        payload = {"error": f"adset {aid} not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAdsetDetailsById",
                "description": "Gets one ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {"adset_id": {"type": "string"}},
                    "required": ["adset_id"],
                },
            },
        }
