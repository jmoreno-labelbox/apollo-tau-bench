# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class InitializePullRequestsBlock(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], repo_name) -> str:
        me = _auth(data)["username"]
        existing = next((pr for pr in _prs(data) if pr["owner"] == me and pr["repo_name"] == repo_name), None)
        if existing:
            return json.dumps({"message": "PR block already exists"})
        _prs(data).append({
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
        })
        return json.dumps({"message": "Initialized pull_requests block for repo."})

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "initialize_pull_requests_block",
                "description": "Manually initializes a pull_requests entry for a new repo",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                    },
                    "required": ["repo_name"]
                }
            }
        }
