# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListCommits(Tool):
    """Lists commits for a given repository and optional branch."""

    @staticmethod
    def invoke(data: Dict[str, Any], branch, repo_name) -> str:
        commits = _commits(data)

        for entry in commits:
            if entry["repo_name"] == repo_name:
                if not branch:
                    return json.dumps(entry, indent=2)

                if branch in entry["branch_names"]:
                    idx = entry["branch_names"].index(branch)
                    return json.dumps({
                        "branch": branch,
                        "commit_shas": entry["commit_shas"][idx],
                        "messages": entry["commit_messages"][idx],
                        "authors": entry["commit_authors"][idx],
                        "timestamps": entry["commit_timestamps"][idx],
                    }, indent=2)

        return json.dumps({
            "branch": branch,
            "commit_shas": [],
            "messages": [],
            "authors": [],
            "timestamps": [],
        }, indent=2)


    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "list_commits",
                "description": "Lists commits in a repository and branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                    },
                    "required": ["repo_name"]
                }
            }
        }
