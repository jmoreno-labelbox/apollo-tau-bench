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

class WriteFileToBranch(Tool):
    """Adds or updates a file in a branch (does not commit)."""

    @staticmethod
    def invoke(data: Dict[str, Any], branch, content, path, repo_name) -> str:

        if not all([repo_name, branch, path, content]):
            return json.dumps({"error": "repo_name, branch, path, and content are required."}, indent=2)

        try:
            repo = _find_repo_record(data, repo_name)
            idx = _branch_index(repo, branch)

            files = repo["branch_files"][idx]
            contents = repo["branch_contents"][idx]

            if path in files:
                i = files.index(path)
                contents[i] = content
            else:
                files.append(path)
                contents.append(content)

            return json.dumps({
                "message": "File added or updated",
                "repo": repo_name,
                "branch": branch,
                "path": path
            }, indent=2)

        except Exception as e:
            return json.dumps({"error": str(e)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "write_file_to_branch",
                "description": "Adds or updates a file in the given branch (without committing).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                        "path": {"type": "string"},
                        "content": {"type": "string"}
                    },
                    "required": ["repo_name", "branch", "path", "content"]
                }
            }
        }