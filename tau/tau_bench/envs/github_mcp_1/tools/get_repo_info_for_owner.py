from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetRepoInfoForOwner(Tool):
    """Returns key repository info (including file paths and contents) for a given owner + repo_name."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = "", repo_name: str = "") -> str:
        owner = owner.strip()
        repo_name = repo_name.strip()

        if not owner or not repo_name:
            payload = {"error": "Both 'owner' and 'repo_name' are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        # DB may be { "repositories": [...] } or a direct list
        repos = data.get("repositories", {}).values()

        repo = next(
            (
                r
                for r in repos.values() if r.get("owner") == owner and r.get("repo_name") == repo_name
            ),
            None,
        )
        if not repo:
            payload = {"error": f"Repository '{owner}/{repo_name}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out

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
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRepoInfoForOwner",
                "description": "Fetches repository metadata including owner, repo_name, description, private flag, auto_init, default branch, branches, branch SHAs, timestamps, and file paths/contents.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {
                            "type": "string",
                            "description": "Repository owner (account/team).",
                        },
                        "repo_name": {
                            "type": "string",
                            "description": "Repository name.",
                        },
                    },
                    "required": ["owner", "repo_name"],
                },
            },
        }
