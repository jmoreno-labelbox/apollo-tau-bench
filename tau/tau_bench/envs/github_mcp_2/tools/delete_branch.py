from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class DeleteBranch(Tool):
    """Removes a branch from a repository, excluding the default branch (deduplicated)."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, branch: str = None) -> str:
        if not all([repo_name, branch]):
            payload = {"error": "repo_name and branch are required."}
            out = json.dumps(payload, indent=2)
            return out

        repo = _find_repo_record(data, repo_name)
        if branch == repo.get("default_branch"):
            payload = {"error": "Cannot delete the default branch."}
            out = json.dumps(payload, indent=2)
            return out

        if branch not in repo.get("branches", []):
            payload = {"error": "Branch not found."}
            out = json.dumps(payload, indent=2)
            return out

        idx = repo["branches"].index(branch)

        # Safely eliminate parallel entries
        for key in ["branches", "branch_files", "branch_contents", "branch_shas"]:
            if key in repo and len(repo[key]) > idx:
                repo[key].pop(idx)

        # Arrays that are optional
        if "branch_protections" in repo and len(repo["branch_protections"]) > idx:
            repo["branch_protections"].pop(idx)
        payload = {"message": f"Branch '{branch}' deleted from repo '{repo_name}'"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "DeleteBranch",
                "description": "Deletes a branch (except the default branch).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                    },
                    "required": ["repo_name", "branch"],
                },
            },
        }
