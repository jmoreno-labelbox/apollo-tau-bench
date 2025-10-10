# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class MergePullRequest(Tool):
    """Merges the specified pull request into its base branch."""

    @staticmethod
    def invoke(data: Dict[str, Any], pr_number, repo_name) -> str:

        if not all([repo_name, pr_number]):
            return json.dumps({"error": "repo_name and pr_number are required."}, indent=2)

        me = _auth(data)["username"]
        pr = next(
            (p for p in _prs(data)
             if p["owner"] == me and p["repo_name"] == repo_name and int(pr_number) in p["pr_numbers"]),
            None
        )
        if not pr:
            return json.dumps({"error": "Pull request not found."}, indent=2)

        try:
            idx = pr["pr_numbers"].index(int(pr_number))
        except ValueError:
            return json.dumps({"error": "PR number not found in PR block."}, indent=2)

        # ✅ Check if the PR is open before proceeding.
        if pr["pr_states"][idx] != "open":
            return json.dumps({"error": "PR is not open."}, indent=2)

        # ✅ Prevent merging when head equals base (no-op merges)
        head_branch = pr["head_branches"][idx]
        base_branch = pr["base_branches"][idx]
        if head_branch == base_branch:
            pr["pr_states"][idx] = "rejected"
            return json.dumps({
                "message": "Pull request rejected.",
                "reason": "head and base branch are the same",
                "merged": "false"
            }, indent=2)

        repo = _find_repo_record(data, repo_name)
        head_idx = _branch_index(repo, head_branch)
        base_idx = _branch_index(repo, base_branch)

        # Merge = substitute base branch content with head branch content.
        repo["branch_files"][base_idx] = list(repo["branch_files"][head_idx])
        repo["branch_contents"][base_idx] = list(repo["branch_contents"][head_idx])
        repo["branch_shas"][base_idx] = get_next_commit_sha()

        pr["pr_states"][idx] = "merged"

        return json.dumps({"message": "Pull request merged.", "merged": "true", "merge_method": "merge"}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "merge_pull_request",
                "description": "Merges the pull request into base branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"}
                    },
                    "required": ["repo_name", "pr_number"]
                }
            }
        }
