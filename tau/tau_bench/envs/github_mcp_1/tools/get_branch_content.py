from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetBranchContent(Tool):
    """
    Returns branch-specific information for a given owner/repository/branch.
    Output includes: branch name, branch files, branch contents, and branch SHA,
    all aligned by the same branch index.
    """

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = "", repo_name: str = "", branch_name: str = "") -> str:
        owner = owner.strip()
        repo_name = repo_name.strip()
        branch = branch_name.strip()

        if not owner or not repo_name or not branch:
            payload = {
                    "error": "Parameters 'owner', 'repo_name', and 'branch' are all required."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Support either {"repositories": [...]} or a direct list
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

        branches = repo.get("branches", [])
        if branch not in branches:
            payload = {
                    "error": f"Branch '{branch}' not found in repository '{owner}/{repo_name}'."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        idx = branches.index(branch)

        # Fetch aligned per-branch artifacts (defensive against missing keys)
        branch_files_all = repo.get("branch_files", [])
        branch_contents_all = repo.get("branch_contents", [])
        branch_shas_all = repo.get("branch_shas", [])

        # Fallbacks: if per-branch arrays are missing, fall back to repo-wide files/contents
        files = None
        contents = None

        if idx < len(branch_files_all):
            files = branch_files_all[idx]
        elif "file_paths" in repo:
            files = repo.get("file_paths", [])

        if idx < len(branch_contents_all):
            contents = branch_contents_all[idx]
        elif "file_contents" in repo:
            contents = repo.get("file_contents", [])

        sha = branch_shas_all[idx] if idx < len(branch_shas_all) else None

        result = {
            "branch": branch,
            "branch_files": files if files is not None else [],
            "branch_contents": contents if contents is not None else [],
            "branch_sha": sha,
        }
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetBranchContent",
                "description": "Fetch branch-level files, contents, and SHA for a given owner/repository/branch.",
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
                        "branch_name": {
                            "type": "string",
                            "description": "Branch name to retrieve.",
                        },
                    },
                    "required": ["owner", "repo_name", "branch_name"],
                },
            },
        }
