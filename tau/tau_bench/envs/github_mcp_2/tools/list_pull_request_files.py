# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListPullRequestFiles(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_name = kwargs.get("repo_name")
        pr_number = _resolve_pr_number(data, repo_name, kwargs.get("pr_number"))

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
