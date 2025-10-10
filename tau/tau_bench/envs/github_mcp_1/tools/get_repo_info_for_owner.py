# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRepoInfoForOwner(Tool):
    """Returns key repository info (including file paths and contents) for a given owner + repo_name."""

    @staticmethod
    def invoke(data: Dict[str, Any], owner = "", repo_name = "") -> str:
        owner = owner.strip()
        repo_name = repo_name.strip()

        if not owner or not repo_name:
            return json.dumps(
                {"error": "Both 'owner' and 'repo_name' are required."},
                indent=2
            )

        # DB could either be { "repositories": [...] } or a straightforward list.
        repos = list(data.get("repositories", {}).values())

        repo = next(
            (r for r in repos
             if r.get("owner") == owner and r.get("repo_name") == repo_name),
            None
        )
        if not repo:
            return json.dumps(
                {"error": f"Repository '{owner}/{repo_name}' not found."},
                indent=2
            )

        result = {
            "owner": repo.get("owner"),
            "repo_name": repo.get("repo_name"),
            "description": repo.get("description_nullable"),
            "private": repo.get("private_flag"),
            "auto_init": repo.get("auto_init_flag"),
            "default_branch": repo.get("default_branch"),
            "file_paths": repo.get("file_paths", []),
            "file_contents": repo.get("file_contents", []),
            "branches": repo.get("branches", []),
            "branch_shas": repo.get("branch_shas", []),
            "created_ts": repo.get("created_ts"),
            "updated_ts": repo.get("updated_ts"),
            
        }
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_repo_info_for_owner",
                "description": "Fetches repository metadata including owner, repo_name, description, private flag, auto_init, default branch, branches, branch SHAs, timestamps, and file paths/contents.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {
                            "type": "string",
                            "description": "Repository owner (account/team)."
                        },
                        "repo_name": {
                            "type": "string",
                            "description": "Repository name."
                        }
                    },
                    "required": ["owner", "repo_name"]
                }
            }
        }
