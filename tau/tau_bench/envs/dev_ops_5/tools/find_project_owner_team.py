# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindProjectOwnerTeam(Tool):
    """Finds the owner team for a project."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")
        repos = list(data.get("repositories", {}).values())
        teams = data.get("teams", [])
        
        repo_id = None
        for repo in repos:
            if repo.get("project_id") == project_id:
                repo_id = repo.get("id")
                break
        
        if not repo_id:
            return json.dumps({"error": "Could not determine repository for project."})
            
        for team in teams:
            # "project_targets": ["proj_001", "proj_002", "proj_003"],
            if project_id in team['project_focus']:
                 return json.dumps({"team_id": team['id']})

        return json.dumps({"error": f"Could not determine owner for project '{project_id}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_project_owner_team",
                "description": "Finds the owner team for a project.",
                "parameters": {
                    "type": "object",
                    "properties": {"project_id": {"type": "string"}},
                    "required": ["project_id"],
                },
            },
        }
