# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteFileInRepo(Tool):
    """
    Deletes a file from a repository branch.
    - Removes from branch_files[idx] and branch_contents[idx] at the same index.
    - If branch is 'main', also removes from repo-level file_paths/file_contents.
    - Returns remaining files in the branch (and repo-level files if branch is 'main').
    """

    @staticmethod
    def invoke(data: Dict[str, Any], branch_name = "", file_name = "", owner = "", repo_name = "") -> str:
        owner = owner.strip()
        repo_name = repo_name.strip()
        branch_name = branch_name.strip()
        file_name = file_name.strip()

        if not owner or not repo_name or not branch_name or not file_name:
            return json.dumps(
                {"error": "Parameters 'owner', 'repo_name', 'branch_name', and 'file_name' are required."},
                indent=2
            )

        # Optimal method for accessing the repository
        repos: List[Dict[str, Any]] = list(data.get("repositories", {}).values())
        if not isinstance(repos, list):
            return json.dumps(
                {"error": "Invalid database format: expected 'repositories' to be a list."},
                indent=2
            )

        # Find the repository.
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
        idx = branches.index(branch_name)

        # Verify the existence and alignment of structures for each branch.
        branch_files_all: List[List[str]] = repo.setdefault("branch_files", [])
        branch_contents_all: List[List[str]] = repo.setdefault("branch_contents", [])
        while len(branch_files_all) < len(branches):
            branch_files_all.append([])
        while len(branch_contents_all) < len(branches):
            branch_contents_all.append([])

        branch_files = branch_files_all[idx]
        branch_contents = branch_contents_all[idx]

        if not isinstance(branch_files, list) or not isinstance(branch_contents, list):
            return json.dumps(
                {"error": "Invalid repository format: branch_files/branch_contents must be lists."},
                indent=2
            )

        if file_name not in branch_files:
            return json.dumps(
                {"error": f"File '{file_name}' not found in branch '{branch_name}'."},
                indent=2
            )

        # Ensure arrays are aligned prior to removal.
        while len(branch_contents) < len(branch_files):
            branch_contents.append("")

        fidx = branch_files.index(file_name)
        removed_content = branch_contents[fidx]

        # Remove from branch-specific arrays (identical index)
        branch_files.pop(fidx)
        branch_contents.pop(fidx)

        # If on the 'main' branch, also delete from repository-wide lists (by filename).
        repo_files_after = None
        if branch_name == "main":
            repo.setdefault("file_paths", [])
            repo.setdefault("file_contents", [])
            if file_name in repo["file_paths"]:
                ridx = repo["file_paths"].index(file_name)
                # Ensure proper alignment prior to removal.
                while len(repo["file_contents"]) < len(repo["file_paths"]):
                    repo["file_contents"].append("")
                repo["file_paths"].pop(ridx)
                repo["file_contents"].pop(ridx)
            repo_files_after = list(repo.get("file_paths", []))


        repo["updated_ts"] = get_current_updated_timestamp()
        add_terminal_message(data, f"Deleted '{file_name}' from {owner}/{repo_name}@{branch_name}.", get_current_updated_timestamp())

        result = {
            "success": f"Deleted '{file_name}' from {owner}/{repo_name}@{branch_name}.",
            "repo": f"{owner}/{repo_name}",
            "branch": branch_name,
            "deleted": {
                "file_name": file_name,
                "content": removed_content
            },
            "available_files": list(branch_files)  # files left in this branch
        }
        if repo_files_after is not None:
            result["repo_available_files"] = repo_files_after  # files at the repository level (main branch only)

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_file_in_repo",
                "description": "Delete a file from a repository branch; if branch is 'main', also delete from repo-level file paths/contents. Returns remaining files.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner (account/team)."},
                        "repo_name": {"type": "string", "description": "Repository name."},
                        "branch_name": {"type": "string", "description": "Branch name (e.g., 'main')."},
                        "file_name": {"type": "string", "description": "Path/name of the file to delete."}
                    },
                    "required": ["owner", "repo_name", "branch_name", "file_name"]
                }
            }
        }
