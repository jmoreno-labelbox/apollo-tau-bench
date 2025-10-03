from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetProjectKey(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: str | None = None) -> str:
        projects = _get_table(data, "projects")
        proj = None
        if project_id:
            proj = next((p for p in projects if p.get("id") == project_id), None)
        if not proj:
            proj = (
                sorted(projects, key=lambda x: x.get("id", ""))[0] if projects else None
            )
        key = (proj or {}).get("project_key")
        payload = {"project_key": key}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProjectKey",
                "description": "Returns a deterministic project_key from projects.json (by id if provided, else first by id).",
                "parameters": {
                    "type": "object",
                    "properties": {"project_id": {"type": "string"}},
                    "required": [],
                },
            },
        }
