# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class search_positions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], title: str) -> str:
        positions = data.get("positions", [])
        hits = [p for p in positions if p["title"] == title]
        return json.dumps(hits, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_positions",
                "description": "Return all positions that match the title. If no match, return an empty list.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"}
                    },
                    "required": ["title"],
                    "additionalProperties": False
                }
            }
        }
