# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListPullRequestsTool(Tool):
    """
    List all pull requests for a repository deterministically.

    This tool retrieves all pull requests for a repository.
    Each pull request is returned with a deterministic `pr_id`
    (via `_safe_id`) and includes a `report_date`.

    Input Parameters:
        repo_name (str): The name of the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful.
            - data: A list of pull requests with metadata, including:
                - pr_id (str): Deterministic unique pull request ID.
                - title (str): Pull request title.
                - state (str): Current state ("open", "closed", or "merged").
                - created_at (str): PR creation date.
                - updated_at (str): PR last update date.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` is missing or invalid.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
        try:
            repo_name = _validate_param(kwargs, "repo_name", str)
            state = kwargs.get("state")  # not mandatory
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        prs = list(data.get("pull_requests", {}).values())
        repo_prs = [
            {
                "pr_id": _safe_id(pr, "pr_id", f"PR_{repo_name}_", ["title", "head_branch", "base_branch"]),
                "title": pr.get("title"),
                "state": pr.get("state"),
                "created_at": pr.get("created_at"),
                "report_date": CURRENT_DATE,
            }
            for pr in prs
            if pr.get("repo") == repo_name and (state is None or pr.get("state") == state)
        ]
        return _response("ok", repo_prs)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_pull_requests",
                "description": "List pull requests for a repository (optionally filter by state).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "state": {"type": "string"},
                    },
                    "required": ["repo_name"],
                },
            },
        }
