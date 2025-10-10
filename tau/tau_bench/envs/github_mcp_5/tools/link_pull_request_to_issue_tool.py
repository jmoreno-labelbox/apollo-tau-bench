# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LinkPullRequestToIssueTool(Tool):
    """
    Link a pull request to an existing issue (in-memory only).

    This tool associates a pull request with an issue in the same repository,
    typically used to indicate that the PR addresses or resolves the issue.
    The `updated_at` timestamp is refreshed deterministically.

    Input Parameters:
        repo_name (str): The name of the repository.
        pr_id (str): Deterministic ID of the pull request to link.
        issue_id (str): Deterministic ID of the issue to link.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if the link was created successfully, or "error" otherwise.
            - data: Updated pull request metadata, including a reference to the linked issue.

    Errors:
        - Returns an error if any required parameter is missing or invalid.
        - Returns an error if the pull request or issue does not exist in the repository.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
        try:
            repo_name = _validate_param(kwargs, "repo_name", str)
            pr_number = _validate_param(kwargs, "pr_number", int)
            issue_number = _validate_param(kwargs, "issue_number", int)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        prs = list(data.get("pull_requests", {}).values())
        pr = next((p for p in prs if p.get("repo") == repo_name and p.get("number") == pr_number), None)

        if not pr:
            return _response("error", ERROR_MESSAGES["NOT_FOUND"].format(entity="Pull Request", entity_id=pr_number), "NOT_FOUND")

        pr.setdefault("linked_issues", []).append(issue_number)
        pr["updated_at"] = CURRENT_DATE
        return _response("ok", pr)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "link_pull_request_to_issue",
                "description": "Link a pull request to an issue deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"},
                        "issue_number": {"type": "integer"},
                    },
                    "required": ["repo_name", "pr_number", "issue_number"],
                },
            },
        }
