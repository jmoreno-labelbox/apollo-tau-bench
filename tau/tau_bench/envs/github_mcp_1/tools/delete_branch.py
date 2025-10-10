# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteBranch(Tool):
    """
    Deletes a branch from a repository.
    - Inputs: owner, repo_name, branch_name
    - Refuses to delete the repo's default branch.
    - Removes the branch entry and its aligned entries in branch_files, branch_contents, and branch_shas.
    - Returns details of what was removed and the remaining branches.
    - Deterministic (no timestamps or randomness).
    """

    @staticmethod
    def invoke(data: Dict[str, Any], branch_name = "", owner = "", repo_name = "") -> str:
        owner = owner.strip()
        repo_name = repo_name.strip()
        branch_name = branch_name.strip()

        if not owner or not repo_name or not branch_name:
            return json.dumps(
                {"error": "Parameters 'owner', 'repo_name', and 'branch_name' are required."},
                indent=2
            )

        # Optimal method for accessing the repository
        repos: List[Dict[str, Any]] = list(data.get("repositories", {}).values())
        if not isinstance(repos, list):
            return json.dumps(
                {"error": "Invalid database format: expected 'repositories' to be a list."},
                indent=2
            )

        # Find repository
        repo = next(
            (r for r in repos if r.get("owner") == owner and r.get("repo_name") == repo_name),
            None
        )
        if not repo:
            return json.dumps(
                {"error": f"Repository '{owner}/{repo_name}' not found."},
                indent=2
            )
    

        branches: List[str] = repo.get("branches", [])
        if branch_name not in branches:
            return json.dumps(
                {"error": f"Branch '{branch_name}' not found in repository '{owner}/{repo_name}'."},
                indent=2
            )

        # Prevent the deletion of the default branch.
        default_branch = repo.get("default_branch", "main")
        if branch_name == default_branch:
            return json.dumps(
                {"error": f"Cannot delete the default branch '{default_branch}'."},
                indent=2
            )

        idx = branches.index(branch_name)

        # Verify that per-branch arrays are present and aligned with the current branches.
        branch_files_all: List[List[str]] = repo.setdefault("branch_files", [])
        branch_contents_all: List[List[str]] = repo.setdefault("branch_contents", [])
        branch_shas: List[str] = repo.setdefault("branch_shas", [])


        while len(branch_files_all) < len(branches):
            branch_files_all.append([])
        while len(branch_contents_all) < len(branches):
            branch_contents_all.append([])
        while len(branch_shas) < len(branches):
            branch_shas.append("")

        # Gather deleted data (defensive indexing)
        removed_files = branch_files_all[idx] if idx < len(branch_files_all) else []

        # Execute deletions while maintaining array alignment.
        branches.pop(idx)
        if idx < len(branch_files_all):
            branch_files_all.pop(idx)
        if idx < len(branch_contents_all):
            branch_contents_all.pop(idx)
        if idx < len(branch_shas):
            branch_shas.pop(idx)

        updated_ts = get_current_updated_timestamp()
        repo["updated_ts"] = updated_ts

        add_terminal_message(data, f"Branch '{branch_name}' deleted from {owner}/{repo_name}.", get_current_updated_timestamp())

        return json.dumps(
            {
                "success": f"Branch '{branch_name}' deleted from {owner}/{repo_name}.",
                "repo": f"{owner}/{repo_name}",
                "deleted_branch": branch_name,
                "removed_file_count": len(removed_files),
                "remaining_branches": list(branches)
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_branch",
                "description": "Delete a non-default branch from a repository; updates branch_files, branch_contents, and branch_shas accordingly.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner (account/team)."},
                        "repo_name": {"type": "string", "description": "Repository name."},
                        "branch_name": {"type": "string", "description": "Branch name to delete."}
                    },
                    "required": ["owner", "repo_name", "branch_name"]
                }
            }
        }
