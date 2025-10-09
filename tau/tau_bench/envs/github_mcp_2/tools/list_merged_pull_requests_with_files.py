from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class ListMergedPullRequestsWithFiles(Tool):
    """Provides merged PRs for a specified repository and owner, along with the changed files."""

    @staticmethod
    def invoke(data: dict[str, Any], owner: str = None, repo_name: str = None) -> str:
        owner = owner or _auth(data)["username"]
        if not all([owner, repo_name]):
            payload = {"error": "owner and repo_name are required."}
            out = json.dumps(payload, indent=2)
            return out

        prs = _prs(data)
        merged = [
            {"number": pr["number"], "title": pr["title"], "files": pr.get("files", [])}
            for pr in prs
            if pr.get("owner") == owner
            and pr.get("repo_name") == repo_name
            and pr.get("state") == "merged"
        ]
        payload = merged
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listMergedPullRequestsWithFiles",
                "description": "Returns merged PRs for the given owner/repo with changed files.",
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
