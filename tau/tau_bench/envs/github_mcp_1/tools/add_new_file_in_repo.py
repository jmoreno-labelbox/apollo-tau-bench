# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddNewFileInRepo(Tool):
    """
    Appends a new file and its content to a repository branch.
    - Adds to branch_files[idx] and branch_contents[idx] (same index as the branch).
    - If branch is 'main', also adds to repo-level file_paths and file_contents.
    - Prevents duplicate file_names within the same branch.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], branch_name = "", file_content = "", file_name = "", owner = "", repo_name = "") -> str:
        owner = owner.strip()
        repo_name = repo_name.strip()
        branch_name = branch_name.strip()
        file_name = file_name.strip()

        if not owner or not repo_name or not branch_name or not file_name:
            return json.dumps(
                {"error": "Parameters 'owner', 'repo_name', 'branch_name', and 'file_name' are required."},
                indent=2
            )

        # Optimal method for accessing the repository.
        repos = list(data.get("repositories", {}).values())
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

        branches = repo.get("branches", [])
        if branch_name not in branches:
            return json.dumps(
                {"error": f"Branch '{branch_name}' not found in repository '{owner}/{repo_name}'."},
                indent=2
            )
        idx = branches.index(branch_name)

        # Verify that per-branch structures are present and correspond to the lengths of the branches.
        branch_files_all = repo.setdefault("branch_files", [])
        branch_contents_all = repo.setdefault("branch_contents", [])

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

        # Avoid duplicate file_name within the branch.
        if file_name in branch_files:
            return json.dumps(
                {"error": f"File '{file_name}' already exists in branch '{branch_name}'."},
                indent=2
            )

        # Add to arrays scoped to the branch (at the same index)
        branch_files.append(file_name)
        branch_contents.append(file_content)

        # For the 'main' branch, additionally add to the repository-wide file lists (prevent duplicates).
        if branch_name == "main":
            repo.setdefault("file_paths", [])
            repo.setdefault("file_contents", [])
            if file_name not in repo["file_paths"]:
                repo["file_paths"].append(file_name)
                repo["file_contents"].append(file_content)

        repo["updated_ts"] = get_current_updated_timestamp()

        add_terminal_message(data, f"Added '{file_name}' to {owner}/{repo_name}@{branch_name}.", get_current_timestamp())

        return json.dumps(
            {
                "success": f"Added '{file_name}' to {owner}/{repo_name}@{branch_name}.",
                "repo": f"{owner}/{repo_name}",
                "branch": branch_name,
                "added": {
                    "file_name": file_name,
                    "file_content": file_content
                },
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_new_file_in_repo",
                "description": "Append a new file and content to a repository branch; if branch is 'main', also append to repo-level file paths/contents.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner (account/team)."},
                        "repo_name": {"type": "string", "description": "Repository name."},
                        "branch_name": {"type": "string", "description": "Branch to modify (e.g., 'main')."},
                        "file_name": {"type": "string", "description": "Path/name of the file to add (e.g., 'src/app.ts')."},
                        "file_content": {"type": "string", "description": "File contents to store."}
                    },
                    "required": ["owner", "repo_name", "branch_name", "file_name", "file_content"]
                }
            }
        }
