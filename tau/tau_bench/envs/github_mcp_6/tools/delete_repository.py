# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteRepository(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str) -> str:
        """Delete a repository permanently."""
        repositories = list(data.get("repositories", {}).values())

        # Locate and delete the repository.
        for i, repository in enumerate(repositories):
            if repository["owner"] == owner and repository["repo_name"] == repo:
                repositories.pop(i)

                # Additionally, remove associated data.
                # Eliminate commits
                commits = list(data.get("commits", {}).values())
                for j in range(len(commits) - 1, -1, -1):
                    if commits[j]["owner"] == owner and commits[j]["repo_name"] == repo:
                        commits.pop(j)

                # Eliminate pull requests.
                pull_requests = list(data.get("pull_requests", {}).values())
                for j in range(len(pull_requests) - 1, -1, -1):
                    if pull_requests[j]["owner"] == owner and pull_requests[j]["repo_name"] == repo:
                        pull_requests.pop(j)

                # Eliminate problems.
                issues = list(data.get("issues", {}).values())
                for j in range(len(issues) - 1, -1, -1):
                    if issues[j]["owner"] == owner and issues[j]["repo_name"] == repo:
                        issues.pop(j)

                # Eliminate code scanning notifications.
                alerts = data.get("code_scanning_alerts", [])
                for j in range(len(alerts) - 1, -1, -1):
                    if alerts[j]["owner"] == owner and alerts[j]["repo_name"] == repo:
                        alerts.pop(j)

                return json.dumps({"deleted": True, "repository": f"{owner}/{repo}"}, indent=2)

        return json.dumps({"error": f"Repository {owner}/{repo} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_repository",
                "description": "Delete a repository permanently.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner"},
                        "repo": {"type": "string", "description": "Repository name"}
                    },
                    "required": ["owner", "repo"]
                }
            }
        }
