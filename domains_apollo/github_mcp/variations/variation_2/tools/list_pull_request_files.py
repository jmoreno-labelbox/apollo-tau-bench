from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class ListPullRequestFiles(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, pr_number: int = None) -> str:
        pr_number = _resolve_pr_number(data, repo_name, pr_number)

        prs = _prs(data)
        pr_block = next((b for b in prs if b.get("repo_name") == repo_name), None)

        if not pr_block:
            payload = {"error": "Pull request not found."}
            out = json.dumps(payload, indent=2)
            return out

        try:
            idx = pr_block["pr_numbers"].index(pr_number)
        except Exception:
            payload = {"files": []}
            out = json.dumps(payload, indent=2)
            return out

        try:
            pr_files = pr_block["pr_files"][idx][0]
            if pr_files:
                payload = {"files": pr_files}
                out = json.dumps(payload, indent=2)
                return out
        except Exception:
            pass  # fallback below

        # fallback to calculate the difference
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
                payload = {"error": "No file diff found in fallback."}
                out = json.dumps(
                    payload, indent=2
                )
                return out
            payload = {"files": diff_files}
            out = json.dumps(payload, indent=2)
            return out
        except Exception as e:
            payload = {"error": f"No file diff recorded for this pull request. {str(e)}"}
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
                "name": "ListPullRequestFiles",
                "description": "Lists files changed in pull request's head branch.",
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
