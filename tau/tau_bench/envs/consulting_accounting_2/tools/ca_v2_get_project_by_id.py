# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool








def _ok() -> str:
    out = {"status": "success"}
    out.update(payload)
    return json.dumps(out)

def _find_one(lst: List[Dict[str, Any]], key: str, value: Any) -> Dict[str, Any] | None:
    for x in lst or []:
        if x.get(key) == value:
            return x
    return None

def _error(msg: str) -> str:
    return json.dumps({"error": msg})

class CaV2GetProjectById(Tool):
    """Get project details by project ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], project_id) -> str:

        if not project_id:
            return _error("project_id is required.")

        projects = list(data.get("projects", {}).values())
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
            status=project.get("status")
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_project_by_id",
                "description": "Get project details by project ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"}
                    },
                    "required": ["project_id"],
                },
            },
        }