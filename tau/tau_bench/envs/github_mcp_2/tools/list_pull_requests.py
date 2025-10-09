from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class ListPullRequests(Tool):
    """Enumerates pull requests for a particular repository or for all repositories."""

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str = None) -> str:
        pass
        _auth(data)["username"]

        result = []
        for pr in _prs(data):
            if repo_name and pr["repo_name"] != repo_name:
                continue
            result.extend(
                [
                    {
                        "owner": pr["owner"],
                        "repo_name": pr["repo_name"],
                        "pr_number": number,
                        "title": title,
                        "state": state,
                        "head_sha": head_sha,
                        "files": files,
                    }
                    for number, title, state, head_sha, files in zip(
                        pr["pr_numbers"],
                        pr["pr_titles"],
                        pr["pr_states"],
                        pr["head_shas"],
                        [x[0] for x in pr["pr_files"]],
                    )
                ]
            )
        payload = {"pull_requests": result}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListPullRequests",
                "description": "List all pull requests optionally filtered by repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {
                            "type": "string",
                            "description": "Optional name of the repository to filter PRs",
                        }
                    },
                    "required": [],
                },
            },
        }
