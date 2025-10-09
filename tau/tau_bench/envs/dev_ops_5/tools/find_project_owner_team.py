from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FindProjectOwnerTeam(Tool):
    """Identifies the owner team for a project."""

    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None) -> str:
        repos = data.get("repositories", [])
        teams = data.get("teams", [])

        repo_id = None
        for repo in repos:
            if repo.get("project_id") == project_id:
                repo_id = repo.get("id")
                break

        if not repo_id:
            payload = {"error": "Could not determine repository for project."}
            out = json.dumps(payload)
            return out

        for team in teams:
            #"project_focus": ["proj_001", "proj_002", "proj_003"],
            if project_id in team["project_focus"]:
                payload = {"team_id": team["id"]}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Could not determine owner for project '{project_id}'."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindProjectOwnerTeam",
                "description": "Finds the owner team for a project.",
                "parameters": {
                    "type": "object",
                    "properties": {"project_id": {"type": "string"}},
                    "required": ["project_id"],
                },
            },
        }
