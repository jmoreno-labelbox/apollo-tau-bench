from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any

class GetAdsByAdsetID(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None) -> str:
        rows = [r for r in data.get("ads", []) if r.get("adset_id") == adset_id]
        payload = {"ads": rows}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAdsByAdsetId",
                "description": "Lists ads by ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {"adset_id": {"type": "string"}},
                    "required": ["adset_id"],
                },
            },
        }
