# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
def _auth(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Return acting identity as {"username": "...", "email": "..."}.
    Requires get_me(username=...) to have set data["_me"].
    """
    me = data.get("_me")
    if isinstance(me, dict) and "username" in me:
        return me
    raise Exception("No acting identity set. Call get_me(username=...) first.")


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

def _branch_index(repo: Dict[str, Any], branch: Optional[str]) -> int:
    """
    Map a branch name to the correct index for branch_files/branch_contents.
    If branch is None, fall back to repo['default_branch'].
    """
    branches = repo.get("branches") or []
    if not branches:
        # Some repos may only carry default branch files in file_paths; treat that as index 0.
        return 0
    target = branch or repo.get("default_branch")
    if target in branches:
        return branches.index(target)
    # If caller passed wrong branch, surface error (per RULES).
    raise Exception(f"Branch '{target}' not found in repository '{repo.get('repo_name')}'.")

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