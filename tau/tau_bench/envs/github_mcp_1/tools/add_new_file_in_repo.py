from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AddNewFileInRepo(Tool):
    """
    Appends a new file and its content to a repository branch.
    - Adds to branch_files[idx] and branch_contents[idx] (same index as the branch).
    - If branch is 'main', also adds to repo-level file_paths and file_contents.
    - Prevents duplicate file_names within the same branch.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        owner: str = "",
        repo_name: str = "",
        branch_name: str = "",
        file_name: str = "",
        file_content: str = ""
    ) -> str:
        owner = owner.strip()
        repo_name = repo_name.strip()
        branch_name = branch_name.strip()
        file_name = file_name.strip()

        if not owner or not repo_name or not branch_name or not file_name:
            payload = {
                    "error": "Parameters 'owner', 'repo_name', 'branch_name', and 'file_name' are required."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #Preferred repository access pattern
        repos = data.get("repositories", {}).values()
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
        if branch_name not in branches:
            payload = {
                    "error": f"Branch '{branch_name}' not found in repository '{owner}/{repo_name}'."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        idx = branches.index(branch_name)

        #Ensure per-branch structures exist and are aligned to branches length
        branch_files_all = repo.setdefault("branch_files", [])
        branch_contents_all = repo.setdefault("branch_contents", [])

        while len(branch_files_all) < len(branches):
            branch_files_all.append([])
        while len(branch_contents_all) < len(branches):
            branch_contents_all.append([])

        branch_files = branch_files_all[idx]
        branch_contents = branch_contents_all[idx]

        if not isinstance(branch_files, list) or not isinstance(branch_contents, list):
            payload = {
                    "error": "Invalid repository format: branch_files/branch_contents must be lists."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #Prevent duplicate file_name in the branch
        if file_name in branch_files:
            payload = {
                    "error": f"File '{file_name}' already exists in branch '{branch_name}'."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #Append to branch-scoped arrays (same index)
        branch_files.append(file_name)
        branch_contents.append(file_content)

        #If 'main' branch, also append to repo-wide file lists (avoid duplicates)
        if branch_name == "main":
            repo.setdefault("file_paths", [])
            repo.setdefault("file_contents", [])
            if file_name not in repo["file_paths"]:
                repo["file_paths"].append(file_name)
                repo["file_contents"].append(file_content)

        repo["updated_ts"] = get_current_updated_timestamp()

        add_terminal_message(
            data,
            f"Added '{file_name}' to {owner}/{repo_name}@{branch_name}.",
            get_current_timestamp(),
        )
        payload = {
                "success": f"Added '{file_name}' to {owner}/{repo_name}@{branch_name}.",
                "repo": f"{owner}/{repo_name}",
                "branch": branch_name,
                "added": {"file_name": file_name, "file_content": file_content},
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
                "name": "AddNewFileInRepo",
                "description": "Append a new file and content to a repository branch; if branch is 'main', also append to repo-level file paths/contents.",
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
                            "description": "Branch to modify (e.g., 'main').",
                        },
                        "file_name": {
                            "type": "string",
                            "description": "Path/name of the file to add (e.g., 'src/app.ts').",
                        },
                        "file_content": {
                            "type": "string",
                            "description": "File contents to store.",
                        },
                    },
                    "required": [
                        "owner",
                        "repo_name",
                        "branch_name",
                        "file_name",
                        "file_content",
                    ],
                },
            },
        }
