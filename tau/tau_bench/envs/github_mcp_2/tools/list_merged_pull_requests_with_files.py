# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListMergedPullRequestsWithFiles(Tool):
    """Returns merged PRs for a given repo and owner, including changed files."""

    @staticmethod
    def invoke(data: Dict[str, Any], owner, repo_name) -> str:
        owner = owner or _auth(data)["username"]
        if not all([owner, repo_name]):
            return json.dumps({"error": "owner and repo_name are required."}, indent=2)

        prs = _prs(data)
        merged = [
            {"number": pr["number"], "title": pr["title"], "files": pr.get("files", [])}
            for pr in prs
            if pr.get("owner") == owner and pr.get("repo_name") == repo_name and pr.get("state") == "merged"
        ]
        return json.dumps(merged, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_merged_pull_requests_with_files",
                "description": "Returns merged PRs for the given owner/repo with changed files.",
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
