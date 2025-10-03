from tau_bench.envs.tool import Tool
import json
from typing import Any

class search_positions(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], title: str) -> str:
        positions = data.get("positions", [])
        hits = [p for p in positions if p["title"] == title]
        payload = hits
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "searchPositions",
                "description": "Return all positions that match the title. If no match, return an empty list.",
                "parameters": {
                    "type": "object",
                    "properties": {"title": {"type": "string"}},
                    "required": ["title"],
                    "additionalProperties": False,
                },
            },
        }
