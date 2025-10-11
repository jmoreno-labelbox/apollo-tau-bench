# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _find_repo_record(data: Dict[str, Any], repo_name: str) -> Dict[str, Any]:
    """
    Find a repo owned by the acting user. repositories is a LIST in our dataset,
    so iterate; do NOT use dict.get.
    """
    me = _auth(data)["username"]
    repos = data.get("repositories") or []
    for r in repos:
        if r.get("owner") == me and r.get("repo_name") == repo_name:
            return r
    # Mirror RULES: if not found, surface a crisp error (no workarounds)
    raise Exception(f"Repository not found for owner '{me}': {repo_name}")

class DeleteBranch(Tool):
    """Deletes a branch from a repository, except the default branch (deduped)."""

    @staticmethod
    def invoke(data: Dict[str, Any], branch, repo_name) -> str:

        if not all([repo_name, branch]):
            return json.dumps({"error": "repo_name and branch are required."}, indent=2)

        repo = _find_repo_record(data, repo_name)
        if branch == repo.get("default_branch"):
            return json.dumps({"error": "Cannot delete the default branch."}, indent=2)

        if branch not in repo.get("branches", []):
            return json.dumps({"error": "Branch not found."}, indent=2)

        idx = repo["branches"].index(branch)

        # Safely eliminate concurrent entries.
        for key in ["branches", "branch_files", "branch_contents", "branch_shas"]:
            if key in repo and len(repo[key]) > idx:
                repo[key].pop(idx)

        # Arrays that are not mandatory.
        if "branch_protections" in repo and len(repo["branch_protections"]) > idx:
            repo["branch_protections"].pop(idx)

        return json.dumps(
            {"message": f"Branch '{branch}' deleted from repo '{repo_name}'"}, indent=2
        )

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "delete_branch",
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