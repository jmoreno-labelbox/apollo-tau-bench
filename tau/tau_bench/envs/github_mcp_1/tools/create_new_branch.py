# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner", "").strip()
        repo_name = kwargs.get("repo_name", "").strip()
        branch_name = kwargs.get("branch_name", "").strip()
        base_branch = kwargs.get("base_branch", "").strip()  # not mandatory

        if not owner or not repo_name or not branch_name:
            return json.dumps(
                {"error": "Parameters 'owner', 'repo_name', and 'branch_name' are required."},
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
        repo = next((r for r in repos if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if not repo:
            return json.dumps({"error": f"Repository '{owner}/{repo_name}' not found."}, indent=2)

        branches: List[str] = repo.get("branches", [])
        if branch_name in branches:
            return json.dumps({"error": f"Branch '{branch_name}' already exists."}, indent=2)

        # Determine the base branch (defaulting to the repository's default_branch).
        if not base_branch:
            base_branch = repo.get("default_branch", "main")

        if base_branch not in branches:
            return json.dumps(
                {"error": f"Base branch '{base_branch}' not found in '{owner}/{repo_name}'."},
                indent=2
            )

        base_idx = branches.index(base_branch)

        # Verify that branch-specific structures are present and properly aligned.
        branch_files_all: List[List[str]] = repo.setdefault("branch_files", [])
        branch_contents_all: List[List[str]] = repo.setdefault("branch_contents", [])
        while len(branch_files_all) < len(branches):
            branch_files_all.append([])
        while len(branch_contents_all) < len(branches):
            branch_contents_all.append([])

        # Generate new branch data (deterministically replicate from the base).
        base_files = branch_files_all[base_idx] if base_idx < len(branch_files_all) else []
        base_contents = branch_contents_all[base_idx] if base_idx < len(branch_contents_all) else []

        new_files = list(base_files) if isinstance(base_files, list) else []
        new_contents = list(base_contents) if isinstance(base_contents, list) else []

        # The new branch index will correspond to the current length, indicating an append operation at the end.
        new_branch_index = len(branches)

        # Add branch identifier
        branches.append(branch_name)

        # Concatenate aligned arrays for the new branch.
        branch_files_all.append(new_files)
        branch_contents_all.append(new_contents)

        # Verify the existence of branch_shas and add a consistent SHA.
        branch_shas: List[str] = repo.setdefault("branch_shas", [])
        # If branch_shas is smaller than current branches, add padding for alignment first.
        while len(branch_shas) < new_branch_index:
            branch_shas.append("")  # marker for consistent length alignment

        new_branch_sha = get_next_branch_sha(data)
        branch_shas.append(new_branch_sha)

        repo["updated_ts"] = get_current_updated_timestamp()

        # (No modifications to file_paths/file_contents at the repository level)

        add_terminal_message(data, f"Branch '{branch_name}' created in {owner}/{repo_name} from '{base_branch}'.", get_current_timestamp())

        return json.dumps(
            {
                "success": f"Branch '{branch_name}' created in {owner}/{repo_name} from '{base_branch}'.",
                "repo": f"{owner}/{repo_name}",
                "created_branch": branch_name,
                "base_branch": base_branch,
                "branch_index": new_branch_index,
                "branch_sha": new_branch_sha,
                "branch_file": new_files
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_branch",
                "description": "Create a new branch (optionally from a base branch) with deterministic SHA; copies files/contents from base.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner (account/team)."},
                        "repo_name": {"type": "string", "description": "Repository name."},
                        "branch_name": {"type": "string", "description": "Name of the new branch to create."},
                        "base_branch": {"type": "string", "description": "Existing branch to copy from (defaults to repo default branch)."}
                    },
                    "required": ["owner", "repo_name", "branch_name"]
                }
            }
        }
