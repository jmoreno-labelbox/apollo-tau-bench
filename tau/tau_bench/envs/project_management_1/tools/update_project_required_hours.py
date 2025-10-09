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

class UpdateProjectRequiredHours(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None, required_hours: int = None) -> str:
        if not all([project_id, required_hours]):
            payload = {"error": "project_id and required hours are required"}
            out = json.dumps(payload)
            return out

        projects = data.get("projects", [])

        for project in projects:
            if project.get("project_id") == project_id:
                project["required_hours_per_week"] = required_hours
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
                "name": "UpdateProjectRequiredHours",
                "description": "Update the hours per week required by a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The project ID",
                        },
                        "required_hours": {
                            "type": "integer",
                            "description": "Hours per week required by the project",
                        },
                    },
                    "required": ["project_id", "required_hours"],
                },
            },
        }
