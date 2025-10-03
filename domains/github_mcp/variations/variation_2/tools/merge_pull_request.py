from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class MergePullRequest(Tool):
    """Integrates the specified pull request into its base branch."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, pr_number: int = None) -> str:
        if not all([repo_name, pr_number]):
            payload = {"error": "repo_name and pr_number are required."}
            out = json.dumps(
                payload, indent=2
            )
            return out

        me = _auth(data)["username"]
        pr = next(
            (
                p
                for p in _prs(data)
                if p["owner"] == me
                and p["repo_name"] == repo_name
                and int(pr_number) in p["pr_numbers"]
            ),
            None,
        )
        if not pr:
            payload = {"error": "Pull request not found."}
            out = json.dumps(payload, indent=2)
            return out

        try:
            idx = pr["pr_numbers"].index(int(pr_number))
        except ValueError:
            payload = {"error": "PR number not found in PR block."}
            out = json.dumps(payload, indent=2)
            return out

        #✅ Confirm that the PR is open before proceeding
        if pr["pr_states"][idx] != "open":
            payload = {"error": "PR is not open."}
            out = json.dumps(payload, indent=2)
            return out

        #✅ Prohibit merging when head equals base (no-operation merges)
        head_branch = pr["head_branches"][idx]
        base_branch = pr["base_branches"][idx]
        if head_branch == base_branch:
            pr["pr_states"][idx] = "rejected"
            payload = {
                    "message": "Pull request rejected.",
                    "reason": "head and base branch are the same",
                    "merged": "false",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        repo = _find_repo_record(data, repo_name)
        head_idx = _branch_index(repo, head_branch)
        base_idx = _branch_index(repo, base_branch)

        #Merge means substituting base branch content with head branch content
        repo["branch_files"][base_idx] = list(repo["branch_files"][head_idx])
        repo["branch_contents"][base_idx] = list(repo["branch_contents"][head_idx])
        repo["branch_shas"][base_idx] = get_next_commit_sha()

        pr["pr_states"][idx] = "merged"
        payload = {
                "message": "Pull request merged.",
                "merged": "true",
                "merge_method": "merge",
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "MergePullRequest",
                "description": "Merges the pull request into base branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"},
                    },
                    "required": ["repo_name", "pr_number"],
                },
            },
        }
