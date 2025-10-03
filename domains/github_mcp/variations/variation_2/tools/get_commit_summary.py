from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class GetCommitSummary(Tool):
    """Provides the count of commits for a specified repository and owner, categorized by branch."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo_name: str = None) -> str:
        owner = owner or _auth(data)["username"]
        if not all([owner, repo_name]):
            payload = {"error": "owner and repo_name are required."}
            out = json.dumps(payload, indent=2)
            return out

        commits = _commits(data)
        summary = {}

        for c in commits:
            if c.get("owner") == owner and c.get("repo_name") == repo_name:
                for branch, shas in zip(c["branch_names"], c["commit_shas"]):
                    summary[branch] = len(shas)
        payload = {"repo_name": repo_name, "commit_summary": summary}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getCommitSummary",
                "description": "Returns commit summary per branch for a repo and owner.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string"},
                        "repo_name": {"type": "string"},
                    },
                    "required": ["owner", "repo_name"],
                },
            },
        }
