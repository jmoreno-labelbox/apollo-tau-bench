# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetBranchContent(Tool):
    """
    Returns branch-specific information for a given owner/repository/branch.
    Output includes: branch name, branch files, branch contents, and branch SHA,
    all aligned by the same branch index.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], branch_name = "", owner = "", repo_name = "") -> str:
        owner = owner.strip()
        repo_name = repo_name.strip()
        branch = branch_name.strip()

        if not owner or not repo_name or not branch:
            return json.dumps(
                {"error": "Parameters 'owner', 'repo_name', and 'branch' are all required."},
                indent=2
            )

        # Accept either {"repositories": [...]} format or a plain list.
        repos = list(data.get("repositories", {}).values())

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
        if branch not in branches:
            return json.dumps(
                {"error": f"Branch '{branch}' not found in repository '{owner}/{repo_name}'."},
                indent=2
            )

        idx = branches.index(branch)

        # Retrieve aligned artifacts for each branch (to handle potential missing keys)
        branch_files_all = repo.get("branch_files", [])
        branch_contents_all = repo.get("branch_contents", [])
        branch_shas_all = repo.get("branch_shas", [])

        # Fallbacks: in the absence of per-branch arrays, utilize repository-wide files/contents instead.
        files  = None
        contents  = None

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
            "branch_sha": sha
        }
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_branch_content",
                "description": "Fetch branch-level files, contents, and SHA for a given owner/repository/branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {
                            "type": "string",
                            "description": "Repository owner (account/team)."
                        },
                        "repo_name": {
                            "type": "string",
                            "description": "Repository name."
                        },
                        "branch_name": {
                            "type": "string",
                            "description": "Branch name to retrieve."
                        }
                    },
                    "required": ["owner", "repo_name", "branch_name"]
                }
            }
        }
