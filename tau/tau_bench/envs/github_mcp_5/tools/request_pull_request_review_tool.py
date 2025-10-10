# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RequestPullRequestReviewTool(Tool):
    """
    Request reviews for a pull request deterministically (in-memory only).

    This tool appends one or more reviewers to a pull request.
    Reviewers are normalized with `_normalize_user`.
    The `updated_at` field is refreshed deterministically.

    Input Parameters:
        repo_name (str): The name of the repository.
        pr_id (str): Deterministic ID of the pull request.
        reviewers (List[str]): List of reviewers to assign.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if reviewers were assigned successfully, or "error" otherwise.
            - data: Updated pull request metadata with reviewer list.

    Errors:
        - Returns an error if required parameters are missing or invalid.
        - Returns an error if the pull request does not exist.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
        try:
            repo_name = _validate_param(kwargs, "repo_name", str)
            pr_number = _validate_param(kwargs, "pr_number", int)
            reviewers = _validate_param(kwargs, "reviewers", list, required=False, subtype=str) or []
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        prs = list(data.get("pull_requests", {}).values())
        pr = next((p for p in prs if p.get("repo") == repo_name and p.get("number") == pr_number), None)

        if not pr:
            return _response("error", ERROR_MESSAGES["NOT_FOUND"].format(entity="Pull Request", entity_id=pr_number), "NOT_FOUND")

        pr["reviewers"] = [_normalize_user(r) for r in reviewers]
        pr["updated_at"] = CURRENT_DATE
        return _response("ok", pr)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "request_pull_request_review",
                "description": "Assign reviewers to a pull request deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"},
                        "reviewers": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["repo_name", "pr_number", "reviewers"],
                },
            },
        }
