from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateProjectStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None, status: str = None) -> str:
        if not all([project_id, status]):
            payload = {"error": "project_id and status are required"}
            out = json.dumps(payload)
            return out

        projects = data.get("projects", [])

        for project in projects:
            if project.get("project_id") == project_id:
                project["status"] = status
                payload = {"success": True, "project": project}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Project with ID '{project_id}' not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateProjectStatus",
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
