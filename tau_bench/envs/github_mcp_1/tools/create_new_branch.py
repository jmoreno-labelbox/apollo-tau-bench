from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateNewBranch(Tool):
    """
    Creates a new branch in a repository.
    - Inputs: owner, repo_name, branch_name, (optional) base_branch.
    - If base_branch is provided (or defaults to repo.default_branch), the new branch's files/contents
      are copied from it (deterministically, no timestamps).
    - Appends a deterministic branch SHA using DB size and branch index: "branch_sha_<len(repos)>_<new_index>".
    - Keeps branch_files and branch_contents aligned with branches.
    - Does NOT modify repo-level file_paths/file_contents (those reflect 'main' updates via other tools).
    """

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = "", repo_name: str = "", branch_name: str = "", base_branch: str = "") -> str:
        owner = owner.strip()
        repo_name = repo_name.strip()
        branch_name = branch_name.strip()
        base_branch = base_branch.strip()  # optional

        if not owner or not repo_name or not branch_name:
            payload = {
                    "error": "Parameters 'owner', 'repo_name', and 'branch_name' are required."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Preferred repository access pattern
        repos: list[dict[str, Any]] = data.get("repositories", [])
        if not isinstance(repos, list):
            payload = {
                    "error": "Invalid database format: expected 'repositories' to be a list."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Locate repo
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
        if branch_name in branches:
            payload = {"error": f"Branch '{branch_name}' already exists."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        # Resolve base branch (default to repo's default_branch)
        if not base_branch:
            base_branch = repo.get("default_branch", "main")

        if base_branch not in branches:
            payload = {
                    "error": f"Base branch '{base_branch}' not found in '{owner}/{repo_name}'."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        base_idx = branches.index(base_branch)

        # Ensure per-branch structures exist & are aligned
        branch_files_all: list[list[str]] = repo.setdefault("branch_files", [])
        branch_contents_all: list[list[str]] = repo.setdefault("branch_contents", [])
        while len(branch_files_all) < len(branches):
            branch_files_all.append([])
        while len(branch_contents_all) < len(branches):
            branch_contents_all.append([])

        # Prepare new branch data (copy from base deterministically)
        base_files = (
            branch_files_all[base_idx] if base_idx < len(branch_files_all) else []
        )
        base_contents = (
            branch_contents_all[base_idx] if base_idx < len(branch_contents_all) else []
        )

        new_files = list(base_files) if isinstance(base_files, list) else []
        new_contents = list(base_contents) if isinstance(base_contents, list) else []

        # New branch index will be the current length (appending at the end)
        new_branch_index = len(branches)

        # Append branch name
        branches.append(branch_name)

        # Append aligned arrays for the new branch
        branch_files_all.append(new_files)
        branch_contents_all.append(new_contents)

        # Ensure branch_shas exists and append deterministic SHA
        branch_shas: list[str] = repo.setdefault("branch_shas", [])
        # If branch_shas is shorter than existing branches, pad to align first
        while len(branch_shas) < new_branch_index:
            branch_shas.append("")  # placeholder to align lengths deterministically

        new_branch_sha = get_next_branch_sha(data)
        branch_shas.append(new_branch_sha)

        repo["updated_ts"] = get_current_updated_timestamp()

        # (No repo-level file_paths/file_contents changes here)

        add_terminal_message(
            data,
            f"Branch '{branch_name}' created in {owner}/{repo_name} from '{base_branch}'.",
            get_current_timestamp(),
        )
        payload = {
                "success": f"Branch '{branch_name}' created in {owner}/{repo_name} from '{base_branch}'.",
                "repo": f"{owner}/{repo_name}",
                "created_branch": branch_name,
                "base_branch": base_branch,
                "branch_index": new_branch_index,
                "branch_sha": new_branch_sha,
                "branch_file": new_files,
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
                "name": "CreateNewBranch",
                "description": "Create a new branch (optionally from a base branch) with deterministic SHA; copies files/contents from base.",
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
                            "description": "Name of the new branch to create.",
                        },
                        "base_branch": {
                            "type": "string",
                            "description": "Existing branch to copy from (defaults to repo default branch).",
                        },
                    },
                    "required": ["owner", "repo_name", "branch_name"],
                },
            },
        }
