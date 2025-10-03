from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class FetchProjects(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], unexpected: Any = None) -> str:
        payload = {"projects": data.get("projects", [])}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchProjects",
                "description": "List all projects.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
