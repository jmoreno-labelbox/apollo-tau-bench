from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class DeleteRepository(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], owner: str, repo: str) -> str:
        """Delete a repository permanently."""
        pass
        repositories = data.get("repositories", [])

        #Locate and delete the repository
        for i, repository in enumerate(repositories):
            if repository["owner"] == owner and repository["repo_name"] == repo:
                repositories.pop(i)

                #Additionally, remove associated data
                #Delete commits
                commits = data.get("commits", [])
                for j in range(len(commits) - 1, -1, -1):
                    if commits[j]["owner"] == owner and commits[j]["repo_name"] == repo:
                        commits.pop(j)

                #Delete pull requests
                pull_requests = data.get("pull_requests", [])
                for j in range(len(pull_requests) - 1, -1, -1):
                    if (
                        pull_requests[j]["owner"] == owner
                        and pull_requests[j]["repo_name"] == repo
                    ):
                        pull_requests.pop(j)

                #Delete issues
                issues = data.get("issues", [])
                for j in range(len(issues) - 1, -1, -1):
                    if issues[j]["owner"] == owner and issues[j]["repo_name"] == repo:
                        issues.pop(j)

                #Delete code scanning alerts
                alerts = data.get("code_scanning_alerts", [])
                for j in range(len(alerts) - 1, -1, -1):
                    if alerts[j]["owner"] == owner and alerts[j]["repo_name"] == repo:
                        alerts.pop(j)
                payload = {"deleted": True, "repository": f"{owner}/{repo}"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"Repository {owner}/{repo} not found"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteRepository",
                "description": "Delete a repository permanently.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"},
                    },
                    "required": ["owner", "repo"],
                },
            },
        }
