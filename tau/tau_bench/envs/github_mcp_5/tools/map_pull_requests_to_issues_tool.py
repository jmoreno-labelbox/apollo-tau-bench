# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class MapPullRequestsToIssuesTool(Tool):
    """
    Map pull requests to their linked issues deterministically.

    This tool retrieves all pull requests in a repository and identifies any linked issues.
    It provides traceability from pull requests to the issues they are meant to resolve.

    Input Parameters:
        repo_name (str): The name of the repository.
        pr_ids (List[str]): A list of pull request IDs to map.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful, or "error" otherwise.
            - data: A mapping of pull request IDs to linked issue IDs.

    Errors:
        - Returns an error if `repo_name` or `pr_ids` are missing or invalid.
        - Returns an error if no links exist for the given pull requests.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
        try:
            repo_name = _validate_param(kwargs, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        prs = list(data.get("pull_requests", {}).values())

        mapping = [
            {
                "issue_id": _safe_id(pr, "issue_id", f"ISSUE_{repo_name}_", ["title", "body"]),
                "pr_id": _safe_id(pr, "pr_id", f"PR_{repo_name}_", ["title", "head_branch", "base_branch"]),
                "linked_issues": pr.get("linked_issues", []),
                "report_date": CURRENT_DATE,
            }
            for pr in prs if pr.get("repo") == repo_name
        ]
        return _response("ok", mapping)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "map_pull_requests_to_issues",
                "description": "Map pull requests deterministically to their linked issues.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }
