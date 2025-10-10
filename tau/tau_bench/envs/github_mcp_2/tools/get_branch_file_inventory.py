# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetBranchFileInventory(Tool):
    """Returns file list and latest SHA for a given branch in a repo owned by the user."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        branch = kwargs.get("branch")

        if not all([repo_name, branch]):
            return json.dumps({"error": "repo_name and branch are required."}, indent=2)

        try:
            repo = _find_repo_record(data, repo_name)
            idx = _branch_index(repo, branch)

            files = repo.get("branch_files", [])[idx]
            sha = repo.get("branch_shas", [])[idx]

            return json.dumps({
                "repo_name": repo_name,
                "branch": branch,
                "commit_sha": sha,
                "files": files
            }, indent=2)

        except Exception as e:
            return json.dumps({"error": str(e)}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_branch_file_inventory",
                "description": "Returns latest SHA and file list for a given repo and branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"}
                    },
                    "required": ["repo_name", "branch"]
                }
            }
        }
