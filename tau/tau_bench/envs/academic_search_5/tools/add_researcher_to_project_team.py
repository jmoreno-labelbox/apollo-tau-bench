from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AddResearcherToProjectTeam(Tool):
    """Utility for including a researcher in a project's team."""

    @staticmethod
    def invoke(data: dict[str, Any], project_id: Any = None, user_id: Any = None) -> str:
        project_id = project_id
        user_id = user_id
        if not project_id or not user_id:
            payload = {"error": "project_id and user_id are required."}
            out = json.dumps(payload)
            return out

        projects = data.get("projects", {}).values()
        for project in projects.values():
            if project.get("project_id") == project_id:
                # This presumes the data model can be enhanced with a 'team_members' list.
                if "team_members" not in project:
                    project["team_members"] = []
                if user_id not in project["team_members"] and user_id != project.get(
                    "lead_researcher_id"
                ):
                    project["team_members"].append(user_id)
                    payload = {
                        "success": True,
                        "message": f"User {user_id} added to project {project_id}.",
                    }
                    out = json.dumps(payload)
                    return out
                else:
                    payload = {
                        "error": "User is already on the team or is the lead researcher."
                    }
                    out = json.dumps(payload)
                    return out
        payload = {"error": "Project not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddResearcherToProjectTeam",
                "description": "Adds a researcher to the team of an existing project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The ID of the project.",
                        },
                        "user_id": {
                            "type": "string",
                            "description": "The user ID of the researcher to add.",
                        },
                    },
                    "required": ["project_id", "user_id"],
                },
            },
        }
