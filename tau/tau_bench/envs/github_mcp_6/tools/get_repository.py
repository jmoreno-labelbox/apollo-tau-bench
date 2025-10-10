# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRepository(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], owner: str, repo: str) -> str:
        """Get detailed information about a specific repository."""
        repositories = list(data.get("repositories", {}).values())

        # Locate the repository.
        target_repo = None
        for repository in repositories:
            repo_name = repository.get("repo_name") or repository.get("name")
            if repository.get("owner") == owner and repo_name == repo:
                target_repo = repository
                break

        if not target_repo:
            return json.dumps({
                "success": False,
                "error": f"Repository '{owner}/{repo}' not found",
                "error_code": "REPO_NOT_FOUND",
                "metadata": {
                    "searched_owner": owner,
                    "searched_repo": repo,
                    "available_repos": [f"{r.get('owner')}/{r.get('repo_name') or r.get('name')}" for r in repositories]
                }
            }, indent=2)

        return json.dumps({
            "success": True,
            "repository": {
                "name": target_repo.get("repo_name"),
                "owner": target_repo.get("owner"),
                "description": target_repo.get("description"),
                "private": target_repo.get("private", False),
                "default_branch": target_repo.get("default_branch", "main"),
                "created_at": target_repo.get("created_at"),
                "updated_at": target_repo.get("updated_at"),
                "language": target_repo.get("language"),
                "topics": target_repo.get("topics", []),
                "open_issues_count": target_repo.get("open_issues_count", 0),
                "forks_count": target_repo.get("forks_count", 0),
                "stars_count": target_repo.get("stars_count", 0)
            },
            "metadata": {
                "verification_method": "direct_repository_lookup",
                "repository_id": f"{owner}/{repo}"
            }
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_repository",
                "description": "Get detailed information about a specific repository",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {
                            "type": "string",
                            "description": "Repository owner (username or organization)"
                        },
                        "repo": {
                            "type": "string",
                            "description": "Repository name"
                        }
                    },
                    "required": ["owner", "repo"]
                }
            }
        }
