# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateRepository(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], name: str, description: str, private: bool, autoInit: bool) -> str:
        """Create a repository with metadata."""
        repositories = list(data.get("repositories", {}).values())

        # Verify the existence of the repository name.
        existing_names = [repo["repo_name"] for repo in repositories]
        repo_name = name
        if name in existing_names:
            repo_name = f"{name}_v2"

        # Retrieve the authenticated user.
        auth_users = data.get("authentication", [])
        username = auth_users[0]["username"] if auth_users else "default_user"

        # Add a new entry to the repository.
        new_repo = {
            "owner": username,
            "repo_name": repo_name,
            "description": description,
            "private": private,
            "default_branch": "main",
            "file_paths": ["README.md"] if autoInit else [],
            "file_contents": [f"# {repo_name}\n\nAutomatically created repository."] if autoInit else [],
            "branches": ["main"],
            "branch_files": [["README.md"]] if autoInit else [[]],
            "branch_contents": [[f"# {repo_name}\n\nAutomatically created repository."]] if autoInit else [[]],
            "branch_shas": [f"repo_{len(repositories) + 1}_init_sha"],
            "created_at": "2023-12-05T12:00:00Z",
            "updated_at": "2023-12-05T12:00:00Z"
        }

        repositories.append(new_repo)

        return json.dumps({
            "name": repo_name,
            "default_branch": "main"
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_repository",
                "description": "Create a repository with metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Repository name"},
                        "description": {"type": "string", "description": "Repository description"},
                        "private": {"type": "boolean", "description": "Whether repository is private"},
                        "autoInit": {"type": "boolean", "description": "Auto-initialize with README"}
                    },
                    "required": ["name", "description", "private", "autoInit"]
                }
            }
        }
