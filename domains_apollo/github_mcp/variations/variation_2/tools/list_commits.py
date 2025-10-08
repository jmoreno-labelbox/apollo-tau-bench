from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class ListCommits(Tool):
    """Enumerates commits for a specified repository and optional branch."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None, branch: str = None) -> str:
        commits = _commits(data)

        for entry in commits:
            if entry["repo_name"] == repo_name:
                if not branch:
                    payload = entry
                    out = json.dumps(payload, indent=2)
                    return out

                if branch in entry["branch_names"]:
                    idx = entry["branch_names"].index(branch)
                    payload = {
                        "branch": branch,
                        "commit_shas": entry["commit_shas"][idx],
                        "messages": entry["commit_messages"][idx],
                        "authors": entry["commit_authors"][idx],
                        "timestamps": entry["commit_timestamps"][idx],
                    }
                    out = json.dumps(
                        payload, indent=2,
                    )
                    return out
        payload = {
            "branch": branch,
            "commit_shas": [],
            "messages": [],
            "authors": [],
            "timestamps": [],
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
                "name": "ListCommits",
                "description": "Lists commits in a repository and branch.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                    },
                    "required": ["repo_name"],
                },
            },
        }
