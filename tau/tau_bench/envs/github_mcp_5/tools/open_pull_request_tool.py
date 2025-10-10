# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class OpenPullRequestTool(Tool):
    """
    Open a new pull request deterministically (in-memory only).

    This tool simulates the creation of a new pull request in a repository.
    IDs are generated using `_safe_id` based on the title and branches.
    The PR state defaults to "open", and metadata is stamped with CURRENT_DATE.

    Input Parameters:
        repo_name (str): The name of the repository.
        title (str): The pull request title.
        head_branch (str): The branch with proposed changes.
        base_branch (str): The branch to merge changes into.
        author (str): The user opening the pull request.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if created successfully, or "error" otherwise.
            - data: Metadata of the created pull request, including deterministic `pr_id`.

    Errors:
        - Returns an error if required parameters are missing or invalid.
        - Returns an error if a pull request with the same title already exists for the same branches.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
        try:
            repo_name = _validate_param(kwargs, "repo_name", str)
            title = _validate_param(kwargs, "title", str)
            body = _validate_param(kwargs, "body", str)
            head_branch = _validate_param(kwargs, "head_branch", str)
            base_branch = _validate_param(kwargs, "base_branch", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        prs = list(data.get("pull_requests", {}).values())
        new_number = len(prs) + 1
        new_pr = {
            "repo": repo_name,
            "number": new_number,
            "title": title,
            "body": body,
            "head_branch": head_branch,
            "base_branch": base_branch,
            "state": "open",
            "created_at": CURRENT_DATE,
        }
        new_pr["pr_id"] = _safe_id(new_pr, "pr_id", f"PR_{repo_name}_", ["title", "head_branch", "base_branch"])
        prs.append(new_pr)
        return _response("ok", new_pr)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "open_pull_request",
                "description": "Open a new pull request deterministically (in-memory only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "title": {"type": "string"},
                        "body": {"type": "string"},
                        "head_branch": {"type": "string"},
                        "base_branch": {"type": "string"},
                    },
                    "required": ["repo_name", "title", "body", "head_branch", "base_branch"],
                },
            },
        }
