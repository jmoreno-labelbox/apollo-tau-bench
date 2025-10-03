from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetProjectKeyV2(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: str | None = None) -> str:
        pass
        projects = _get_table(data, "projects")
        proj = None
        if project_id:
            proj = next((p for p in projects if p.get("id") == project_id), None)
        if not proj and projects:
            proj = sorted(projects, key=lambda x: x.get("id", ""))[0]
        payload = {"project_key": (proj or {}).get("project_key")}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getProjectKeyV2",
                "description": "Returns a deterministic project_key from projects.json (by id if provided, else first by id).",
                "parameters": {
                    "type": "object",
                    "properties": {"project_id": {"type": "string"}},
                    "required": [],
                },
            },
        }
