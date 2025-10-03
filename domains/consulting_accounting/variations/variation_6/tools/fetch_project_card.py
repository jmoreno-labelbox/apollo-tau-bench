from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class FetchProjectCard(Tool):
    """Get project using project_id."""

    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None) -> str:
        pid = project_id
        row = next(
            (p for p in data.get("projects", []) if p.get("project_id") == pid), None
        )
        if not row:
            payload = {"error": f"project_id '{pid}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchProjectCard",
                "description": "Fetch a project by id.",
                "parameters": {
                    "type": "object",
                    "properties": {"project_id": {"type": "string"}},
                    "required": ["project_id"],
                },
            },
        }
