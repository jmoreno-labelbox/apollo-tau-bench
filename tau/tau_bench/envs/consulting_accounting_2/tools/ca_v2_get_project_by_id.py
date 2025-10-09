from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class CaV2GetProjectById(Tool):
    """Retrieve project information using project ID."""

    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None) -> str:
        if not project_id:
            return _error("project_id is required.")

        projects = data.get("projects", [])
        project = _find_one(projects, "project_id", project_id)

        if not project:
            return _error(f"Project {project_id} not found.")

        return _ok(
            project_id=project.get("project_id"),
            isbn=project.get("isbn"),
            title=project.get("title"),
            publisher_id=project.get("publisher_id"),
            default_hourly_rate=project.get("default_hourly_rate"),
            override_hourly_rate=project.get("override_hourly_rate"),
            status=project.get("status"),
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GetProjectById",
                "description": "Get project details by project ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"project_id": {"type": "string"}},
                    "required": ["project_id"],
                },
            },
        }
