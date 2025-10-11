# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListPullRequests(Tool):
    """Lists pull requests for a specific repository or all repositories."""

    @staticmethod
    def invoke(data: Dict[str, Any], repo_name) -> str:
        me = _auth(data)["username"]

        result = []
        for pr in _prs(data):
            if repo_name and pr["repo_name"] != repo_name:
                continue
            result.extend([
                {
                    "owner": pr["owner"],
                    "repo_name": pr["repo_name"],
                    "pr_number": number,
                    "title": title,
                    "state": state,
                    "head_sha": head_sha,
                    "files": files
                }
                for number, title, state, head_sha, files in zip(
                    pr["pr_numbers"],
                    pr["pr_titles"],
                    pr["pr_states"],
                    pr["head_shas"],
                    [x[0] for x in pr["pr_files"]],
                )
            ])

        return json.dumps({"pull_requests": result}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "list_pull_requests",
                "description": "List all pull requests optionally filtered by repository.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {
                            "type": "string",
                            "description": "Optional name of the repository to filter PRs"
                        }
                    },
                    "required": []
                }
            }
        }
