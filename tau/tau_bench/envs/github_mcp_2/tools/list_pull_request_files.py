# Sierra Copyright

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


def _resolve_pr_number(data: Dict[str, Any], repo_name: str, pr_number: Any) -> int:
    """
    Resolve PR number, handling placeholder strings by finding the most recently created PR.
    Returns the actual PR number as an integer.
    """
    # If it's a placeholder string or any non-integer, find the most recent PR
    if not isinstance(pr_number, int) or str(pr_number) == "{{PR_NUMBER}}":
        me = _auth(data)["username"]
        prs = data.get("pull_requests") or []
        block = next((b for b in prs if b.get("owner") == me and b.get("repo_name") == repo_name), None)
        if not block or not block["pr_numbers"]:
            raise Exception("No pull requests found for this repository")
        # Use the most recently created PR (last in the list)
        return block["pr_numbers"][-1]
    else:
        # Return the actual number (should be an integer)
        return int(pr_number)

def _repos(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("repositories", [])

def _prs(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("pull_requests", [])

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

class ListPullRequestFiles(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], pr_number, repo_name) -> str:
        pr_number = _resolve_pr_number(data, repo_name, pr_number)

        prs = _prs(data)
        pr_block = next((b for b in prs if b.get("repo_name") == repo_name), None)

        if not pr_block:
            return json.dumps({"error": "Pull request not found."}, indent=2)

        try:
            idx = pr_block["pr_numbers"].index(pr_number)
        except Exception:
            return json.dumps({"files": []}, indent=2)

        try:
            pr_files = pr_block["pr_files"][idx][0]
            if pr_files:
                return json.dumps({"files": pr_files}, indent=2)
        except Exception:
            pass  # alternative below

        # revert to calculating the difference
        head_branch = pr_block["head_branches"][idx]
        base_branch = pr_block["base_branches"][idx]

        try:
            repo = next(r for r in _repos(data) if r["repo_name"] == repo_name)
            head_idx = _branch_index(repo, head_branch)
            base_idx = _branch_index(repo, base_branch)

            head_files = set(repo["branch_files"][head_idx])
            base_files = set(repo["branch_files"][base_idx])

            diff_files = list(head_files.symmetric_difference(base_files))
            if not diff_files:
                return json.dumps({"error": "No file diff found in fallback."}, indent=2)

            return json.dumps({"files": diff_files}, indent=2)
        except Exception as e:
            return json.dumps({"error": f"No file diff recorded for this pull request. {str(e)}"}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "list_pull_request_files",
                "description": "Lists files changed in pull request's head branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"},
                    },
                    "required": ["repo_name", "pr_number"]
                }
            }
        }