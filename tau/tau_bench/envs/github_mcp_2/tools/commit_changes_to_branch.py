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

def _commits(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("commits", [])

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

def _auth(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Return acting identity as {"username": "...", "email": "..."}.
    Requires get_me(username=...) to have set data["_me"].
    """
    me = data.get("_me")
    if isinstance(me, dict) and "username" in me:
        return me
    raise Exception("No acting identity set. Call get_me(username=...) first.")

class CommitChangesToBranch(Tool):
    """Commits changes to a branch with a message (generates SHA and metadata)."""

    @staticmethod
    def invoke(data: Dict[str, Any], branch, commit_message, repo_name) -> str:

        if not all([repo_name, branch, commit_message]):
            return json.dumps({"error": "repo_name, branch, and commit_message are required."}, indent=2)

        try:
            repo = _find_repo_record(data, repo_name)
            idx = _branch_index(repo, branch)

            new_sha = get_next_commit_sha()
            repo["branch_shas"][idx] = new_sha

            commits = _commits(data)
            me = _auth(data)["username"]

            commit_block = next((c for c in commits if c["owner"] == me and c["repo_name"] == repo_name), None)
            if not commit_block:
                commit_block = {
                    "owner": me,
                    "repo_name": repo_name,
                    "branch_names": [],
                    "commit_shas": [],
                    "commit_messages": [],
                    "commit_authors": [],
                    "commit_timestamps": [],
                }
                commits.append(commit_block)

            if branch not in commit_block["branch_names"]:
                commit_block["branch_names"].append(branch)
                commit_block["commit_shas"].append([new_sha])
                commit_block["commit_messages"].append([commit_message])
                commit_block["commit_authors"].append([me])
                commit_block["commit_timestamps"].append([get_current_timestamp()])
            else:
                bidx = commit_block["branch_names"].index(branch)
                commit_block["commit_shas"][bidx].append(new_sha)
                commit_block["commit_messages"][bidx].append(commit_message)
                commit_block["commit_authors"][bidx].append(me)
                commit_block["commit_timestamps"][bidx].append(get_current_timestamp())

            return json.dumps({
                "message": "Committed to branch",
                "repo": repo_name,
                "branch": branch,
                "commit_sha": new_sha,
                "commit_message": commit_message
            }, indent=2)

        except Exception as e:
            return json.dumps({"error": str(e)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "commit_changes_to_branch",
                "description": "Commits all current changes to a branch with the given message.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                        "commit_message": {"type": "string"}
                    },
                    "required": ["repo_name", "branch", "commit_message"]
                }
            }
        }