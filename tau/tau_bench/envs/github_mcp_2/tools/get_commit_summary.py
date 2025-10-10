# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCommitSummary(Tool):
    """Returns commit count for a given repo and owner, broken down by branch."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner") or _auth(data)["username"]
        repo_name = kwargs.get("repo_name")
        if not all([owner, repo_name]):
            return json.dumps({"error": "owner and repo_name are required."}, indent=2)

        commits = _commits(data)
        summary = {}

        for c in commits:
            if c.get("owner") == owner and c.get("repo_name") == repo_name:
                for branch, shas in zip(c["branch_names"], c["commit_shas"]):
                    summary[branch] = len(shas)

        return json.dumps({"repo_name": repo_name, "commit_summary": summary}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_commit_summary",
                "description": "Returns commit summary per branch for a repo and owner.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo_name": {"type": "string"},
                    },
                    "required": ["owner", "repo_name"]
                }
            }
        }
