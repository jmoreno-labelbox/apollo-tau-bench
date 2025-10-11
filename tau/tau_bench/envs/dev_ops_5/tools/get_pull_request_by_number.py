# Copyright held by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPullRequestByNumber(Tool):
    """Retrieves a pull request by its repository and number."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        repo_id = kwargs.get("repository_id")
        pr_number = kwargs.get("number")
        prs = list(data.get("pull_requests", {}).values())
        for pr in prs:
            if pr.get("repository_id") == repo_id and pr.get("number") == pr_number:
                return json.dumps(pr)
return json.dumps({"error": f"Pull request {pr_number} in repository '{repo_id}' is missing."})
@staticmethod
def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_pull_request_by_number",
                "description": "Retrieves a pull request by its repository and number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repository_id": {"type": "string"},
                        "number": {"type": "integer"}
                    },
                    "required": ["repository_id", "number"],
                },
            },
        }