from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class InitializePullRequestsBlock(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str) -> str:
        me = _auth(data)["username"]
        existing = next(
            (
                pr
                for pr in _prs(data)
                if pr["owner"] == me and pr["repo_name"] == repo_name
            ),
            None,
        )
        if existing:
            payload = {"message": "PR block already exists"}
            out = json.dumps(payload)
            return out
        _prs(data).append(
            {
                "owner": me,
                "repo_name": repo_name,
                "pr_numbers": [],
                "pr_titles": [],
                "pr_bodies": [],
                "pr_states": [],
                "head_branches": [],
                "base_branches": [],
                "head_shas": [],
                "mergeable_flags": [],
                "merged_flags": [],
                "created_ts": [],
                "updated_ts": [],
                "pr_files": [],
            }
        )
        payload = {"message": "Initialized pull_requests block for repo."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "InitializePullRequestsBlock",
                "description": "Manually initializes a pull_requests entry for a new repo",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                    },
                    "required": ["repo_name"],
                },
            },
        }
