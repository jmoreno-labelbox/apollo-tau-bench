from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

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
    def invoke(data: dict[str, Any], owner: str = "", repo_name: str = "", branch_name: str = "") -> str:
        owner = owner.strip()
        repo_name = repo_name.strip()
        branch_name = branch_name.strip()

        if not owner or not repo_name or not branch_name:
            payload = {
                    "error": "Parameters 'owner', 'repo_name', and 'branch_name' are required."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #Preferred repository access pattern
        repos: list[dict[str, Any]] = data.get("repositories", [])
        if not isinstance(repos, list):
            payload = {
                    "error": "Invalid database format: expected 'repositories' to be a list."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #Locate repository
        repo = next(
            (
                r
                for r in repos
                if r.get("owner") == owner and r.get("repo_name") == repo_name
            ),
            None,
        )
        if not repo:
            payload = {"error": f"Repository '{owner}/{repo_name}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        branches: list[str] = repo.get("branches", [])
        if branch_name not in branches:
            payload = {
                    "error": f"Branch '{branch_name}' not found in repository '{owner}/{repo_name}'."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #Do not allow deleting default branch
        default_branch = repo.get("default_branch", "main")
        if branch_name == default_branch:
            payload = {"error": f"Cannot delete the default branch '{default_branch}'."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        idx = branches.index(branch_name)

        #Ensure per-branch arrays exist and are aligned to current branches
        branch_files_all: list[list[str]] = repo.setdefault("branch_files", [])
        branch_contents_all: list[list[str]] = repo.setdefault("branch_contents", [])
        branch_shas: list[str] = repo.setdefault("branch_shas", [])

        while len(branch_files_all) < len(branches):
            branch_files_all.append([])
        while len(branch_contents_all) < len(branches):
            branch_contents_all.append([])
        while len(branch_shas) < len(branches):
            branch_shas.append("")

        #Collect removed info (defensive indexing)
        removed_files = branch_files_all[idx] if idx < len(branch_files_all) else []

        #Perform deletions (keep arrays aligned)
        branches.pop(idx)
        if idx < len(branch_files_all):
            branch_files_all.pop(idx)
        if idx < len(branch_contents_all):
            branch_contents_all.pop(idx)
        if idx < len(branch_shas):
            branch_shas.pop(idx)

        updated_ts = get_current_updated_timestamp()
        repo["updated_ts"] = updated_ts

        add_terminal_message(
            data,
            f"Branch '{branch_name}' deleted from {owner}/{repo_name}.",
            get_current_updated_timestamp(),
        )
        payload = {
                "success": f"Branch '{branch_name}' deleted from {owner}/{repo_name}.",
                "repo": f"{owner}/{repo_name}",
                "deleted_branch": branch_name,
                "removed_file_count": len(removed_files),
                "remaining_branches": list(branches),
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeleteBranch",
                "description": "Delete a non-default branch from a repository; updates branch_files, branch_contents, and branch_shas accordingly.",
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
                            "description": "Branch name to delete.",
                        },
                    },
                    "required": ["owner", "repo_name", "branch_name"],
                },
            },
        }
