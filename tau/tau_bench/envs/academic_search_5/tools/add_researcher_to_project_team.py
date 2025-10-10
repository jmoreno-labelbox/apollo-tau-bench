# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddResearcherToProjectTeam(Tool):
    """Tool to add a researcher to a project's team."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get('project_id')
        user_id = kwargs.get('user_id')
        if not project_id or not user_id:
            return json.dumps({"error": "project_id and user_id are required."})

        projects = list(data.get('projects', {}).values())
        for project in projects:
            if project.get('project_id') == project_id:
                # This presumes that the data model can incorporate a 'team_members' array.
                if 'team_members' not in project:
                    project['team_members'] = []
                if user_id not in project['team_members'] and user_id != project.get('lead_researcher_id'):
                    project['team_members'].append(user_id)
                    return json.dumps({"success": True, "message": f"User {user_id} added to project {project_id}."})
                else:
                    return json.dumps({"error": "User is already on the team or is the lead researcher."})
        return json.dumps({"error": "Project not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_researcher_to_project_team",
                "description": "Adds a researcher to the team of an existing project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "The ID of the project."},
                        "user_id": {"type": "string", "description": "The user ID of the researcher to add."}
                    },
                    "required": ["project_id", "user_id"]
                }
            }
        }
