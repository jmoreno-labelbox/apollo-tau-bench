# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateBranch(Tool):
    """Creates a new branch from an existing branch in the repo."""

    @staticmethod
    def invoke(data: Dict[str, Any], new_branch, repo_name, source_branch) -> str:

        if not all([repo_name, source_branch, new_branch]):
            return json.dumps({"error": "repo_name, source_branch, and new_branch are required."}, indent=2)

        try:
            repo = _find_repo_record(data, repo_name)
            if new_branch in repo.get("branches", []):
                return json.dumps({"error": f"Branch '{new_branch}' already exists."}, indent=2)

            idx = _branch_index(repo, source_branch)
            repo.setdefault("branches", []).append(new_branch)
            repo.setdefault("branch_files", []).append(list(repo["branch_files"][idx]))
            repo.setdefault("branch_contents", []).append(list(repo["branch_contents"][idx]))
            repo.setdefault("branch_shas", []).append(get_next_commit_sha())

            return json.dumps({
                "message": "Branch created",
                "new_branch": new_branch,
                "from": source_branch
            }, indent=2)
        except Exception as e:
            return json.dumps({"error": str(e)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_branch",
                "description": "Creates a new branch from an existing one in the repo.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "source_branch": {"type": "string"},
                        "new_branch": {"type": "string"},
                    },
                    "required": ["repo_name", "source_branch", "new_branch"],
                },
            },
        }
