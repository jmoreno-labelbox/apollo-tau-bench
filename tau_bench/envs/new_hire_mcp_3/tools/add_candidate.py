from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class AddCandidate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], candidate: dict = None) -> str:
        new_candidate = candidate or {}
        candidates = data.get("candidates", [])
        candidates.append(new_candidate)
        data["candidates"] = candidates
        payload = {"added_candidate": new_candidate}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addCandidate",
                "description": "Add a new candidate.",
                "parameters": {
                    "type": "object",
                    "properties": {"candidate": {"type": "object"}},
                    "required": ["candidate"],
                },
            },
        }
