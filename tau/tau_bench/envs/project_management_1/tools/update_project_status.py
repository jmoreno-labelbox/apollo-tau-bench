# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateProjectStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")
        status = kwargs.get("status")

        if not all([project_id, status]):
            return json.dumps({"error": "project_id and status are required"})

        projects = list(data.get("projects", {}).values())

        for project in projects:
            if project.get("project_id") == project_id:
                project["status"] = status
                return json.dumps({"success": True, "project": project})

        return json.dumps({"error": f"Project with ID '{project_id}' not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_project_status",
                "description": "Update the status of a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The project ID",
                        },
                        "status": {
                            "type": "string",
                            "description": "New status: active, completed, cancelled, on-hold",
                        },
                    },
                    "required": ["project_id", "status"],
                },
            },
        }
