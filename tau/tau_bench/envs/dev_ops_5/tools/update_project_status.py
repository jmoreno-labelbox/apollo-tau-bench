# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateProjectStatus(Tool):
    """Updates the active status of a project."""
    @staticmethod
    def invoke(data: Dict[str, Any], id, is_active) -> str:
        project_id = id
        projects = list(data.get("projects", {}).values())
        for p in projects:
            if p.get("id") == project_id:
                p["is_active"] = is_active
                return json.dumps({"status": "success", "message": f"Project '{project_id}' active status set to {is_active}."})
        return json.dumps({"error": f"Project with ID '{project_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_project_status",
                "description": "Updates the active status of a project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "is_active": {"type": "boolean"}
                    },
                    "required": ["id", "is_active"],
                },
            },
        }
