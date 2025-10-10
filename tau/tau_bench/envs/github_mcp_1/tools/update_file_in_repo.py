# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateFileInRepo(Tool):
    """
    Updates the content of an existing file in a repository branch.
    - Finds the branch by name and locates the file_name in branch_files[idx].
    - Updates branch_contents[idx] at the same file index.
    - If branch is 'main', also updates repo-level file_contents at the file_name's index.
    - Deterministic, no timestamps or randomness.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner", "").strip()
        repo_name = kwargs.get("repo_name", "").strip()
        branch_name = kwargs.get("branch_name", "").strip()
        file_name = kwargs.get("file_name", "").strip()
        file_content = kwargs.get("file_content", "")

        if not owner or not repo_name or not branch_name or not file_name:
            return json.dumps(
                {"error": "Parameters 'owner', 'repo_name', 'branch_name', and 'file_name' are required."},
                indent=2
            )

        # Recommended method for accessing the repository
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
        idx = branches.index(branch_name)

        # Verify that branch-specific structures are present and properly aligned.
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

        fidx = branch_files.index(file_name)
        # Maintain array alignment.
        while len(branch_contents) < len(branch_files):
            branch_contents.append("")

        previous_content = branch_contents[fidx]
        branch_contents[fidx] = file_content

        # If on the main branch, update the repository-level file_contents as well.
        if branch_name == "main":
            repo.setdefault("file_paths", [])
            repo.setdefault("file_contents", [])
            # Standardize lengths
            while len(repo["file_contents"]) < len(repo["file_paths"]):
                repo["file_contents"].append("")
            if file_name in repo["file_paths"]:
                ridx = repo["file_paths"].index(file_name)
                repo["file_contents"][ridx] = file_content

        repo["updated_ts"] = get_current_updated_timestamp()

        add_terminal_message(data, f"Updated '{file_name}' in {owner}/{repo_name}@{branch_name}.", get_current_updated_timestamp())

        return json.dumps(
            {
                "success": f"Updated '{file_name}' in {owner}/{repo_name}@{branch_name}.",
                "repo": f"{owner}/{repo_name}",
                "branch": branch_name,
                "file": {
                    "file_name": file_name,
                    "previous_content": previous_content,
                    "new_content": file_content
                }
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_file_in_repo",
                "description": "Update the content of an existing file in a repository branch; if branch is 'main', also update repo-level file contents.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner (account/team)."},
                        "repo_name": {"type": "string", "description": "Repository name."},
                        "branch_name": {"type": "string", "description": "Branch name (e.g., 'main')."},
                        "file_name": {"type": "string", "description": "Path/name of the file to update."},
                        "file_content": {"type": "string", "description": "New content to write into the file."}
                    },
                    "required": ["owner", "repo_name", "branch_name", "file_name", "file_content"]
                }
            }
        }
